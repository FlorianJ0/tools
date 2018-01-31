import vtk
import numpy as np
import os
from vtk.util import numpy_support
from vmtk import pypes
from vmtk import vmtkscripts
import time

start_time = time.time()

loc = '/home/florian/liverSim/test_convert/'
# surf with VC open at both NumberOfEndpointSpheres
surfFile = loc + "test.vtp"
fname = os.path.splitext(os.path.split(surfFile)[1])[0]

args = "vmtksurfacereader -ifile " + surfFile
myPype = pypes.PypeRun(args)
mySurface = myPype.GetScriptObject('vmtksurfacereader', '0').Surface

ntwk = vmtkscripts.vmtkNetworkExtraction()
ntwk.Surface = mySurface
ntwk.Execute()
myWriter = vmtkscripts.vmtkSurfaceWriter()
myWriter.Surface = ntwk.Network
myWriter.OutputFileName = loc + "network.vtp"
myWriter.Execute()


polyDataOutput = ntwk.Network
test = 0  # if 1 then compute only a few ctrl

cellData = polyDataOutput.GetCellData()
cellNumber = polyDataOutput.GetNumberOfCells()
points = polyDataOutput.GetPoints()

print 'total cell number in network tree: ', cellNumber

# extraction of topology field
arrTopo = numpy_support.vtk_to_numpy(cellData.GetArray(0))

# magic formula vmtk
outletsCells = []
outletsCells = (arrTopo[:, 0] + 1) * (arrTopo[:, 1] + 1)

BCids = []
for i in range(len(outletsCells)):
    if outletsCells[i] < 1:
        BCids.append(i)

print 'nb cells in domain: ', len(arrTopo), '; nb of BC cells: ', len(BCids)

pointData = polyDataOutput.GetPointData()
arrRadius = numpy_support.vtk_to_numpy(pointData.GetArray(0))
arrRadius = arrRadius.tolist()
VC = []

for i, j in enumerate(arrRadius):
    if j == 0.0:
        VC.append(points.GetPoint(i))

# getting list of first and last point in BC cells
ptListTotal = []
for i in xrange(cellNumber):
    cell = polyDataOutput.GetCell(i)
    nIds = cell.GetPointIds().GetNumberOfIds()
    ids = [cell.GetPointIds().GetId(0), cell.GetPointIds().GetId(nIds - 1)]
    coord0 = points.GetPoint(ids[0])
    coord1 = points.GetPoint(ids[1])
    ptListTotal.append(coord0)
    ptListTotal.append(coord1)
ptList = []
# addition of the VC inlet
ptList.append(VC[-1])
print ptList
points = polyDataOutput.GetPoints()
for i in range(len(BCids)):
    cell = polyDataOutput.GetCell(BCids[i])
    nIds = cell.GetPointIds().GetNumberOfIds()
    ids = [cell.GetPointIds().GetId(0), cell.GetPointIds().GetId(nIds - 1)]
    coord0 = points.GetPoint(ids[0])
    coord1 = points.GetPoint(ids[1])

    if ptListTotal.count(coord0) == 1:
        ptList.append(coord0)
    if ptListTotal.count(coord1) == 1:
        ptList.append(coord1)

flatten = lambda l: [item for sublist in l for item in sublist]
ptList = flatten(ptList)
if test:
    ptList = ptList[:60]

print 'Endpoints extracted, computing centerlines with {:f}\
 outlets'.format(len(ptList) / 3.)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

ctrLines = vmtkscripts.vmtkCenterlines()
ctrLines.Surface = mySurface
ctrLines.SeedSelectorName = 'pointlist'
ctrLines.SourcePoints = VC[0]
ctrLines.TargetPoints = ptList
ctrLines.RadiusArrayName = "radius"
ctrLines.Execute()
print 'Centerlines computed'
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

view = vmtkscripts.vmtkCenterlineViewer()
view.Centerlines = ctrLines.Centerlines
# view.Execute()

myWriter = vmtkscripts.vmtkSurfaceWriter()
myWriter.Surface = ctrLines.Centerlines
myWriter.OutputFileName = loc + fname + "_ctrlines.vtp"
myWriter.Execute()

# quit()


ext = vmtkscripts.vmtkEndpointExtractor()
ext.Centerlines = ctrLines.Centerlines
ext.RadiusArrayName = "radius"
ext.GroupIdsArray = "GroupIds"
ext.BlankingArrayName = "BlankIds"
ext.NumberOfEndpointSpheres = 1
ext.NumberOfGapSpheres = 1
ext.Execute()
print 'Endpoints extracted for BC clipping'
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

clip = vmtkscripts.vmtkBranchClipper()
clip.Surface = mySurface
clip.Centerlines = ext.Centerlines
# clip.cutoffradiusfactor = 0.1
clip.BlankingArrayName = "BlankIds"
clip.GroupIdsArrayName = "GroupIds"
clip.RadiusArrayName = "radius"
clip.Progress = 1
print 'Branches clipped'
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

clip.Execute()

myWriter.Surface = clip.Surface
myWriter.OutputFileName = loc + fname + "_endTubesClip.vtp"
myWriter.Execute()


con = vmtkscripts.vmtkSurfaceConnectivity()
con.Surface = clip.Surface
con.CleanOutput = 1
con.Execute()
print 'Connectivity executed'
print("--- %s seconds ---" % (time.time() - start_time))

view = vmtkscripts.vmtkSurfaceViewer()
view.Surface = con.Surface
view.Execute()

start_time = time.time()


myWriter.Surface = con.Surface
myWriter.OutputFileName = loc + fname + "_endTubesCut.vtp"
myWriter.Execute()

print 'Surfaces written to disk'
print("--- %s seconds ---" % (time.time() - start_time))

print '\n\nBye babe'
