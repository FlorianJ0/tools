import subprocess

p1_pre_LT_R = {'nBC':78, 'idInletVC':38,'idOutletVC':8, 'idWall':1,'scale':0.001}
p1_pos_LT_R = {'nBC':38, 'idInletVC':3,'idOutletVC':2, 'idWall':1,'scale':0.001}
p1_pos_RC_V = {'nBC':38, 'idInletVC':1,'idOutletVC':2, 'idWall':38,'scale':0.001}
p1_pos_LL_V = {'nBC':38, 'idInletVC':17,'idOutletVC':9, 'idWall':1,'scale':0.001}

p2_pre_LL_R = {'nBC':39 , 'idInletVC':6,'idOutletVC':3, 'idWall':1,'scale':0.001}
p2_pos_LL_R = {'nBC':29, 'idInletVC':8,'idOutletVC':4, 'idWall':1,'scale':0.001}
p2_pos_RC_V = {'nBC':27, 'idInletVC':25,'idOutletVC':4, 'idWall':1,'scale':0.001}
p2_pos_LT_V = {'nBC':29, 'idInletVC':2,'idOutletVC':4, 'idWall':26,'scale':0.001}

p1 = ['p1_pre_LT_R', 'p1_pos_LT_R', 'p1_pos_RC_V','p1_pos_LL_V']
#p1 = ['p1_pre_LT_R']

