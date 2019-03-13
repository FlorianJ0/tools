#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:13:07 2018

@author: florian
"""
import os
import sys
import subprocess
import numpy as np
from PyFoam.Execution.ConvergenceRunner import ConvergenceRunner
from PyFoam.Execution.UtilityRunner import UtilityRunner
from PyFoam.LogAnalysis.BoundingLogAnalyzer import BoundingLogAnalyzer
from PyFoam.RunDictionary.SolutionFile import SolutionFile
from PyFoam.RunDictionary.SolutionDirectory import SolutionDirectory
from PyFoam.Applications.CloneCase import CloneCase
from PyFoam.Applications.Decomposer import Decomposer
from PyFoam.Execution.BasicRunner import BasicRunner

from PyFoam.RunDictionary.ParsedParameterFile import ParsedParameterFile

from icecream import ic
# subprocess.call("OFv18", shell=True)

studyPath = '/home/florianjoly/OpenFOAM/florianjoly-v1806/run/DO255M1_DA_DPPIV_GS/'
refCase = 'DO255M1_DA_DPPIV_GS_pancakes'
caseName = refCase
solver = "advDiffMicellesNoFlow"
refFile = "/home/florian/PycharmProjects/tools/openFOAM_batchrun_pancakes_POSTPROCESS_PV.py"
tmp = refFile[:-3]+'_tmp.py'
pvpath = '/home/florian/codes/ParaView-5.6.0-343-g71e8f64-MPI-Linux-64bit/bin/pvbatch'


def toASCII():
    a="foamDictionary -entry writeFormat -set ascii "+refCase+"/system/controlDict"
    subprocess.call(a, shell=True)

def tobinary():
    a="foamDictionary -entry writeFormat -set binary "+refCase+"/system/controlDict"
    subprocess.call(a, shell=True)

pancakesCenters = np.array([[1.33311696e-04, 4.51988610e-05, 0.00000000e+00],
       [8.67053063e-05, 1.82984583e-05, 0.00000000e+00],
       [6.61065130e-05, 4.78821313e-05, 0.00000000e+00],
       [1.33245134e-05, 7.44170804e-05, 0.00000000e+00],
       [4.09143092e-05, 1.00885771e-04, 0.00000000e+00],
       [7.66616591e-05, 7.04207459e-05, 0.00000000e+00],
       [6.08161931e-05, 1.33039061e-04, 0.00000000e+00],
       [1.04636926e-04, 8.91552694e-05, 0.00000000e+00],
       [1.27760557e-04, 1.16715642e-04, 0.00000000e+00],
       [7.90107847e-05, 1.13855536e-04, 0.00000000e+00],
       [1.33227401e-05, 1.51324922e-04, 0.00000000e+00],
       [1.41335505e-04, 9.18499088e-05, 0.00000000e+00],
       [9.80882076e-05, 1.45416068e-04, 0.00000000e+00]])


i = 0
force = True  # force creating folders
generate = False  # generate cases
postpro = True # run pv post process
run = False  # run simulations
nproc = 30
caseList  = []
dire=SolutionDirectory(refCase)
sol=SolutionFile(dire.initialDir(),"Ct")
#activation disk radius (m)
radius = 10e-6


if force:
    print('ARRE YOU SUUUUUUUUUUURE ?')


k = 0
if postpro:
    for pancackes in range(pancakesCenters.shape[0]):

      cp = "cp " + refFile +" " + tmp
      subprocess.call(cp, shell=True)

      sed = "sed -i 's/posx_/"+str(pancakesCenters[pancackes,0])+"/g' "+tmp
      subprocess.call(sed, shell=True)
      sed = "sed -i 's/posy_/"+str(pancakesCenters[pancackes,1])+"/g' "+tmp
      subprocess.call(sed, shell=True)
      sed = "sed -i 's/case_/"+str(k)+"/g' "+tmp
      subprocess.call(sed, shell=True)
      sed = "sed -i 's/radius_/"+str(radius)+"/g' "+tmp
      subprocess.call(sed, shell=True)
      k += 1
      pvrun = pvpath + ' ' + tmp
      subprocess.call(pvrun, shell=True)


if generate:
    os.chdir(studyPath)
    for pancackes in range(pancakesCenters.shape[0]):
#        toASCII()

        activator = 'funkySetFields -case '+refCase+' -field Ct -expression "0" -condition "1>0" -time "0"'
        subprocess.call(activator, shell=True)

        activator = 'funkySetFields -case '+refCase+' -field Ct -expression "1e-3" -condition "(pow(pos().x-'+str(pancakesCenters[pancackes,0])+',2) + pow(pos().y-'+str(pancakesCenters[pancackes,1])+',2) < pow('+str(radius)+',2) )&&(pos().z>0) && (pos().z<=(1e-6+0))" -time "0"'

        subprocess.call(activator, shell=True)
        dire=SolutionDirectory(refCase)
        sol=SolutionFile(dire.initialDir(),"Ct")
        sol.replaceBoundary("inlet","0")
        a= 'sh fixInlet.sh'
        subprocess.call(a, shell=True)

#        tobinary()
                # parallel decomposition
        if nproc > 1:
            args = ["--method=scotch", "--clear", refCase, nproc]
            Decomposer(args=args)

        run = BasicRunner(
            argv=[
                solver,
                "-case",
                caseName],
            silent=True,
            noLog=False)
        run.start()
        runCmd = 'pyFoamRunner.py advDiffMicellesNoFlow -case '+caseName+' > /dev/null 2>&1 &'
        # subprocess.call(runCmd, shell=True)
        post = 'mpirun -np ' + str(nproc) + ' foamToEnsight -case '+refCase+' -parallel -name pancanke_noflow_radius='+str(radius)+'_loc='+str(pancackes)
        subprocess.call(post, shell=True)
        a = "rm 0/t* 0/*.backup"
        subprocess.call(a, shell=True)