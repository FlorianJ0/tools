    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 22:04:47 2018

@author: florian
"""

import pandas as pd
import numpy as np
import os
import sys
import subprocess
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

file_name = '{}_Ccmc{}_Cbd{}_Cbc{}'
df_list = []
i=0

if computeAVG:
    
for Ccmc in ccmcList:
    for Cbd in CbdList:
        for Cbc in CbcList:
            sed = "sed -i 's/t36.vtu/t39.vtu/g' "+runLAVD


for Ccmc in ccmcList:
    for Cbd in CbdList:
        for Cbc in CbcList:
            
            caseName = str(i) + '_Ccmc' + str(Ccmc) + '_Cbd' + \
                str(Cbd) + '_Cbc' + str(Cbc)
            caseName = caseName.replace(".", "")
            caseList.append(caseName)
            f = file_name.format(i, Ccmc, Cbd,Cbc)
            f = f.replace(".", "")
            f+='.csv'
            df_list.append(pd.read_csv(f))
            ic(f)
            i += 1

df = pd.concat(df_list)