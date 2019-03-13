import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy import fftpack, signal
from scipy.interpolate import UnivariateSpline
import seaborn as sns
import pandas as pd
#import vapeplot
#from vapeplot import *

# from icecream import ic
from sklearn import preprocessing

'''
creates Q profile from 
Spectral Doppler of the Hepatic Veins in Noncardiac Diseases: 
What the Echocardiographer Should Know
'''

# plt.xkcd()
qvc_article=np.array([-0.547945205479451,3.83561643835617,9.31506849315069,14.7945205479452,21.3698630136986,26.3013698630137,31.2328767123288,35.0684931506849,31.7808219178082,28.4931506849315,23.013698630137,18.6301369863014,15.3424657534247,12.6027397260274,12.0547945205479,13.6986301369863,17.5342465753425,20.2739726027397,21.3698630136986,19.1780821917808,16.986301369863,15.3424657534247,13.6986301369863,10.958904109589,9.31506849315069,6.02739726027397,1.0958904109589,-1.0958904109589,-4.38356164383562,-7.67123287671232,-4.93150684931507,-2.73972602739725,0])
qvc_article_pd = pd.DataFrame(qvc_article)
def shifting(a, b):
    A = fftpack.fft(a)
    B = fftpack.fft(b)
    Ar = A.conjugate()
    Br = B.conjugate()
    AB = np.argmax(np.abs(fftpack.ifft(Ar * B)))
    BA = np.argmax(np.abs(fftpack.ifft(A * Br)))
    # ic(np.argmax(signal.correlate(a, b)))
    # ic(np.argmax(signal.correlate(b, a)))
    # plt.plot(np.abs(fftpack.ifft(Ar * B)), label="a")
    # plt.plot(np.abs(fftpack.ifft(A * Br)), label="b")

    return AB, BA


