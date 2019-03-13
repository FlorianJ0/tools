import lcmaes
import os
import random
import re
import subprocess
from shutil import copyfile
from time import time
import numpy as np
import matplotlib.pyplot as plt
from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import cma_multiplt as lcmaplt

rootRAM = '/home/florian/lumpedflow/trunk/Models/LiverProject/ClosedLoop/PatientModel/RightLeftLiv_original/'
os.chdir(rootRAM + '/src/')
infile = rootRAM + '/headers/ConfFile/Patient_BFAW.h'
solfile = rootRAM + '/src/tmp.out'
copyfile(infile, infile + '.bak')
optimfile = infile + '.optim'
outfile = os.path.split(infile)[0] + '/optimoutput.dat'
copyfile(infile, optimfile)
callMake = 'make clean; make -j 3'
callOutput = './output'
fplot_current = rootRAM + '/src/lcmaes.dat'
optim = True
sensi = False


def lossL2(a, b, w):
    # imposer b = mes , a = simu
    q = (a - b) / b
    return np.sqrt((w * q * q).sum())


conv = 1333.27
T = 1000
scoreList = [0] * 2000  # for plotting
niter = 0  # for plotting
names = ['HVPG', 'Qao ', 'Pao ', 'Ppv ', 'Qpv ', 'Qha ']
curriter = 0

# measured values
HVPG_m = 2
Qao_m = 3.7
Pao_m = 72
Ppv_m = 11
Qpv_m = 0.760
Qha_m = 0.134
refs = np.array([HVPG_m, Qao_m, Pao_m, Ppv_m, Qpv_m, Qha_m])

# corresponding weights
HVPG_w = 1
Qao_w = 1
Pao_w = 1
Ppv_w = 2 / 3.
Qpv_w = 1 / 3.
Qha_w = 1 / 3.
weigths = np.array([HVPG_w, Qao_w, Pao_w, Ppv_w, Qpv_w, Qha_w])
smWeights = np.sum(weigths)
weigths /= smWeights

FNULL = open('/dev/null', 'w')
xplot = np.linspace(0, 1, 10)
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(xplot, np.empty(np.shape(xplot)), 'r-')  # Returns a tuple of line objects, thus the comma


def generator():
    # measured values. If they dont exist, replace by <0 values
    Ppv = 11
    Pra = 9
    HVPG = 2
    Qao = 3.7
    Pao = 72
    Qpv = 0.760
    Qha = 0.134
    HR = 66

    # computing missing and extra values
    if Qha < 0:
        Qha = 0.05 * Qao

    if Qpv < 0:
        Qpv = 0.2 * Qao

    Pt = Pra + 0.5 * (Ppv - Pra)
    P0 = Ppv * 1333  # pression porte mesuree perop en cgs
    Tcc = 60 / HR  # temps cycle cardiaque
    Tvc = 0.34 * Tcc  # temps contraction ventricule
    Tvr = 0.15 * Tcc  # temps relaxation ventricule
    Tac = 0.17 * Tcc  # temps contraction atriale
    Tar = 0.17 * Tcc  # temps relaxation atriale
    tac = 0.8 * Tcc  # debut contration atriale
    tar = Tac + tac  # debut relaxation atriale
    Req = (Pao - Pra) * 1333.27 / (Qao)  # Resistance equivalente
    Rmestotal = (Pao - Ppv) * 1333.27 / (Qpv)
    RmesP = 0.1 * Rmestotal
    RmesD = 0.9 * Rmestotal
    Rresttot = (1 / (1 / Req - 1 / Rmestotal - 1 / Rha))
    RrestP = 100
    RrestD = Rresttot - RrestP
    Rha = (Pao - Pt) * 1333.27 / (Qha)
    Rpv = (Ppv - Pt) * 1333.27 / (Qpv)
    Rhv = (Pt - Pra) * 1333.27 / (Qpv + Qha)
    RmesP = (Pao - Ppv0) * 1333.27 / (Qpv)
    RpulP = 53.33
    RpulD = 53.33

    # filling patient.h
    with open(infile, 'r') as f:
        read_data = f.read()
    newstring = re.sub('Tcc	RCONST\(1.07\)', 'Tcc RCONST(' + str(Tcc) + ')', read_data)
    newstring = re.sub('Eb_RA RCONST\(93.31\)', 'Eb_RA RCONST(' + str(Eb_RA) + ')', newstring)

    with open(infile, 'r+') as f:
        f.write(newstring)


def ploplo(iter):
    print(iter, fplot_current, 'plotting')
    dat = np.loadtxt(fplot_current)
    # print('shape', dat.shape, dat[0])
    # number of static variables at the head of every line (i.e. independent of problem dimension)
    single_values = 4
    costf = dat[1:, 0]
    yval = np.zeros(np.shape(xplot))
    # print(len(costf), costf)
    yval[:np.shape(costf)[0]] = costf
    print(yval)
    line1.set_ydata(yval)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.show()


