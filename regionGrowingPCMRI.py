import os
from read_click import getQ
import numpy as np
import glob
from myshow import scrollshow
import SimpleITK as sitk
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter
import seaborn as sns

# source for profiles doi/10.1111/echo.12994/full
r = 3  # scaling factor
multi = 7.5  # multiplicator for region growing

extract = 1  # do not extract data from image but load npy array

if extract:
    # im = "/home/florian/liverSim/images/PCMRI/De lima Mendes/irm flux preop/QRURUMC4/KPBA3L5B/I2000001"
    imfolder = '/home/florian/liverSim/images/PCMRI/De lima Mendes/irm flux preop/QRURUMC4/SCZ2RGG5/'
    imlist = glob.glob(imfolder + '*')
    imlist.sort()
    for i in imlist:
        if os.path.split(i)[1] == 'VERSION':
            imlist.remove(i)

    # get info from 1st image for scrolling display
    img = sitk.ReadImage(imlist[0])
    nda = sitk.GetArrayFromImage(img)
    size = img.GetSize()
    rescaleIntercept, rescaleSlope = img.GetMetaData('0028|1052'), img.GetMetaData('0028|1053')
    print rescaleIntercept, rescaleSlope
    '''
    WARING
    a VERSION file is supposed to be present in the folder and thus rejected
    remove the -1 in the last direction of scrollArray and vesselArray if not
    '''
    scrollArray = np.empty([size[1], size[0], len(imlist)])
    vesselArray = np.empty([size[1] * r, size[0] * r, len(imlist)])

    print scrollArray.shape
    k = 0
    for i in imlist:
        try:
            img = sitk.ReadImage(i)
            nda = sitk.GetArrayFromImage(img)
            scrollArray[:, :, k] = nda[0, :, :]
        except RuntimeError:
            print 'ERROR-ERROR-ERROR-ERROR-ERROR-ERROR'
            print i
        k += 1
    scrollshow(scrollArray)

    print 'SHOW ME YOUR BEST ANGLE: '
    slice = input()
    try:
        val = int(slice)
    except ValueError:
        print("That's not an int!")

    # slice = 14
    segArray = getQ(imlist[slice], r, multi)

    k = 0
    q = np.empty([0])  # flow rate array
    uavg = np.empty([0])  # avg veloc array
    for i in imlist:
        try:
            img = sitk.ReadImage(i)
            img = sitk.ReadImage(i)
            img = sitk.Expand(img, [r, r, 1] * 3, sitk.sitkLinear)  # resampling with same dx dy as for getQ function
            nda = sitk.GetArrayFromImage(img)
            vesselArray[:, :, k] = nda[0, :, :] * segArray  # get only the ROI
            vesselArray[:, :, k] = vesselArray[:, :, k] * int(rescaleSlope) + int(rescaleIntercept)
            q = np.append(q, (np.sum(vesselArray[:, :, k])))
            uavg = np.append(uavg, (np.mean(vesselArray[:, :, k])))

        except RuntimeError:
            print i
        k += 1

    scrollshow(vesselArray)
else:
    uavg = np.load('veloc.npy')

CP = 1  # heart period 1s
k = 8
RP = k * CP  # respiratory period 8s

np.save('veloc', uavg)

# CORRECTION POUR CE CAS UNIQUEMENT : SLIDE #1 = pourrite
uavg[0] = 0.5 * (uavg[1] + uavg[-1])

sns.set()
sns.set_style("whitegrid")
sns.despine(left=True)


def smooth(Y):
    plotvar = np.append(np.append(Y, Y), Y)
    x = np.linspace(0, 3 * CP, num=plotvar.shape[0], endpoint=True)
    y3 = savgol_filter(plotvar, 5, 3)
    f3 = interp1d(x, y3, kind='quadratic')
    xnew = np.linspace(0, 3 * CP, num=100, endpoint=True)
    plt.plot(x, plotvar, 'o', xnew, f3(xnew), '--')
    return f3


vsmooth = smooth(uavg)
print vsmooth

plt.show()