def csvreader(infile):
    toto = []
    with open(infile, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            toto.append(row)

    return np.array(toto).astype(float)


def smoothie(Y, l=1, curveName="toto"):
    k = 1
    plotvar = Y
    plotvar[0, 0] = 0
    plotvar[-1, 0] = 1
    plotvar[:, 0] = plotvar[:, 0] * k
    plot2 = np.array([plotvar[:, 0] + 1 * k, plotvar[:, 1]])[:, 1:]
    plot3 = np.array([plotvar[:, 0] + 2 * k, plotvar[:, 1]])[:, 1:]
    plot4 = np.array([plotvar[:, 0] + 3 * k, plotvar[:, 1]])[:, 1:]
    plotvar = np.append(plotvar, plot2.T, axis=0)
    plotvar = np.append(plotvar, plot3.T, axis=0)
    plotvar = np.append(plotvar, plot4.T, axis=0)

    f3 = interp1d(plotvar[:, 0], plotvar[:, 1], kind='cubic')
    xnew = np.linspace(0, 4 * k * CP, num=4 * k * 100, endpoint=True)
    ynew = f3(xnew)
    yhat = signal.savgol_filter(ynew, 15, 3)
    yhat = signal.savgol_filter(yhat, 5, 3)
    yhat = np.array([np.linspace(0, k * CP, num=k * 100, endpoint=True), yhat[1 * k * 100:2 * k * 100]])
    yhat = yhat.T
    yhat = np.tile(yhat, (4, 1))
    yhat[:, 0] = np.linspace(0, 4 * k * CP, num=4 * k * 100, endpoint=True)
    print('RI = ', (np.max(yhat[:,1])-np.min(yhat[:,1]))/np.max(yhat[:,1]))
    if l == 4:
        yhat = yhat[:100, :]
        yhat[:, 0] *= l
    if curveName == 'respiration profile':
        plt.plot(yhat[:, 0], yhat[:, 1], '.', label=curveName)
    else:
        plt.plot(yhat[:, 0], yhat[:, 1], '-', label=curveName)

    return yhat


CP = 1  # heart period 1s
k = 4
RP = k * CP  # respiratory period 8s

try:
    toto = np.load('/home/florian/codes/liverSim/dataSource.npy')
    rawRespi, rawQRespi, rawQ3, rawQ4,rawQarticle = toto
    print(('read {}'.format('/home/florian/codes/liverSim/dataSource.npy')))
except:
    rawRespi = csvreader('/home/florian/codes/liverSim/respiration.csv')
    rawQRespi = csvreader('/home/florian/codes/liverSim/HV_echo_flow-respi.csv')
    rawQ3 = csvreader('/home/florian/codes/liverSim/HV_echo_flow3.csv')
    rawQ4 = csvreader('/home/florian/codes/liverSim/HV_echo_flow4.csv')
    rawQarticle = csvreader('/home/florian/codes/liverSim/HV_tri_article.csv')
    allArr = np.array([rawRespi, rawQRespi, rawQ3, rawQ4])
    np.save('/home/florian/codes/liverSim/dataSource.npy', allArr)

qmri = np.load('/home/florian/codes/liverSim/q_vc_MRI.npy')
xmri = np.linspace(0, 1, 40, endpoint=True)
qmri = np.array([xmri, qmri]).T
print(qmri[0], type(qmri))
print('totototo')
sns.set()
sns.set_style('white')
sns.set_context('paper')
#vapeplot.set_palette('vaporwave')
#q4 = smoothie(rawQ4 * (-1), 1, 'U 4 phases')
#q3 = smoothie(rawQ3 * (-1), 1, 'U 3 phases')
#rawQarticle[:,1] *= 0.5
qarticle = smoothie(rawQarticle,1, 'u article')
#qrespi = smoothie(rawQRespi * (-1), 4, 'U w/ respiration')
#respi = smoothie(rawRespi, 4, 'respiration profile')

plt.ylabel('Velocity (m/s)')
plt.xlabel('Time (s)')
# print(qmri, qmri.shape)
# plt.plot(qmri[:,0],qmri[:,1], '-', label=' Q mri')

# qmri = smoothie(qmri, 1, 'Q vc mri')

# plt.plot(qmri[:,0],qmri[:,1], '-', label=' Q mri')
# plt.show()

# normalization w/ respect to q3
minref = np.min(qmri[:, 1])
maxref = np.max(qmri[:, 1])
# qmri[:, 1] = (qmri[:, 1] - minref) / (maxref - minref) * (np.max(q3[:, 1]) - np.min(q3[:, 1])) + np.min(q3[:, 1])

# # shifting qmri to align time with ref Q3
# AA, BB = shifting(q4, q3)
# ic(AA, BB)

# plt.legend()
plt.axhline(y=0, color='k')

# plt.show()
# sp = np.fft.fft(q3[:, 1])
# freq = np.fft.fftfreq(q3.shape[0], d=0.04)
# plt.plot(freq, sp.real, '-', label='real')
# plt.plot(freq, sp.imag, '-', label='img')
#
# sp = np.fft.fft(qmri[:, 1])
# freq = np.fft.fftfreq(qmri.shape[0], d=0.04)
# plt.plot(freq, sp.real, '-', label='real')
# plt.plot(freq, sp.imag, '-', label='img')
#
# plt.show()
# shifting qmri to align time with ref Q3
# AA, BB = shifting(qmri[:, 1], q3[:, 1])
# ic(AA, BB)
# plt.plot(q3[:, 0, ], q3[:, 1], '-', label=' q3')
# plt.plot(q4[:, 0, ], q4[:, 1], '-', label=' q4')
# plt.plot(qrespi[:, 0, ], qrespi[:, 1], '-', label=' q_respi')
# plt.plot(respi[:, 0, ], respi[:, 1], '-', label=' respi profile')
# plt.plot(qmri[:, 0], qmri[:, 1], '-', label=' Q mri')
# qmriTemp = qmri
# ic(qmriTemp[:BB, 1].shape)
# ic(qmriTemp[-BB:, 1].shape)
# ic(qmriTemp[BB:, 1].shape)
# ic(qmriTemp[:-BB, 1].shape)
# qmriTemp[:BB, 1] = qmri[-BB:, 1]
# qmriTemp[BB:, 1] = qmri[:-BB, 1]
# qmri = qmriTemp

# qmri[:, 0] -= BB / 400.
# plt.plot(qmri[:, 0], qmri[:, 1], '-', label=' Q mri  ')
# plt.plot(qmriTemp[:, 0], qmriTemp[:, 1], '-', label=' Q mri temp ')

plt.legend()
plt.savefig('veloc_HV_Fadeletal.png')
plt.show()
