import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter
from scipy.interpolate import UnivariateSpline
import seaborn as sns
import vapeplot
from icecream import ic

'''
creates Q profile from 
Spectral Doppler of the Hepatic Veins in Noncardiac Diseases: 
What the Echocardiographer Should Know
'''


def rfft_xcorr(x, y):
    M = len(x) + len(y) - 1
    N = 2 ** int(np.ceil(np.log2(M)))
    X = np.fft.rfft(x, N)
    Y = np.fft.rfft(y, N)
    cxy = np.fft.irfft(X * np.conj(Y))
    cxy = np.hstack((cxy[:len(x)], cxy[N - len(y) + 1:]))
    return cxy


def match(x, ref):
    cxy = rfft_xcorr(x, ref)
    index = np.argmax(cxy)
    if index < len(x):
        return index
    else:  # negative lag
        return index - len(cxy)


plt.xkcd()


def csvreader(infile):
    toto = []
    with open(infile, 'rb') as csvfile:
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
    yhat = savgol_filter(ynew, 15, 3)
    yhat = savgol_filter(yhat, 5, 3)
    yhat = np.array([np.linspace(0, k * CP, num=k * 100, endpoint=True), yhat[1 * k * 100:2 * k * 100]])
    yhat = yhat.T
    yhat = np.tile(yhat, (4, 1))
    yhat[:, 0] = np.linspace(0, 4 * k * CP, num=4 * k * 100, endpoint=True)
    if l == 4:
        yhat = yhat[:100, :]
        yhat[:, 0] *= l
    plt.plot(yhat[:, 0], yhat[:, 1], '-', label=curveName)
    return yhat


CP = 1  # heart period 1s
k = 4
RP = k * CP  # respiratory period 8s

try:
    toto = np.load('/home/florian/liverSim/dataSource.npy')
    rawRespi, rawQRespi, rawQ3, rawQ4 = toto
    print('read {}'.format('/home/florian/liverSim/dataSource.npy'))
except:
    rawRespi = csvreader('/home/florian/liverSim/respiration.csv')
    rawQRespi = csvreader('/home/florian/liverSim/HV_echo_flow-respi.csv')
    rawQ3 = csvreader('/home/florian/liverSim/HV_echo_flow3.csv')
    rawQ4 = csvreader('/home/florian/liverSim/HV_echo_flow4.csv')
    allArr = np.array([rawRespi, rawQRespi, rawQ3, rawQ4])
    np.save('/home/florian/liverSim/dataSource.npy', allArr)

qmri = np.load('/home/florian/liverSim/q_vc_MRI.npy')
xmri = np.linspace(0, 1, 25, endpoint=True)
qmri = np.array([xmri, qmri]).T
sns.set()
sns.set_style('white')
sns.set_context('paper')
vapeplot.set_palette('vaporwave')
q4 = smoothie(rawQ4 * (-1), 1, 'Q 4 phases')
q3 = smoothie(rawQ3 * (-1), 1, 'Q 3 phases')
respi = smoothie(rawRespi, 4, 'respiration profile')
qrespi = smoothie(rawQRespi * (-1), 4, 'Q w/ respiration')
qmri = smoothie(qmri, 1, 'Q vc mri')

plt.legend()
plt.axhline(y=0, color='k')

plt.show()
sp = np.fft.fft(q3[:, 1])
freq = np.fft.fftfreq(q3.shape[0], d=0.04)
plt.plot(freq, sp.real, '-', label='real')
plt.plot(freq, sp.imag, '-', label='img')

sp = np.fft.fft(qrespi[:, 1])
freq = np.fft.fftfreq(qrespi.shape[0], d=0.04)
plt.plot(freq, sp.real, '-', label='real')
plt.plot(freq, sp.imag, '-', label='img')

plt.show()
# plt.plot(q3[:,0],q3[:,1], '-', label=' w/o respi')
plt.plot(qmri[:, 0], qmri[:, 1], '-', label=' Q mri')
plt.legend()
# plt.savefig('qmri.png')
plt.show()
