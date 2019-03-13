import os, sys
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
# profiles image names
r = 3  # scaling factor
multi = 7.5  # multiplicator for region growing

extract = 0  # do not extract data from image but load npy array
plot = 1
imagesSourcesFaivre = {"faivre_PV": '/home/florian/codes/liverSim/images/PCMRI/Faivre/irmflux/YAUSEQ0O/GCNUDSJY/',
                       "faivre_VCI": '/home/florian/codes/liverSim/images/PCMRI/Faivre/irmflux/YAUSEQ0O/4RCRHXM0/',
                       "faivre_VCI30": '/home/florian/codes/liverSim/images/PCMRI/Faivre/irmflux/YAUSEQ0O/OKTTPH2Q/',
                       "faivre_VCS": '/home/florian/codes/liverSim/images/PCMRI/Faivre/irmflux/YAUSEQ0O/4RVFT1PH/',
                       'faivre_A-ASC': '/home/florian/codes/liverSim/images/PCMRI/Faivre/irmflux/YAUSEQ0O/TS3F12CD/',
                       'faivre_A-DES': '/home/florian/codes/liverSim/images/PCMRI/Faivre/irmflux/YAUSEQ0O/TS3F12CD/'
                       }
imagesSourcesAGeorges = {
    'ageorges_PV': "/home/florian/codes/liverSim/images/PCMRI/ageorgesirmflux/0CU03R5Y/FXVBGII4/"
}

imagesSourcesDeLima = {
    'delima_A-DES': '/home/florian/codes/liverSim/images/PCMRI/De lima Mendes/irm flux preop/QRURUMC4/K1PPKOWE/',
    'delima_PV': '/home/florian/codes/liverSim/images/PCMRI/De lima Mendes/irm flux preop/QRURUMC4/GAMAJK0P/',
    'delima_VCI': '/home/florian/codes/liverSim/images/PCMRI/De lima Mendes/irm flux preop/QRURUMC4/S11ASJ0I/'
}

imagesSourcesLariou = {
    'lariou_PV': '/home/florian/codes/liverSim/images/PCMRI/Lariou/irmflux/ZZ4NH0B5/CP3YH44M/',
    'lariou_HA': '/home/florian/codes/liverSim/images/PCMRI/Lariou/irmflux/ZZ4NH0B5/JHEDZLGV/',
    'lariou_A-DES': '/home/florian/codes/liverSim/images/PCMRI/Lariou/irmflux/ZZ4NH0B5/5033WNWX/',
    'lariou_A-ASC': '/home/florian/codes/liverSim/images/PCMRI/Lariou/irmflux/ZZ4NH0B5/5033WNWX/',
    'lariou_VCI': '/home/florian/codes/liverSim/images/PCMRI/Lariou/irmflux/ZZ4NH0B5/FNVTGXHC/'
}

imagesSourcesBelmejdoub = {
    'Belmejdoub_PV': '/home/florian/codes/liverSim/images/PCMRI/Belmejdoub/IRMFLUX/SREUF1TI/1MO2CISA/',
    'Belmejdoub_A-ASC': '/home/florian/codes/liverSim/images/PCMRI/Belmejdoub/IRMFLUX/SREUF1TI/JQBQCBTL/',
    # 'Belmejdoub_A-DES60': '/home/florian/codes/liverSim/images/PCMRI/Belmejdoub/IRMFLUX/SREUF1TI/1ID4DCYF/',
    'Belmejdoub_VCI': '/home/florian/codes/liverSim/images/PCMRI/Belmejdoub/IRMFLUX/SREUF1TI/DTOHGWWT/',
    'Belmejdoub_VCI2': '/home/florian/codes/liverSim/images/PCMRI/Belmejdoub/IRMFLUX/SREUF1TI/SMRHXGRB/'
}