def f(x, n):
    global curriter
    if curriter == 0:
        prev_refs = np.empty(refs.shape[0])  # for optim win gradient

    fixInitialCond = True  # update initial condition at each run
    t0 = time()
    # attribute input values
    # relier Ea/Ea L et Eb/Eb R
    hdict = {'Ea_RA': 79.98, 'Eb_RA': 93.31, 'Ea_RV': 733.15, 'Eb_RV': 66.65, 'Ea_LA': 93.31, 'Eb_LA': 119.97,
             'Ea_LV': 3665.75, 'Eb_LV': 106.64}
    # coeff
    alpha_a = x[0]
    alpha_b = x[0]
    beta_a = x[1]
    beta_b = x[1]
    print('******************\n')

    print(' alpha_a = {0:0.2}\t alpha_b = {1:0.2f}\n beta_a = {2:0.2f}\t beta_b = {3:0.2f}\n '.format(alpha_a, alpha_b,
                                                                                                      beta_a, beta_b))

    Ea_RA = alpha_a * hdict['Ea_RA']
    Eb_RA = alpha_b * hdict['Eb_RA']
    Ea_RV = alpha_a * hdict['Ea_RV']
    Eb_RV = alpha_b * hdict['Eb_RV']
    Ea_LA = beta_a * hdict['Ea_LA']
    Eb_LA = beta_b * hdict['Eb_LA']
    Ea_LV = beta_a * hdict['Ea_LV']
    Eb_LV = beta_b * hdict['Eb_LV']

    # write values to 0d code input file
    with open(infile, 'r') as f:
        read_data = f.read()

    newstring = re.sub('Ea_RA RCONST\(79.98\)', 'Ea_RA RCONST(' + str(Ea_RA) + ')', read_data)
    newstring = re.sub('Eb_RA RCONST\(93.31\)', 'Eb_RA RCONST(' + str(Eb_RA) + ')', newstring)
    newstring = re.sub('Ea_RV RCONST\(733.15\)', 'Ea_RV RCONST(' + str(Ea_RV) + ')', newstring)
    newstring = re.sub('Eb_RV RCONST\(66.65\)', 'Eb_RV RCONST(' + str(Eb_RV) + ')', newstring)
    newstring = re.sub('Ea_LA RCONST\(93.31\)', 'Ea_LA RCONST(' + str(Ea_LA) + ')', newstring)
    newstring = re.sub('Eb_LA RCONST\(119.97\)', 'Eb_LA RCONST(' + str(Eb_LA) + ')', newstring)
    newstring = re.sub('Ea_LV RCONST\(3665.75\)', 'Ea_LV RCONST(' + str(Ea_LV) + ')', newstring)
    newstring = re.sub('Eb_LV RCONST\(106.64\)', 'Eb_LV RCONST(' + str(Eb_LV) + ')', newstring)

    curriter += 1
    if fixInitialCond and os.path.getsize(solfile) and curriter == 10:
        print('Updating initial conditons')
        Sol = np.loadtxt(solfile)
        Sol = np.array(Sol)
        Pra0 = Sol[:, 15][-1]
        Prv0 = Sol[:, 30][-1]
        Pla0 = Sol[:, 17][-1]
        Plv0 = Sol[:, 18][-1]
        Pp0 = Sol[:, 22][-1]
        Pp_pul0 = Sol[:, 20][-1]
        Pp_mes0 = Sol[:, 23][-1]
        Pt_L0 = Sol[:, 31][-1]
        newstring = re.sub('Pp_0 RCONST\(92029.0\)', 'Pp_0 RCONST(' + str(Pp0) + ')', newstring)
        newstring = re.sub('Pp_pul_0 RCONST\(19337.0\)', ' Pp_pul_0 RCONST(' + str(Pp_pul0) + ')', newstring)
        newstring = re.sub('Pp_mes_0 RCONST\(105620.0\)', ' Pp_mes_0 RCONST(' + str(Pp_mes0) + ')', newstring)
        newstring = re.sub('Pt_0 RCONST\(17039.0\)', ' Pt_0 RCONST(' + str(Pt_L0) + ')', newstring)
        newstring = re.sub('Pra_0 RCONST\(9160.5\)', ' Pra_0 RCONST(' + str(Pra0) + ')', newstring)
        newstring = re.sub('Prv_0 RCONST\(8022.0\)', ' Prv_0 RCONST(' + str(Prv0) + ')', newstring)
        newstring = re.sub('Pla_0 RCONST\(17181.0\)', ' Pla_0 RCONST(' + str(Pla0) + ')', newstring)
        newstring = re.sub('Plv_0 RCONST\(16439.0\)', ' Plv_0 RCONST(' + str(Plv0) + ')', newstring)

    with open(optimfile, 'r+') as f:
        f.write(newstring)

    # compile and run 0d code
    subprocess.call(callMake + ';' + callOutput, shell=True, stdout=FNULL, stderr=FNULL)
    # subprocess.call(callMake + ';' + callOutput, shell=True)

    # Load code solution
    Sol = np.loadtxt(solfile)
    Sol = np.array(Sol)
    Sol = np.mean(Sol, axis=0)
    Pao = Sol[21]
    Qao = Sol[11]
    Pp = Sol[22]
    Qpv_L = Sol[24]
    Qpv_R = Sol[25]
    Qha_L = Sol[26]
    Qha_R = Sol[27]
    Qhv_L = Sol[28]
    Qhv_R = Sol[29]
    Ppv = Sol[30]
    Pra = Sol[15]
    HVPG = Ppv - Pra
    Qha = Qha_L + Qha_R
    Qpv = Qpv_L + Qpv_R
    Qhv = Qhv_L + Qhv_R

    # optimization target values
    vals = np.array([HVPG / conv, Qao * 60 / 1000, Pao / conv, Ppv / conv, Qpv * 60 / 1000,
                     Qha * 60 / 1000])
    lL = lossL2(vals, np.abs(refs-prev_refs), weigths)
    prev_refs = refs
    np.append(vals, curriter)
    np.save('computed_pQ', vals)
    print('L2 distance = {0:0.2f}'.format(lL))

    for i in range(len(names)):
        print('{0}\t:\t{1:0.2f}\t{2:0.2f}\t{3:0.2f} %'.format(names[i], vals[i], refs[i],
                                                              100 * (vals[i] - refs[i]) / refs[i]))

    print("iter {0} run time = {1:0.2} s".format(curriter, time() - t0))
    if curriter > 5 and curriter % 25 == 0:
        lcmaplt.plot(fplot_current)
    return lL


