"""
Region Growing Segmentation
===========================

Thresholding is the most basic form of segmentation. The first step of
improvement upon the naive thresholding is a class of algorithms called
region growing.

The common theme in this class of algorithms is that a voxel's
neighbor is considered to be in the same class if its intensities are
similar to the current voxel. The definition of similar is what varies.
Initial set of voxel are called seed points. These initial seed points are
usually manually selected.

We illustrate the use of three variants of this family of algorithms:

- `ConnectedThreshold <http://www.itk.org/Doxygen/html/classitk_1_1ConnectedThresholdImageFilter.html>`_
- `ConfidenceConnected <http://www.itk.org/Doxygen/html/classitk_1_1ConfidenceConnectedImageFilter.html>`_
- `VectorConfidenceConnected <http://www.itk.org/Doxygen/html/classitk_1_1VectorConfidenceConnectedImageFilter.html>`_

We will illustrate the usage of these three filters using a cranial MRI
scan (T1 and T2) and attempt to segment one of the ventricles.
"""
# License: CC-BY
# sphinx_gallery_thumbnail_number = 4


from read_click import getQ
import numpy as np
import glob
from myshow import scrollshow
import SimpleITK as sitk
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

r = 3  # scaling factor
multi = 7.5  # multiplicator for region growing
im = "/home/florian/liverSim/images/PCMRI/De lima Mendes/irm flux preop/QRURUMC4/KPBA3L5B/I2000001"
imfolder = '/home/florian/liverSim/images/PCMRI/De lima Mendes/irm flux preop/QRURUMC4/SCZ2RGG5/'
imlist = glob.glob(imfolder + '*')
imlist.sort()
# get info from 1st image for scrolling display
img = sitk.ReadImage(imlist[0])
nda = sitk.GetArrayFromImage(img)
size = img.GetSize()
'''
WARING
a VERSION file is supposed to be present in the folder and thus rejected
remove the -1 in the last direction of scrollArray and vesselArray if not
'''
scrollArray = np.empty([size[1], size[0], len(imlist) - 1])
vesselArray = np.empty([size[1] * r, size[0] * r, len(imlist) - 1])

print scrollArray.shape
k = 0
for i in imlist:
    try:
        img = sitk.ReadImage(i)
        nda = sitk.GetArrayFromImage(img)
        scrollArray[:, :, k] = nda[0, :, :]
    except RuntimeError:
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
for i in imlist:
    try:
        img = sitk.ReadImage(i)
        img = sitk.ReadImage(i)
        img = sitk.Expand(img, [r, r, 1] * 3, sitk.sitkLinear)  # resampling with same dx dy as for getQ function
        nda = sitk.GetArrayFromImage(img)
        vesselArray[:, :, k] = nda[0, :, :] * segArray
        q = np.append(q, (np.sum(vesselArray[:, :, k])))
    except RuntimeError:
        print i
    k += 1

scrollshow(vesselArray)
x = np.linspace(0, 1, num=q.shape[0], endpoint=True)
f2 = interp1d(x, q, kind='linear')
xnew = np.linspace(0, 1, num=q.shape[0] * 2, endpoint=True)
plt.plot(x, q, 'o', xnew, f2(xnew), '--')
plt.show()