imagesSourcesSEBG = {
        'SEBG_PV':'',
        'SEBG_VCI':'/home/florian/codes/liverSim/images/PCMRI/Bauman/EAEWITP1/PEE3WTJX/', #vci amont
        'SEBG_VCII':' /home/florian/codes/liverSim/images/PCMRI/Bauman/EAEWITP1/ONGDXIJW/', #vci amont 2
        'SEBG_VCI2':'/home/florian/codes/liverSim/images/PCMRI/Bauman/EAEWITP1/ZGERO2IS/',#vci aval sushep
        'SEBG_HV':'/home/florian/codes/liverSim/images/PCMRI/Bauman/EAEWITP1/OAWHOEGY/',
        'SEBG_A-DES':'/home/florian/codes/liverSim/images/PCMRI/Bauman/EAEWITP1/FRR15TAX/'
        }

fname = 'SEBG_VCI'
imfolder = imagesSourcesSEBG[fname]

print('Current evaluation is {}'.format(fname))


col = {'PV': 'burnt sienna', 'VCS': 'pea green', 'A-DES': 'dark teal', 'A-DES60': 'dark teal', 'A-ASC': 'cerulean',
       'VCI': 'goldenrod',
       'VCI30': 'bluish purple', 'VCI2': 'bluish purple', 'HV': 'charcoal', 'HA': 'coral'}


def BSA(W, H, S):
    # Schlich formula
    H *= 100  # H in m
    # female
    if S:
        bsa = 0.000975482 * W ** 0.46 * H ** 1.08
    # male
    else:
        bsa = 0.000579479 * W ** 0.38 * H ** 1.24
    return bsa


def smooth(Y, color, leg, CP=1):
    plotvar = np.append(np.append(Y, Y), Y)
    x = np.linspace(0, 3 * CP, num=plotvar.shape[0], endpoint=True)
    print('heart period: ', CP)
    y3 = savgol_filter(plotvar, 5, 3)
    f3 = interp1d(x, y3, kind='cubic')
    xnew = np.linspace(0, 3 * CP, num=149, endpoint=True)
    ynew = f3(xnew)
    # plt.plot(x, plotvar, 'o', xnew, f3(xnew), '--')
    if leg[:2] == 'HV':
        plt.plot(xnew[0:49], ynew[50:99], '--', color='xkcd:' + color, label=leg)
    else:
        plt.plot(xnew[0:49], ynew[50:99], '-', color='xkcd:' + color, label=leg)
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Volumetric flow rate (L/min)')
    # plt.text(2, np.max(f3(xnew)[50:83]) + 2, r'Q average {0:0.2f} L/min'.format(60000 * np.mean(q)), fontsize=10)
    return f3


def computeFlowRate(veins, HR, ptName):
    qmean = []
    umean = []
    umax = []
    dx = 1.0625 * 1e-3 / r
    ds = dx * dx
    veldict = {}
    Qdict = {}

    for v in veins:
        print('\n', pt + '_' + v + '.npy loaded')
        veldict[v] = np.load(pt + '_' + v + '.npy')
        if np.mean(veldict[v]) < 0:
            veldict[v] *= -1

        Qdict[v] = 60000 * ds * np.sum(veldict[v] / 100, axis=1)
        qmean_corr = np.mean(ds * np.sum(veldict[v] / 100, axis=1))
        umean.append(np.mean(veldict[v]))
        umax.append(np.max(veldict[v]))
        qmean.append(np.abs(qmean_corr * 60000))
        print('Q = {} L/min'.format(np.abs(qmean_corr * 60000)))
        # if v not in []:#['A-ASC', 'A-DES']:
        smooth(60000 * ds * np.sum(veldict[v] / 100, axis=1), col[v],
               v + (r' : $\bar Q$ = {0:0.2f} L/min'.format(np.mean(Qdict[v]))), HR)
    if 'VCI' in veins and 'PV' in veins:
        veldict['HV'] = veldict['VCI'] * 1.2 * np.mean(veldict['PV']) / np.mean(veldict['VCI'])
        Qdict['HV'] = Qdict['VCI'] * 1.2 * np.mean(Qdict['PV']) / np.mean(Qdict['VCI'])
        smooth(Qdict['HV'], col['HV'],
               'HV' + (r' : $\bar Q$ = {0:0.2f} L/min'.format(
                       np.mean(Qdict['HV'])
               )), HR)
        umean.append(np.mean(veldict['HV']))
        umax.append(np.max(veldict['HV']))
        qmean.append(np.abs(np.mean(Qdict['HV'])))
        print('QPV = {} L/min'.format(np.mean(np.abs(qmean * 60000))))
        print('QPV = {} L/min'.format(np.mean(Qdict['HV'])))
    if ptName == 'lariou':
        print(Qdict['VCI'])
        print(Qdict['HV'])

    plt.title(ptName)
    # plt.savefig(ptName + '_Qprofiles.png')
    plt.show()
    return umean, umax, qmean


