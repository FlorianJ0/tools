import cv2
import numpy as np
import SimpleITK as sitk
from myshow import myshow, myshow3d

def getPos(img):
    def draw_circle(event, x, y, flags, param):
        global mouseX, mouseY
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(img, (x, y), 5, (255, 255, 255), 1)
            mouseX, mouseY = x, y

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)

    while 1:
        cv2.imshow('image', img)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:  # click on escape to escape, genius
            break
        elif k == ord('a'):  # click on 'a' to get value
            try:
                print(mouseX, mouseY)
            except NameError:
                print('click first dumbass')

    cv2.destroyAllWindows()
    return mouseX, mouseY, img[mouseX, mouseY]

def getQ(imageFile, r = 2, multi = 7.5):
    ##############################################################################
    # Load Images
    # -----------
    # r = 2 # resampling factor
    resSlope = 2 #from dcm file
    reIntercep = -4096 #from dcm file
    # u = slope * signal + intercept
    img_T1 = sitk.ReadImage(imageFile)
    img_T1 = sitk.Expand(img_T1, [r,r,1] * 3, sitk.sitkLinear)
    imArray = sitk.GetArrayFromImage(img_T1)
    imArray = imArray[0, :, :]
    # To visualize the labels image in RGB needs a image with 0-255 range
    img_T1_255 = sitk.Cast(sitk.RescaleIntensity(img_T1), sitk.sitkUInt8)


    ny, nx = img_T1_255.GetSize()[0], img_T1_255.GetSize()[1]
    imArray255 = sitk.GetArrayFromImage(img_T1_255)
    imArray255 = imArray255[0, :, :]
    print(imArray255.shape)
    imArray255 = imArray255.reshape((nx, ny))
    size = img_T1_255.GetSize()
    print('size = ', size)
    # myshow(img_T1_255, title='T1')  # , zslices=range(50, size[2] - 50, 20), title='T1')

    ##############################################################################
    # Seed selection
    # --------------
    print('getpos po ok')

    x, y, val = getPos(imArray255)
    print('getpos ok')
    seed = (x, y, 0)
    print('seed: ', seed)
    seg = sitk.Image(img_T1.GetSize(), sitk.sitkUInt8)
    seg.CopyInformation(img_T1)
    seg[seed] = 1

    seg = sitk.BinaryDilate(seg, 3)

    # myshow3d(sitk.LabelOverlay(img_T1_255, seg),
    #          xslices=range(img_T1.GetSize()[0], img_T1.GetSize()[1]), title="Initial Seed")

    ##############################################################################
    # ``ConfidenceConnected``
    # ^^^^^^^^^^^^^^^^^^^^^^^
    #
    #
    # Unlike in ``ConnectedThreshold``, you need not select the bounds in
    # ``ConfidenceConnected`` filter. Bounds are implicitly specified as
    # :math:`\mu\pm c\sigma`, where :math:`\mu` is the mean intensity of the seed
    # points, :math:`\sigma` their staimArray255rd deviation and :math:`c` a user specified
    # constant.
    #
    # This algorithm has some flexibility which you should familiarize yourself with:
    #
    # * The ``multiplier`` parameter is the constant :math:`c` from the formula above.
    # * You can specify a region around each seed point ``initialNeighborhoodRadius``
    #   from which the statistics are estimated, see what happens when you set it to zero.
    # * The ``numberOfIterations`` allows you to rerun the algorithm. In the first
    #   run the bounds are defined by the seed voxels you specified, in the
    #   following iterations :math:`\mu` and :math:`\sigma` are estimated from
    #   the segmented points and the region growing is updated accordingly.


    seg_conf = sitk.ConfidenceConnected(img_T1, seedList=[seed],
                                        numberOfIterations=1,
                                        multiplier=multi,
                                        initialNeighborhoodRadius=1,
                                        replaceValue=1)
    #
    # myshow3d(sitk.LabelOverlay(img_T1_255, seg_conf),
    #          xslices=range(img_T1.GetSize()[0], img_T1.GetSize()[1]), title="ConfidenceConnected")

    # Clean up, clean up
    # ------------------
    #
    # Use of low level segmentation algorithms such as region growing is often followed by a clean up step. In this step we fill holes and remove small connected components. Both of these operations are achieved by using binary morphological operations, opening (``BinaryMorphologicalOpening``) to remove small connected components and closing (``BinaryMorphologicalClosing``) to fill holes.
    #
    # SimpleITK supports several shapes for the structuring elements (kernels) including:
    #
    # - sitkAnnulus
    # - sitkBall
    # - sitkBox
    # - sitkCross
    #
    # The size of the kernel can be specified as a scalar (same for all dimensions) or as a vector of values, size per dimension.
    #
    # The following code illustrates the results of such a clean up, using
    # closing to remove holes in the original segmentation.


    vectorRadius = (2, 2, 1)
    kernel = sitk.sitkBall
    seg_clean = sitk.BinaryMorphologicalClosing(seg_conf,
                                                vectorRadius,
                                                kernel)

    myshow3d(sitk.LabelOverlay(img_T1_255, seg_clean), title="Cleaned up segmentation")

    # print seg_clean[234, 256,1]
    segArray = sitk.GetArrayFromImage(seg_clean)
    print(segArray.shape)
    segArray = segArray[0,:,:]
    segImArray = imArray[segArray>0]
    print(segImArray.shape, len(segImArray))
    # u = slope * signal + intercept
    sumPix = np.sum(segImArray)
    vag = np.mean(segImArray)
    print('Q =', sumPix, 'Vavg = ', vag)
    segImArrayPhysical = segImArray * resSlope + reIntercep #in physical units
    sumPix = np.sum(segImArrayPhysical)
    vag = np.mean(segImArrayPhysical)
    print('Q =', sumPix, 'Vavg = ', vag)

    return  segArray

if __name__ == "__main__":
    img = np.zeros((512, 512, 3), np.uint8)
    getPos(img)