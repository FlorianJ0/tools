#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 11:42:08 2018

@author: florian
"""
from icecream import ic
import numpy as np
import pint
import vapeplot
from vapeplot import palette
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

import seaborn as sns


ureg = pint.UnitRegistry()
ureg.auto_reduce_dimensions = True
Q_ = ureg.Quantity
pal = sns.blend_palette(vapeplot.palette("vaporwave"))

# radius of a 98A^2 surface "sphere"
# https://pubchem.ncbi.nlm.nih.gov/compound/439520#section=Top
r = (98e-20 / (4 * 3.14))**(1 / 2) * ureg.meter

k = 1.38e-23 * ureg.joule / ureg.K
mu = 0.001 * ureg.pascal * ureg.second
T = 320 * ureg.K

# data Lanzini, Bile 2003
r_BS_CH = 1e-9 * ureg.meter
r_BS_L_CH = 2.5e-9 * ureg.meter
r_BS_L_CH_vesicle = 35e-9 * ureg.meter


def Diff(r):
    '''
    prints the diffusion coeff given a radius, computed from the Stokes-Einstein law
    '''

#    ic(1*(k*T)/(6*3.14*r*mu),'m2 s-1')
    d = (k * T) / (6 * 3.14 * r * mu)
    ic(d)
    return


def ray(D):
    '''
    prints the radius given a diff coeff, computed from the Stokes-Einstein law
    '''

    radius = (k * T) / (D * 6 * 3.14 * mu)
    ic(radius)
    return

Diff(r_BS_CH)
#ray(300e-12 * ureg.me1r **2 / ureg.second)

# diffusion model from cussler


Dm = 3e-12 * ureg.meter * ureg.meter / ureg.second
D1 = 3e-10 * ureg.meter * ureg.meter / ureg.second
Ccmc = 25e-3 * ureg.mole * ureg.meter ** -3
K = 4.32e-2 * ureg.mole ** -9 * ureg.meter ** 27
#Ct = (np.logspace(1e-9, 2, 100, endpoint=True) - 1) * ureg.mole * ureg.meter ** -3
Ct = np.linspace(1e-3, 1, num=50) * ureg.mole * ureg.meter ** -3
n = 10
eps = 1* ureg.mole * ureg.meter ** -3
'''
basic test
'''

def pos(x):
    if x>0:
        x = 1
    else:
        x = 0
    return x

def pos0(x):
    if x>=0:
        x = 1
    else:
        x = 0
    return x

def neg(x):
    if x<0:
        x = 1
    else:
        x = 0
    return x

def neg0(x):
    if x<=0:
        x = 1
    else:
        x = 0
    return x



def diffeffective(Dm, D1, Ccmc, K, Ct, n, mag=False):
    Deff = 0
    D = []
    for i in range(Ct.shape[0]):
        try:
            CCcmc = Ct[i].magnitude -Ccmc.magnitude
        except:
            CCcmc = Ct[i] -Ccmc
        ptit =1
        DDt =pos(CCcmc)*(Dm+(D1/n) *np.power(1/(n*K),(1/n))*np.power(1/(pos(CCcmc)*CCcmc+neg0(CCcmc)*ptit),(1-(1/n))))+neg0(CCcmc)*D1
        try:
            Dt = pos0(D1.magnitude - DDt.magnitude) * DDt + neg(D1.magnitude-DDt.magnitude) * D1
        except:
            Dt = pos0(D1 - DDt) * DDt + neg(D1-DDt) * D1
        print(Ct[i] ,Dt)
        
        
#        CCcmc = Ct[i]-Ccmc
#        h=np.heaviside(CCcmc, 0.5)
#        Deff=h*(Dm+(D1/n)*(1/(n*K))**(1/n)*(1/(h*(Ct[i]-Ccmc)+(1-h)*eps))**(1-1/n))+(1-h)*D1
#        if Deff > D1:
#            Deff=D1
#        print(1 / (Ct[i] - Ccmc+eps)**(1 - 1 / n),Deff)
        if mag:
            D.append(Dt)
        else:
            D.append(Dt.magnitude)

#        if CCcmc.magnitude > 0:
#            Deff = Dm + (D1 / n) * (1 / (n * K))**(1 / n) * (1 / (Ct[i] - Ccmc))**(1 - 1 / n)
#        else:
#            Deff = D1

#        if Ct[i] <= Ccmc:
#            Deff = D1#Dm + (D1 / n) * (1 / (n * K))**(1 / n) * \
#                #(1 / (Ct[i] - Ccmc))**(1 - 1 / n)
#        else:
#            Deff = Dm + (D1 / n) * (1 / (n * K))**(1 / n) * \
#                (1 / (Ct[i] - Ccmc))**(1 - 1 / n)
#            if Deff > D1:
#                Deff = D1

    return D


def diffeffectiveTurq(Dm, D1, Ccmc, K, Ct, n, mag=False):
    Deff = 0
    D = []
    for i in range(Ct.shape[0]):
        if Ct[i] <= Ccmc:
            Deff = D1
        else:
            Deff = Dm + (D1 / n) * (1 / (n * K))**(1 / n) * \
                (1 / (Ct[i] - Ccmc))**(1 - 1 / n)
            if Deff > D1:
                Deff = D1
        if mag:
            D.append(Deff)
        else:
            D.append(Deff.magnitude)

    return D


Diff = diffeffective(Dm, D1, Ccmc, K, Ct, n,0)
if 1 == 0:
    df = pd.DataFrame(list(zip(Ct.magnitude, Diff)), columns=['Ct', 'Deff'])
    sns.set()
    sns.set_style("whitegrid")
    sns.lineplot(x='Ct', y='Deff', data=df, palette=pal)
    plt.axvline(x=Ccmc.magnitude, color='black')
    plt.show()
    plt.savefig('diffFunctionCt.jpeg')


'''
Ccmc comparison
'''


def compareccmc(ccmclist):
    dfccmc = pd.DataFrame(Ct.magnitude, columns=['Ct'])
    for i in ccmclist:
        d = diffeffective(Dm, D1, i, K, Ct, n)
        colname = 'Ccmc=' + str(i)
        dfccmc[colname] = pd.Series(d, index=dfccmc.index)
    return(dfccmc)

if 1 == 0:

    ccmclist = [0.5 * Ccmc, Ccmc, 2 * Ccmc]
    Difflist = compareccmc(ccmclist)

    sns.set()
    sns.set_style("whitegrid")
    sns.lineplot(x='Ct', y='Ccmc=5.0 mole / meter ** 3', data=Difflist)
    sns.lineplot(x='Ct', y='Ccmc=10.0 mole / meter ** 3', data=Difflist)
    sns.lineplot(x='Ct', y='Ccmc=20.0 mole / meter ** 3', data=Difflist)

    plt.show()

'''
n comparison
'''


def comparen(nlist):
    dfn = pd.DataFrame(Ct.magnitude, columns=['Ct'])
    for i in nlist:
        d = diffeffective(
            Dm.magnitude,
            D1.magnitude,
            Ccmc.magnitude,
            K.magnitude,
            Ct.magnitude,
            i,
            0)
        colname = 'n=' + str(i)
        dfn[colname] = pd.Series(d, index=dfn.index)
    return(dfn)



if 1 == 1:
    nlist = list(range(4, 100, 20, ))
    Difflist = comparen(nlist)

    sns.set()
    sns.set_style("whitegrid")
    for i in nlist:
        sns.lineplot(x='Ct', y='n=' + str(i), data=Difflist)
        plt.legend = str(i)

    plt.show()

'''
k comparison
'''


def comparek(klist):
    dfk = pd.DataFrame(Ct.magnitude, columns=['Ct'])
    for i in klist:
        d = diffeffective(
            Dm.magnitude,
            D1.magnitude,
            Ccmc.magnitude,
            i,
            Ct.magnitude,
            n,
            True)
        colname = 'k=' + str(i)
        dfk[colname] = pd.Series(d, index=dfk.index)
    return(dfk)



if 1 == 0:
    klist = [K.magnitude / 100, K.magnitude, 100 * K.magnitude]
    Difflist = comparek(klist)

    sns.set()
    sns.set_style("whitegrid")
    for i in klist:
        sns.lineplot(x='Ct', y='k=' + str(i), data=Difflist)
        plt.legend = str(i)

    plt.show()