if extract:
    series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(imfolder)
    if not series_IDs:
        print("ERROR: given directory \"" + imfolder + "\" does not contain a DICOM series.")
        sys.exit(1)
    series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(imfolder, series_IDs[0])

    image_reader = sitk.ImageFileReader()
    image_reader.LoadPrivateTagsOn()

    img = sitk.ReadImage(series_file_names[0])

    time_list = []
    for i in series_file_names:
        img = sitk.ReadImage(i)
        time_list.append(int(img.GetMetaData('0008|0018').split(".")[-1]))

    sort_array = np.argsort(time_list)
    series_file_names = np.array(series_file_names)
    sorted_file_names = series_file_names[sort_array]

    nda = sitk.GetArrayFromImage(img)
    size = img.GetSize()
    rescaleIntercept, rescaleSlope = img.GetMetaData('0028|1052'), img.GetMetaData('0028|1053')
    spacing = img.GetMetaData('0028|0030')
    seqName = img.GetMetaData('0018|0024')
    venc = int(seqName.split('in')[0][-3:])
    print("venc = {} cm/s".format(venc))
    imname = 'flow_faible_AASC.png'

    dx, dy = 1.0625 * 1e-3 / r, 1.0625 * 1e-3 / r  # convert all to m
    pixArea = dx * dy

    scrollArray = np.empty([size[1], size[0], len(sorted_file_names)])
    vesselArray = np.empty([size[1] * r, size[0] * r, len(sorted_file_names)])

    k = 0
    for i in sorted_file_names:
        try:
            img = sitk.ReadImage(i)
            nda = sitk.GetArrayFromImage(img)
            scrollArray[:, :, k] = nda[0, :, :]
        except RuntimeError:
            print('ERROR-ERROR-ERROR-ERROR-ERROR-ERROR')
            print(i)
        k += 1
    scrollshow(scrollArray)

    print('SHOW ME YOUR BEST ANGLE: ')
    slice = input()
    slice = int(slice)
    try:
        val = int(slice)
    except ValueError:
        print("That's not an int!")

    # slice = 14
    segparam = 6
    segok = False
    seginput = ''
    valinput = 0
    while not segok:
        segArray = getQ(sorted_file_names[slice], r, segparam)
        seginput = input('Is segmentation ok ? [y]/n\n')
        if seginput == 'y':
            break
        else:
            valinput = float(
                    input('Increase or decrease segmentation param:\n Current value is ' + str(segparam) + '\n'))
            segparam += valinput

    print('getQ ok')

    k = 0
    q = np.empty([0])
    uavg = np.empty([0])
    umax = np.empty([0])
    velValues = []

    for i in sorted_file_names:
        try:
            img = sitk.ReadImage(i)
            img = sitk.ReadImage(i)
            img = sitk.Expand(img, [r, r, 1] * 3, sitk.sitkLinear)  # resampling with same dx dy as for getQ function
            nda = sitk.GetArrayFromImage(img)  # in mm/s
            # vesselArray[:, :, k] = nda[0, :, :]  # [segArray]  # get only the ROI
            pixValue = nda[0, :, :]
            pixValue = pixValue[segArray == True]
            pixValue = pixValue / 4096 * venc
            vesselSize = len(pixValue)
            # pixArea /= r ^ 2

            # q = sum of U over all elements * dx * dy
            qslice = np.sum(pixValue) / 100 * pixArea  # cm/s to m/s
            q = np.append(q, qslice)
            uavg = np.append(uavg, np.mean(pixValue))
            umax = np.append(umax, np.max(pixValue))
            velValues.append(pixValue)

        except RuntimeError:
            print(i)
        k += 1
    np.save(fname, velValues)
    plt.plot(uavg)
    plt.show()
    print("vessel surface area (cm2)", vesselSize * pixArea * 100 * 100)
    print("average flow rate", np.mean(q), "m3/s", np.mean(q) * 60000, "L/min")
    print("average blood velocity", np.mean(uavg), "cm/s")
    print("max blood velocity", np.max(uavg), "cm/s")
    print("min blood velocity", np.min(uavg), "cm/s")

    CP = 1  # heart period 1s
    k = 8
    RP = k * CP  # respiratory period 8s

    # np.save('veloc', uavg)

    # CORRECTION POUR CE CAS UNIQUEMENT : SLIDE #1 = pourrite
    # uavg[0] = 0.5 * (uavg[1] + uavg[-1])

    sns.set()
    sns.set_style("whitegrid")
    sns.despine(left=True)

    smooth(uavg, 'teal', 'Umean')
    smooth(umax, 'brick red', 'Umax')
    # np.save('/home/florian/codes/liverSim/q_ivc_MRI', uavg)
    # print(vsmooth)
    # plt.savefig("lariouavci.png")
    plt.show()

