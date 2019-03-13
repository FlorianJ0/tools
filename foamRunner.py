#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:50:26 2018

@author: florian
"""

import re,sys
 
from PyFoam.LogAnalysis.LogLineAnalyzer import LogLineAnalyzer
from PyFoam.LogAnalysis.BoundingLogAnalyzer import BoundingLogAnalyzer
from PyFoam.Execution.AnalyzedRunner import AnalyzedRunner
 
class CompactLineAnalyzer(LogLineAnalyzer):
    def __init__(self):
        LogLineAnalyzer.__init__(self)
 
        self.told=""
        self.exp=re.compile("^(.+):  Solving for (.+), Initial residual = (.+), Final residual = (.+), No Iterations (.+)$")
 
    def doAnalysis(self,line):
        m=self.exp.match(line)
        if m!=None:
            name=m.group(2)
            resid=m.group(3)
            time=self.getTime()
            if time!=self.told:
                self.told=time
                print("\n t = %6g : " % ( float(time) )),
            print(" %5s: %6e " % (name,float(resid))),
            sys.stdout.flush()
 
class CompactAnalyzer(BoundingLogAnalyzer):
    def __init__(self):
        BoundingLogAnalyzer.__init__(self)
        self.addAnalyzer("Compact",CompactLineAnalyzer())
 
    
    
solver="advDiffMicellesPimpleFoam"
case="BDCoHBC"
# 
#dire=SolutionDirectory(case,archive="InletVariation")
#dire.clearResults()
#dire.addBackup("PyFoamSolve.logfile")
#dire.addBackup("PyFoamSolve.analyzed")
#dire.addBackup("Pressure.analyzed")
#dire.addBackup("MassFlow.analyzed")

run=AnalyzedRunner(CompactAnalyzer(),silent=True)
run.start()