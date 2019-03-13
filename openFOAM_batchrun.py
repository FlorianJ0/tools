#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:13:07 2018

@author: florian
"""
import os
import sys
import subprocess

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

studyPath = '/home/florian/OpenFOAM/florian-dev/run/'
refCase = 'BDCoHBC_stationnary'
solver = "advDiffMicellesNoFlow"

os.chdir(studyPath)

ccmcList = [25e-3, 50e-3, 100e-3]
CbcList = [0, 10e-3, 100e-3]
CbdList = CbcList.copy()
CbdList.append(0)
i = 0
force = True  # force creating folders
generate = True  # generate cases
run = False  # run simulations
nproc = 1
caseList  = []

if force:
    print('ARRE YOU SUUUUUUUUUUURE ?')

if generate:
    for Ccmc in ccmcList:
        for Cbd in CbdList:
            for Cbc in CbcList:
                print(
                    'Step {}, Ccmc = {}, Cbd = {}, Cbc = {}'.format(
                        i, Ccmc, Cbd, Cbc))
                if i == 2:
                    break
                caseName = str(i) + '_Ccmc' + str(Ccmc) + '_Cbd' + \
                    str(Cbd) + '_Cbc' + str(Cbc)
                caseName = caseName.replace(".", "")
                caseList.append(caseName)
                if force:
                    CloneCase(args=[refCase, caseName, '--force'])
                else:
                    try:
                        CloneCase(args=[refCase, caseName])
                    except BaseException:
                        print(
                            '\n' +
                            caseName +
                            'already exist. Be careful or I\'ll destroy your data' +
                            '\n')
                        i += 1
                        break
                print('toto')
                
                #loading sim files
                dire=SolutionDirectory(caseName)
                dire.clearResults()
                        
                # writing CMC
                transprortPpties = ParsedParameterFile(
                    caseName + '/constant/transportProperties')
                transprortPpties['Ccmc'][2] = Ccmc
                transprortPpties.writeFile()

                # writing Ct BC
                solCt=SolutionFile(dire.initialDir(),"Ct")
                solCt.replaceBoundary("inlet","%f" %(Cbd))

                # writing initial concentrations in the BC<y<BD
                c0 = 'funkySetFields -case ' + \
                    os.path.join(studyPath, caseName) + ' -field Ct -expression "pos().y <= 0.00010447667906605678 ? ' + \
                    str(Cbc) + ' : ' + str(Cbd) + '"  -time 0'
                subprocess.call(c0, shell=True)
                print(c0)

                i += 1


if run:
    i = 0
    for caseName in caseList:
        if i == 2:
            break

        # parallel decomposition
        if nproc > 1:
            args = ["--method=scotch", "--clear", caseName, nproc]
            Decomposer(args=args)

        run = BasicRunner(
            argv=[
                solver,
                "-case",
                caseName],
            silent=True,
            noLog=False)
#        run.start()
        runCmd = 'pyFoamRunner.py advDiffMicellesNoFlow -case '+caseName+' > /dev/null 2>&1 &'
        subprocess.call(runCmd, shell=True)
        i += 1