pp1 = [p1_pre_LT_R,p1_pos_LT_R,p1_pos_RC_V,p1_pos_LL_V]
p2 = ['p2_pre_LL_R', 'p2_pos_LL_R', 'p2_pos_RC_V','p2_pos_LT_V']   
pp2 = [p2_pre_LL_R,p2_pos_LL_R,p2_pos_RC_V,p2_pos_LT_V] 
folder = '/home/florian/codes/liverSim/simus/B1/'
p=p1
pp=pp1
k=0
#what to do ?
surf = 1
vol = 1
bl = 1
for i in p:
    fname = folder + 'p1/' +str(i)+'/'+str(i)+'_surf'
    print(fname)
    nBC = pp[k]['nBC']
    idInletVC = pp[k]['idInletVC']
    idOutletVC = pp[k]['idOutletVC']
    idWall = pp[k]['idWall']
    
    
    listBC = list(range(nBC + 1))[1:]
    listBC.pop(0)
    listHV = list(range(nBC + 1))[1:]
    scale = 'm'
    
    listHV.pop(listHV.index(idInletVC))
    listHV.pop(listHV.index(idOutletVC))
    listHV.pop(listHV.index(idWall))
    print(listHV)
    
    dwall = [0.0005, 0.0009, 0.5]
    dbc = [0.0004, 0.0006, 0.051]
    if scale == 'm':
        dwall = [1.0, 1.3, 0.02 ]
        dbc = [0.5, 0.8, 0.03]
    bcType = 'type = \''
    bcTypevalue = 'typeValue = \''
    bcNumLabel = 'numLabel = \''
    bcLabel = 'label = \''
    bcVariable = 'variable =  \''
    bcComp = 'component =  \''
    bcValue = 'value =  \''
    
    # write mmgs conf file
    a = 'parameters \n' + str(nBC) + '\n'
    a += str(idWall) + ' Triangles ' + str(dwall[0]) + ' ' + str(dwall[1]) + ' ' + str(dwall[2]) + '\n' + str(
            idInletVC) + ' Triangles ' + str(dbc[0]) + ' ' + str(dbc[1]) + ' ' + str(dbc[2]) + '\n' + str(
            idOutletVC) + ' Triangles ' + str(dbc[0]) + ' ' + str(dbc[1]) + ' ' + str(dbc[2]) + '\n'
    for i in listHV:
        a += str(i) + ' Triangles ' + str(dbc[0]) + ' ' + str(dbc[1]) + ' ' + str(dbc[2]) + '\n'
    
    with open(fname + '.mmgs', 'w') as f:
        f.write(a)
    
    # write gmsh conf file
    a = 'Merge "' + fname + '_mmgs.mesh";\n'
    for i in range(nBC):
        i += 1
        a += 'Surface Loop(' + str(i) + ') = {' + str(i) + '};\n'
    
    a += 'Volume(1) = {'
    for i in range(nBC):
        i += 1
        if i == nBC:
            a += str(i)
        else:
            a += str(i) + ', '
    a += '};'
    with open(fname + '.geo', 'w') as f:
        f.write(a)
    
    # write Bloom conf file
    a = '#Anisotropic \nBLReference \n'
    a += '1\n' + str(idWall) + '\n'
    a += 'BLImprintReference \n' + str(nBC - 1) + '\n'
    for i in listHV:
        a += str(i) + ' '
    a += str(idOutletVC) + ' ' + str(idInletVC) + '\n'
    if scale == 'm':
        ispace = 0.2
    else:
        ispace = 0.0002
    a += 'NumberOfLayers \n3 \nInitialSpacing \n' + str(
        ispace) + ' \nGrowthRate \n1.15 \nMeshDeformationReference \n1 \n1 \nMeshDegradationLevel1'
    with open(fname + '_vol.bloom', 'w') as f:
        f.write(a)
    
    # run surf/vol/BL
    if surf:
        subprocess.call("/home/florian/codes/mmg-5.2.4-Linux-4.2.0-1-amd64/bin/mmgs_O3 -in " + fname + '.mesh -out ' + fname + '_mmgs.mesh', shell=True)
    if vol:
        subprocess.call('/home/florian/codes/gmsh-3.0.6-Linux64/bin/gmsh -nt 3 -3 -o ' + fname + '_vol.mesh ' + fname + '.geo',
                         shell=True)
    if bl:
        subprocess.call('/home/florian/codes/gamma3/bin/linux64/bloom -in ' + fname + '_vol.mesh  -v 6 -f -out ' + fname + '_volbl',
                     shell=True)
    # g/enerate BC section of data file for felisce
    
    # time varying flow rate inlet VC
    
    bcType = bcType + 'Dirichlet '
    bcTypevalue = bcTypevalue + 'FunctionTS '
    bcNumLabel = bcNumLabel + str(1) + ' '
    bcLabel = bcLabel + str(idInletVC) + ' '
    bcVariable = bcVariable + 'velocity '
    bcComp = bcComp + 'Comp1 '
    bcValue = bcValue + str(0) + ' '
    
    bcType = bcType + 'Dirichlet '
    bcTypevalue = bcTypevalue + 'FunctionTS '
    bcNumLabel = bcNumLabel + str(1) + ' '
    bcLabel = bcLabel + str(idInletVC) + ' '
    bcVariable = bcVariable + 'velocity '
    bcComp = bcComp + 'Comp2 '
    bcValue = bcValue + str(0) + ' '
    
    bcType = bcType + 'Dirichlet '
    bcTypevalue = bcTypevalue + 'FunctionTS '
    bcNumLabel = bcNumLabel + str(1) + ' '
    bcLabel = bcLabel + str(idInletVC) + ' '
    bcVariable = bcVariable + 'velocity '
    bcComp = bcComp + 'Comp3 '
    bcValue = bcValue + str(0) + ' '
    
    for i in listHV:
        bcType = bcType + 'Dirichlet Dirichlet Dirichlet '
        bcTypevalue = bcTypevalue + 'FunctionTS FunctionTS FunctionTS '
        bcNumLabel = bcNumLabel + ' 1 1 1 '
        bcLabel = bcLabel + str(i) + ' ' + str(i) + ' ' + str(i) + ' '
        bcVariable = bcVariable + 'velocity  velocity  velocity '
        bcComp = bcComp + 'Comp1 Comp2 Comp3 '
        bcValue = bcValue + ' 0 0 0 '
    #
    # for i in listHV:
    #     bcType = bcType + 'Dirichlet '
    #     bcTypevalue = bcTypevalue + 'FunctionTS '
    #     bcNumLabel = bcNumLabel + str(1) + ' '
    #     bcLabel = bcLabel + str(i) + ' '
    #     bcVariable = bcVariable + 'velocity '
    #     bcComp = bcComp + 'Comp2 '
    #     bcValue = bcValue + str(0) + ' '
    #
    # for i in listHV:
    #     bcType = bcType + 'Dirichlet '
    #     bcTypevalue = bcTypevalue + 'FunctionTS '
    #     bcNumLabel = bcNumLabel + str(1) + ' '
    #     bcLabel = bcLabel + str(i) + ' '
    #     bcVariable = bcVariable + 'velocity '
    #     bcComp = bcComp + 'Comp3 '
    #     bcValue = bcValue + str(0) + ' '
    
    # no slip BC wall
    bcType = bcType + 'Dirichlet '
    bcTypevalue = bcTypevalue + 'Constant '
    bcNumLabel = bcNumLabel + str(1) + ' '
    bcLabel = bcLabel + str(idWall) + ' '
    bcVariable = bcVariable + 'velocity '
    bcComp = bcComp + 'Comp123 '
    bcValue = bcValue + str(0) + ' ' + str(0) + ' ' + str(0) + ' '
    
    # pressure outlet VC
    bcType = bcType + 'NeumannNormal '
    bcTypevalue = bcTypevalue + 'Constant '
    bcNumLabel = bcNumLabel + str(1) + ' '
    bcLabel = bcLabel + str(idOutletVC) + ' '
    bcVariable = bcVariable + 'velocity '
    bcComp = bcComp + 'CompNA '
    bcValue = bcValue + str(0) + ' '
    
    print(
            bcType + '\'' + '\n' + bcTypevalue + '\'' + '\n' + bcNumLabel + '\'' + '\n' + bcLabel + '\'' + '\n' + bcVariable + '\'' + '\n' + bcComp + '\'' + '\n' + bcValue + '\'')
    with open(fname + '.data', 'w') as f:
        f.write(
                bcType + '\'' + '\n' + bcTypevalue + '\'' + '\n' + bcNumLabel + '\'' + '\n' + bcLabel + '\'' + '\n' + bcVariable + '\'' + '\n' + bcComp + '\'' + '\n' + bcValue + '\'')
    k+=1