x = [79.98, 733.15, 93.31, 3665.75]  # Ea et Eb=f(Ea)
x0 = [79.98, 93.31, 733.15, 66.65, 93.31, 119.97, 3665.75, 106.64]
x = [1, 1, 1, 1]
x = [1, 1]
'''
bnds = (
(0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None),
(0, None), (0, None), (0, None), (0, None), (0, None))
print(optimize.minimize(f, x, method="BFGS", bounds=bnds))
'''
olambda = len(x)  # lambda is a reserved keyword in python, using olambda instead.
seed = 0  # 0 for seed auto-generated within the lib.
sigma = 0.4
# scaling = [int(1000 * random.random()) for i in range(10)]
# shift = [int(1000 * random.random()) for i in range(10)]
lbounds = [i * 0.1 for i in x]
ubounds = [i * 10 for i in x]
if optim:
    print("Running CMA-ES")
    gp = lcmaes.make_genopheno_pwqb_ls(lbounds, ubounds, olambda)
    p = lcmaes.make_parameters_pwqb_ls(x, sigma, gp, olambda, seed)
    # p.set_str_algo("acmaes")
    p.set_max_iter(500)
    p.set_ftarget(0.15)
    p.set_full_fplot(0)
    p.set_fplot(fplot_current)

    # p.set_full_fplot(1)
    # scaling = [int(1000*random.random()) for i in range(10)]
    # shift = [int(1000*random.random()) for i in range(10)]

    # generate a function object
    objfunc = lcmaes.fitfunc_pbf.from_callable(f)

    # pass the function and parameter to cmaes, run optimization and collect solution object.
    cmasols = lcmaes.pcmaes_pwqb_ls(objfunc, p)

    # collect and inspect results
    bcand = cmasols.best_candidate()
    bx = lcmaes.get_candidate_x(bcand)
    print("best x=", bx)
    print("distribution mean=", lcmaes.get_solution_xmean(cmasols))
    cov = lcmaes.get_solution_cov(cmasols)  # numpy array
    # print("cov=", cov)
    print("elapsed time= {0:0.2} min".format(1e-3 * cmasols.elapsed_time() / 60))

if sensi:
    print("Running sensibility analysis")
    '''
    problem = {
        'num_vars': 8,
        'names': ['Ea_RA', 'Eb_RA', 'Ea_RV', 'Eb_RV', 'Ea_LA', 'Eb_LA', 'Ea_LV', 'Eb_LV'],
        'bounds': [[lbounds[0], ubounds[0]],
                   [lbounds[1], ubounds[1]],
                   [lbounds[2], ubounds[2]],
                   [lbounds[3], ubounds[3]],
                   [lbounds[4], ubounds[4]],
                   [lbounds[5], ubounds[5]],
                   [lbounds[6], ubounds[6]],
                   [lbounds[7], ubounds[7]]]
    }
    '''
    problem = {
        'num_vars': 2,
        'names': ['alpha', 'beta'],
        'bounds': [[lbounds[0], ubounds[0]],
                   [lbounds[1], ubounds[1]]]
    }
    param_values = saltelli.sample(problem, 10)
    Y = np.zeros([param_values.shape[0]])

    for i, X in enumerate(param_values):
        print('i', i)
        Y[i] = f(X, problem['num_vars'])

    Si = sobol.analyze(problem, Y, print_to_console=True)
