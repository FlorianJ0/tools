__author__ = 'Florian'
import os
import time
from vmtk import pypes
from vmtk import vmtkscripts
from time import time

surfaceFile = '/home/florian/liverSim/morpho_analysis/test_surf_open_small.vtp'
centerlinesFileName = surfaceFile[:-4] + '_ctrlTEST1.vtp'
# centerlinesFile = '/home/florian/liverSim/images/nkouka_piggy_LL/nkouka_ctrlines.vtp'

if not os.path.isfile(surfaceFile):
    print('check your input, exiting code\n you failed on the', time.asctime(time.localtime(time.time())))
    exit()

start_time = time()

args = "vmtksurfacereader -ifile " + surfaceFile
myPype = pypes.PypeRun(args)
mySurface = myPype.GetScriptObject('vmtksurfacereader', '0').Surface

myctrl = vmtkscripts.vmtkCenterlines()
myctrl.Surface = mySurface
myctrl.SeedSelectorName = 'openprofiles'
# myctrl.Centerlines = centerlinesFile
myctrl.Execute()

myattr = vmtkscripts.vmtkCenterlineAttributes()
myattr.Centerlines = myctrl.Centerlines
myattr.Execute()

mybranchextractor = vmtkscripts.vmtkBranchExtractor()
mybranchextractor.Centerlines = myattr.Centerlines
mybranchextractor.RadiusArrayName = 'MaximumInscribedSphereRadius'
mybranchextractor.Execute()

# mywriter = vmtkscripts.vmtkSurfaceWriter()
# mywriter.Surface = mybranchextractor.Centerlines
# mywriter.OutputFileName = centerlinesFileName
# mywriter.Execute()



mybifref = vmtkscripts.vmtkBoundaryReferenceSystems()
mybifref.Surface = mybranchextractor.Centerlines
mybifref.Execute()

# mywriter = vmtkscripts.vmtkSurfaceWriter()
# mywriter.Surface = mybifref.Centerlines
# mywriter.OutputFileName = centerlinesFileName[:-4]+'.dat'
# mywriter.Execute()

myvect = vmtkscripts.vmtkBifurcationVectors()
myvect.Surface = mybifref.Centerlines
myvect.Execute()



# ctrl = " vmtkcenterlines -ifile " + surfaceFile + " -ofile " + centerlinesFile + " -seedselector openprofiles"
# myPype = pypes.PypeRun(ctrl)
'''
att = "vmtkcenterlineattributes -ifile " + centerlinesFile + " -ofile " + surfaceFile[:-4] + '_ctrlAtt.vtp'
myPype = pypes.PypeRun(att)

branch = "vmtkbranchextractor -ifile " + surfaceFile[
                                         :-4] + "_ctrlAtt.vtp -radiusarray@ MaximumInscribedSphereRadius --pipe  vmtkbifurcationreferencesystems -ofile " + surfaceFile[
                                                                                                                                                            :-4] + '_ctrlBranchBif.vtp'
myPype = pypes.PypeRun(branch)

# find ref group id
branch = "vmtkbranchextractor -ifile " + surfaceFile[
                                         :-4] + "_ctrlAtt.vtp -radiusarray@ MaximumInscribedSphereRadius --pipe vmtkcenterlineviewer -cellarray GroupIds"
myPype = pypes.PypeRun(branch)
ref = 43

# offsettting
off = "vmtkcenterlineattributes -ifile " + surfaceFile[
                                           :-4] + "_ctrlAtt.vtp --pipe vmtkbranchextractor -radiusarray@ MaximumInscribedSphereRadius --pipe vmtkbifurcationreferencesystems --pipe vmtkcenterlineoffsetattributes -referencegroupid " + str(ref) + " -ofile " + surfaceFile[:-4] + '_ctrloff.vtp'
# myPype = pypes.PypeRun(off)

#bif geom
# bif = "vmtkbifurcationreferencesystems -ifile "+surfaceFile[:-4] + "_ctrlBranchBif.vtp  --pipe vmtkbifurcationvectors -ofile " + surfaceFile[:-4] + '_ctrlbiffref.vtp'
bif = "vmtkcenterlines -ifile "+ surfaceFile + " -seedselector openprofiles --pipe vmtkbranchextractor --pipe vmtkbifurcationreferencesystems --pipe vmtkbifurcationvectors -ofile " + surfaceFile[:-4] +" _ctrlbiffref.vtp"
myPype = pypes.PypeRun(bif)

#smoth ctrl
sm = "vmtkcenterlinegeometry -ifile " + centerlinesFile + " -smoothing 1 -iterations 100 -factor 0.1 -outputsmoothed 1 -ofile " + centerlinesFile[:-4]+"sm.vtp"
sm = " vmtkcenterlines -ifile "+surfaceFile+ " -seedselector openprofiles --pipe vmtkbranchextractor --pipe vmtkbranchgeometry -ofile "+ centerlinesFile[:-4]+"geom.vtp"
myPype = pypes.PypeRun(sm)
'''