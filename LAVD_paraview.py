# trace generated using paraview version 5.5.2
from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs
from vtk.util import numpy_support
from scipy import ndimage, misc
import numpy as np
import operator
from paraview.servermanager import *
from paraview.simple import *

fname = '/home/florian/codes/liverSim/simus/B1/ceri_postBL_LT/NSSolution/Ceri_postTH_LTxx_volbl.case'

dx = 0.1  # dx for resampling EN CM
sf = 1  # starting iter for integration
tf = 30  # final iter for integration

Show(EnSightReader(CaseFileName=fname))
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()
Render()
# Get a nice view angle
cam = GetActiveCamera()
cam.Elevation(45)
Render()
# Check the current view time
view = GetActiveView()
reader = GetActiveSource()
reader.TimestepValues
tsteps = reader.TimestepValues
tsteps = tsteps[sf:tf + 3]
# animationScene1.GoToNext()

[minx, maxx, miny, maxy, minz, maxz] = reader.GetDataInformation().GetBounds()
[nx, ny, nz] = abs(maxx - minx) / dx, abs(maxz - minz) / dx, abs(maxz - minz) / dx
resamp = ResampleToImage(reader)
resamp.SamplingDimensions = [int(nx), int(ny), int(nz)]
Show(resamp)

grad = GradientOfUnstructuredDataSet(resamp)
grad.ScalarArray = 'velocity'
grad.ComputeDivergence = 1
grad.ComputeQCriterion = 1
grad.ComputeVorticity = 1
Show(grad)

domain = ImageDatatoPointSet(grad)
Show(domain)

particleTracer1 = ParticleTracer(Input=domain, SeedSource=domain)
particleTracer1.StaticMesh = 1
particleTracer1.StaticSeeds = 1
particleTracer1.ComputeVorticity = 0
Show(particleTracer1)

dataPart = paraview.servermanager.Fetch(particleTracer1)
ptdata = dataPart.GetPointData()
ptdatavort = ptdata.GetArray("Vorticity")
ptdataID = ptdata.GetArray("ParticleId")

nbpts_ini = ptdatavort.GetNumberOfTuples()
# get tuple ? ptdatavort.GetTuple(id)
smV = np.zeros([nbpts_ini, 3])

animationScene1.GoToNext()
# smVort = ptdatavort
# smVort.SetName("smVort")
# ptdata.AddArray(smVort)
animationScene1.GoToPrevious()
for i in xrange(len(tsteps)):
    animationScene1.GoToNext()
    dataPart = paraview.servermanager.Fetch(particleTracer1)
    ptdata = dataPart.GetPointData()
    ptdatavort = ptdata.GetArray("Vorticity")
    ptdataID = ptdata.GetArray("ParticleId")
    nbpts = ptdatavort.GetNumberOfTuples()
    for j in xrange(nbpts):  # nb of pts
        trackid = ptdataID.GetValue(j)  # id of point
        a = ptdatavort.GetTuple(j)  # vort at point
        smV[trackid, :] += a[0], a[1], a[2]  # sum of val at corresponding id

animationScene1.GoToFirst()

dataPart = paraview.servermanager.Fetch(particleTracer1)
ptdata = dataPart.GetPointData()
# dataPart.AllocatePointGhostArray()
smVort = ptdata.GetArray("Vorticity")
smVort.SetName("smVort")
ptdata.AddArray(smVort)
for i in xrange(int(nbpts_ini)):
    smVort.SetTuple3(i, smV[i, 0], smV[i, 1], smV[i, 2])

t = TrivialProducer()
filter = t.GetClientSideObject()  # filter is a vtkTrivialProducer
filter.SetOutput(dataPart)
t.UpdatePipeline()
mergeBlocks1 = MergeBlocks(Input=reader)
#
# pointDatasetInterpolator1 = PoiasetInterpolator(Input=trivialProducer1, Source=mergeBlocks1)
# pointDatasetInterpolator1.Kernel = 'VoronoiKernel'
# pointDatasetInterpolator1.Locator = 'Static Point Locator'