if plot:
    print('it\'s plotting time')
    results = {}
    weight = {}
    height = {}
    HR = {}
    sex = {}  # sex=0 > male
    BSAdict = {}
    pt = "faivre"
    weight['faivre'] = 62
    height['faivre'] = 1.67
    HR['faivre'] = 73.68
    dx = 1.0625
    sex['faivre'] = 1
    bsa = BSA(weight['faivre'], height['faivre'], sex['faivre'])
    BSAdict['faivre'] = bsa
    print("BSA = {0:0.4f} m2     ".format(bsa))
    veins = ['PV', 'VCS', 'A-DES', 'A-ASC', 'VCI', 'VCI30']
    umean, umax, qmean = computeFlowRate(veins, 60 / HR[pt], pt)
    results[pt] = [veins, umean, umax, qmean]

    pt = "lariou"
    weight['lariou'] = 65
    height['lariou'] = 1.60
    HR['lariou'] = 64.2
    dx = 1.0625
    sex['lariou'] = 1
    bsa = BSA(weight['lariou'], height['lariou'], sex['lariou'])
    BSAdict['lariou'] = bsa

    print("BSA = {0:0.4f} m²".format(bsa))
    veins = ['PV', 'HA', 'A-DES', 'A-ASC', 'VCI']
    umean, umax, qmean = computeFlowRate(veins, 60 / HR[pt], pt)
    results[pt] = [veins, umean, umax, qmean]




    pt = "SEBG"
    weight['SEBG'] = 73
    height['SEBG'] = 1.75
    HR['SEBG'] = 77.16
    dx = 1.0625
    sex['SEBG'] = 0
    bsa = BSA(weight['SEBG'], height['SEBG'], sex['SEBG'])
    BSAdict['SEBG'] = bsa

    print("BSA = {0:0.4f} m²".format(bsa))
    veins = ['VCI', 'VCI2','A-DES', 'HV']
    umean, umax, qmean = computeFlowRate(veins, 60 / HR[pt], pt)
    results[pt] = [veins, umean, umax, qmean]





    pt = "ageorges"
    weight['ageorges'] = 73
    height['ageorges'] = 1.75
    HR['ageorges'] = 77.16
    dx = 1.0625
    sex['ageorges'] = 0
    bsa = BSA(weight['ageorges'], height['ageorges'], sex['ageorges'])
    BSAdict['ageorges'] = bsa

    print("BSA = {0:0.4f} m²".format(bsa))
    veins = ['PV']
    umean, umax, qmean = computeFlowRate(veins, 60 / HR[pt], pt)
    results[pt] = [veins, umean, umax, qmean]

    pt = "delima"
    weight['delima'] = 84
    height['delima'] = 1.76
    HR['delima'] = 61.44
    dx = 1.0625
    sex['delima'] = 0
    bsa = BSA(weight['delima'], height['delima'], sex['delima'])
    BSAdict['delima'] = bsa

    print("BSA = {0:0.4f} m²".format(bsa))
    veins = ['PV', 'A-DES', 'VCI']
    umean, umax, qmean = computeFlowRate(veins, 60 / HR[pt], pt)
    results[pt] = [veins, umean, umax, qmean]
    for k in results.keys():
        print(k, BSAdict[k])
        # results[k][1:] = results[k][1:][-1]/BSAdict[k]
        results[k][1:][-1][:] = [x / BSAdict[k] for x in results[k][1:][-1]]

    # nb of PV data
    x = np.arange(4)
    fig, ax = plt.subplots()
    r = [results['faivre'][-1][0],
         results['lariou'][-1][0],
         results['ageorges'][-1][0],
         results['delima'][-1][0]]
    plt.bar(x, r, color='xkcd:' + col['PV'])
    plt.xticks(x, ('faivre', 'lariou', 'ageorges', 'delima'))
    plt.ylabel('Mean volumetric flow rate (L/min/m2)')
    plt.title("Portal vein")
    # plt.savefig("PV_all_BSA.png")
    plt.show()

    # nb of A-ASC data
    x = np.arange(2)
    fig, ax = plt.subplots()
    r = [
        results['faivre'][-1][3],
        results['lariou'][-1][3]
        # results['ageorges'][-1][0],
        # results['delima'][-1][0]
    ]
    plt.bar(x, r, color='xkcd:' + col['A-ASC'])
    plt.xticks(x, ('faivre', 'lariou'))
    plt.ylabel('Mean volumetric flow rate (L/min/m2)')
    plt.title("Ascending aorta")
    # plt.savefig("A-ASC_all_BSA.png")
    plt.show()

    # nb of A-DES data
    x = np.arange(4)
    fig, ax = plt.subplots()
    r = [
        results['faivre'][-1][2],
        results['lariou'][-1][2],
        # results['ageorges'][-1][0],
        results['delima'][-1][1],
        results['SEBG'][-1][-2]

    ]
    plt.bar(x, r, color='xkcd:' + col['A-DES'])
    plt.xticks(x, ('faivre', 'lariou', 'delima'))
    plt.ylabel('Mean volumetric flow rate (L/min/m2)')
    plt.title("Descending aorta")
    # plt.savefig("A-DES_all_BSA.png")
    plt.show()

    # nb of VCS data
    x = np.arange(1)
    fig, ax = plt.subplots()
    r = [
        results['faivre'][-1][1]
        # results['lariou'][-1][2]
        # results['ageorges'][-1][0],
        # results['delima'][-1][0]
    ]
    plt.bar(x, r, color='xkcd:' + col['VCS'])
    plt.xticks(x, ('faivre'))
    plt.ylabel('Mean volumetric flow rate (L/min/m2)')
    plt.title("Superior vena cava")
    # plt.savefig("VCS_all_BSA.png")
    plt.show()

    # nb of VCI data
    x = np.arange(5)
    fig, ax = plt.subplots()
    r = [
        results['faivre'][-1][4],
        results['lariou'][-1][4],
        # results['ageorges'][-1][0],
        results['delima'][-1][2],
        results['SEBG'][-1][0],
        results['SEBG'][-1][1]

    ]
    plt.bar(x, r, color='xkcd:' + col['VCI'])
    plt.xticks(x, ('faivre', 'lariou', 'delima'))
    plt.ylabel('Mean volumetric flow rate (L/min/m2)')
    plt.title("Inferior vena cava")
    # plt.savefig("VCI_all_BSA.png")
    plt.show()

    # nb of HV data
    x = np.arange(4)
    fig, ax = plt.subplots()
    r = [
        results['faivre'][-1][-1],
        results['lariou'][-1][-1],
        # results['ageorges'][-1][0],
        results['delima'][-1][-1],
        results['SEBG'][-1][-1]

    ]
    plt.bar(x, r, color='xkcd:' + col['HV'])
    plt.xticks(x, ('faivre', 'lariou', 'delima'))
    plt.ylabel('Mean volumetric flow rate (L/min/m2)')
    plt.title("Hepatic veins (sum of)")
    # plt.savefig("HV_all_BSA.png")
    plt.show()

    # HV = HA+PV = 1.2 PV
    x = np.arange(6)
    fig, ax = plt.subplots()
    r = [
        results['faivre'][-1][-1],
        results['faivre'][-1][0] * 1.2,
        results['lariou'][-1][-1],
        results['lariou'][-1][0] * 1.2,
        # results['ageorges'][-1][0],
        results['delima'][-1][-1],
        results['delima'][-1][0] * 1.2
    ]
    barlist = plt.bar(x, r, color='xkcd:' + col['HV'])
    barlist[0].set_color('xkcd:baby blue')
    barlist[1].set_color('xkcd:baby blue')
    barlist[2].set_color('xkcd:bright blue')
    barlist[3].set_color('xkcd:bright blue')
    barlist[4].set_color('xkcd:dark blue')
    barlist[5].set_color('xkcd:dark blue')

    plt.xticks(x, ('faivre HV', 'faivre 1.2*PV', 'lariou HV', 'lariou 1.2*PV', 'delima PV', 'delima  1.2*PV'),
               rotation=45)
    plt.ylabel('Mean volumetric flow rate (L/min/m2)')
    plt.title('HV = HA+PV = 1.2 PV (expected by construction)')
    plt.tight_layout()
    # plt.savefig("HVvsPV.png")
    plt.show()

    # VCI+HV = A-DES
    x = np.arange(6)
    fig, ax = plt.subplots()
    r = [
        results['faivre'][-1][-1] + results['faivre'][-1][4],
        results['faivre'][-1][2],
        results['lariou'][-1][-1] + results['lariou'][-1][4],
        results['lariou'][-1][2],
        results['delima'][-1][-1] + results['delima'][-1][2],
        results['delima'][-1][1],
        # results['ageorges'][-1][0],
    ]
    barlist = plt.bar(x, r, color='xkcd:' + col['A-DES'])
    barlist[0].set_color('xkcd:baby blue')
    barlist[1].set_color('xkcd:baby blue')
    barlist[2].set_color('xkcd:bright blue')
    barlist[3].set_color('xkcd:bright blue')
    barlist[4].set_color('xkcd:dark blue')
    barlist[5].set_color('xkcd:dark blue')

    plt.xticks(x, ('faivre HV+VCI', 'faivre A-DES', 'lariou HV+VCI', 'lariou A-DES', 'delima HV+VCI', 'delima A-DES'),
               rotation=45)
    plt.ylabel('Mean volumetric flow rate (L/min/m2)')
    plt.title('VCI+HV VS A-DES')
    plt.tight_layout()
    # plt.savefig("VCIHVvsADES.png")
    plt.show()

    # VCS = A-ASC - A-DES
    x = np.arange(2)
    fig, ax = plt.subplots()
    r = [
        results['faivre'][-1][3] - results['faivre'][-1][2],
        results['faivre'][-1][1],
        # results['ageorges'][-1][0],
    ]
    barlist = plt.bar(x, r, color='xkcd:' + col['A-DES'])
    barlist[0].set_color('xkcd:baby blue')
    barlist[1].set_color('xkcd:baby blue')
    plt.xticks(x, ('faivre A-ASC - A-DES', 'faivre VCS'),
               rotation=45)
    plt.ylabel('Mean volumetric flow rate (L/min/m2)')
    plt.title('VCS VS A-ASC - A-DES')
    plt.tight_layout()
    # plt.savefig("VCSvsAASCADES.png")
    plt.show()
