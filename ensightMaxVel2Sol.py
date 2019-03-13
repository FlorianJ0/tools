# trace generated using paraview version 5.5.0-RC3-199-gc9ed5ff

#### import the simple module from the paraview
import os
import time
from paraview.simple import *

t0 = time.time()
paraview.simple._DisableFirstRenderCameraReset()

inputCase = '/home/florian/liverSim/simus/LL_transient/ethi_post/NSSolution/Ethi_postTH_VC_definitesm.case'
outputFile = os.path.splitext(inputCase)[0] + '.tsv'
outputFileSol = os.path.splitext(inputCase)[0] + '.sol'

# create a new 'EnSight Reader'
ethi_postTH_VC_definitesmcase = EnSightReader(CaseFileName=inputCase)
ethi_postTH_VC_definitesmcase.PointArrays = ['velocity', 'pressure']
print('Opening files')
# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on ethi_postTH_VC_definitesmcase
ethi_postTH_VC_definitesmcase.PointArrays = ['velocity']

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [767, 783]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 0
renderView1.Background = [0.32, 0.34, 0.43]
renderView1.UseGradientBackground = 1
renderView1.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(0, renderView1)

# show data in view
ethi_postTH_VC_definitesmcaseDisplay = Show(ethi_postTH_VC_definitesmcase, renderView1)

# trace defaults for the display properties.
ethi_postTH_VC_definitesmcaseDisplay.Representation = 'Surface'
ethi_postTH_VC_definitesmcaseDisplay.ColorArrayName = [None, '']
ethi_postTH_VC_definitesmcaseDisplay.OSPRayScaleArray = 'velocity'
ethi_postTH_VC_definitesmcaseDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
ethi_postTH_VC_definitesmcaseDisplay.SelectOrientationVectors = 'velocity'
ethi_postTH_VC_definitesmcaseDisplay.ScaleFactor = 0.019163208454847338
ethi_postTH_VC_definitesmcaseDisplay.SelectScaleArray = 'None'
ethi_postTH_VC_definitesmcaseDisplay.GlyphType = 'Arrow'
ethi_postTH_VC_definitesmcaseDisplay.GlyphTableIndexArray = 'None'
ethi_postTH_VC_definitesmcaseDisplay.GaussianRadius = 0.0009581604227423668
ethi_postTH_VC_definitesmcaseDisplay.SetScaleArray = ['POINTS', 'velocity']
ethi_postTH_VC_definitesmcaseDisplay.ScaleTransferFunction = 'PiecewiseFunction'
ethi_postTH_VC_definitesmcaseDisplay.OpacityArray = ['POINTS', 'velocity']
ethi_postTH_VC_definitesmcaseDisplay.OpacityTransferFunction = 'PiecewiseFunction'
ethi_postTH_VC_definitesmcaseDisplay.DataAxesGrid = 'GridAxesRepresentation'
ethi_postTH_VC_definitesmcaseDisplay.SelectionCellLabelFontFile = ''
ethi_postTH_VC_definitesmcaseDisplay.SelectionPointLabelFontFile = ''
ethi_postTH_VC_definitesmcaseDisplay.PolarAxes = 'PolarAxesRepresentation'
ethi_postTH_VC_definitesmcaseDisplay.ScalarOpacityUnitDistance = 0.004627432311725471

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ethi_postTH_VC_definitesmcaseDisplay.ScaleTransferFunction.Points = [-0.04683300107717514, 0.0, 0.5, 0.0,
                                                                     0.2924340069293976, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ethi_postTH_VC_definitesmcaseDisplay.OpacityTransferFunction.Points = [-0.04683300107717514, 0.0, 0.5, 0.0,
                                                                       0.2924340069293976, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
ethi_postTH_VC_definitesmcaseDisplay.DataAxesGrid.XTitleFontFile = ''
ethi_postTH_VC_definitesmcaseDisplay.DataAxesGrid.YTitleFontFile = ''
ethi_postTH_VC_definitesmcaseDisplay.DataAxesGrid.ZTitleFontFile = ''
ethi_postTH_VC_definitesmcaseDisplay.DataAxesGrid.XLabelFontFile = ''
ethi_postTH_VC_definitesmcaseDisplay.DataAxesGrid.YLabelFontFile = ''
ethi_postTH_VC_definitesmcaseDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
ethi_postTH_VC_definitesmcaseDisplay.PolarAxes.PolarAxisTitleFontFile = ''
ethi_postTH_VC_definitesmcaseDisplay.PolarAxes.PolarAxisLabelFontFile = ''
ethi_postTH_VC_definitesmcaseDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
ethi_postTH_VC_definitesmcaseDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(ethi_postTH_VC_definitesmcaseDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
ethi_postTH_VC_definitesmcaseDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# create a new 'Merge Blocks'
mergeBlocks1 = MergeBlocks(Input=ethi_postTH_VC_definitesmcase)

# show data in view
mergeBlocks1Display = Show(mergeBlocks1, renderView1)
print('Merging blocks')
# trace defaults for the display properties.
mergeBlocks1Display.Representation = 'Surface'
mergeBlocks1Display.ColorArrayName = [None, '']
mergeBlocks1Display.OSPRayScaleArray = 'velocity'
mergeBlocks1Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeBlocks1Display.SelectOrientationVectors = 'velocity'
mergeBlocks1Display.ScaleFactor = 0.019163208454847338
mergeBlocks1Display.SelectScaleArray = 'None'
mergeBlocks1Display.GlyphType = 'Arrow'
mergeBlocks1Display.GlyphTableIndexArray = 'None'
mergeBlocks1Display.GaussianRadius = 0.0009581604227423668
mergeBlocks1Display.SetScaleArray = ['POINTS', 'velocity']
mergeBlocks1Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeBlocks1Display.OpacityArray = ['POINTS', 'velocity']
mergeBlocks1Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeBlocks1Display.DataAxesGrid = 'GridAxesRepresentation'
mergeBlocks1Display.SelectionCellLabelFontFile = ''
mergeBlocks1Display.SelectionPointLabelFontFile = ''
mergeBlocks1Display.PolarAxes = 'PolarAxesRepresentation'
mergeBlocks1Display.ScalarOpacityUnitDistance = 0.004627432311725471

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeBlocks1Display.ScaleTransferFunction.Points = [-0.04683300107717514, 0.0, 0.5, 0.0, 0.2924340069293976, 1.0, 0.5,
                                                    0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeBlocks1Display.OpacityTransferFunction.Points = [-0.04683300107717514, 0.0, 0.5, 0.0, 0.2924340069293976, 1.0, 0.5,
                                                      0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
mergeBlocks1Display.DataAxesGrid.XTitleFontFile = ''
mergeBlocks1Display.DataAxesGrid.YTitleFontFile = ''
mergeBlocks1Display.DataAxesGrid.ZTitleFontFile = ''
mergeBlocks1Display.DataAxesGrid.XLabelFontFile = ''
mergeBlocks1Display.DataAxesGrid.YLabelFontFile = ''
mergeBlocks1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
mergeBlocks1Display.PolarAxes.PolarAxisTitleFontFile = ''
mergeBlocks1Display.PolarAxes.PolarAxisLabelFontFile = ''
mergeBlocks1Display.PolarAxes.LastRadialAxisTextFontFile = ''
mergeBlocks1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(ethi_postTH_VC_definitesmcase, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Temporal Statistics'
temporalStatistics1 = TemporalStatistics(Input=mergeBlocks1)

# Properties modified on temporalStatistics1
temporalStatistics1.ComputeAverage = 0
temporalStatistics1.ComputeMinimum = 0
temporalStatistics1.ComputeStandardDeviation = 0

# show data in view
print('Averaging')
temporalStatistics1Display = Show(temporalStatistics1, renderView1)

# trace defaults for the display properties.
temporalStatistics1Display.Representation = 'Surface'
temporalStatistics1Display.ColorArrayName = [None, '']
temporalStatistics1Display.OSPRayScaleArray = 'velocity_maximum'
temporalStatistics1Display.OSPRayScaleFunction = 'PiecewiseFunction'
temporalStatistics1Display.SelectOrientationVectors = 'None'
temporalStatistics1Display.ScaleFactor = 0.019163208454847338
temporalStatistics1Display.SelectScaleArray = 'None'
temporalStatistics1Display.GlyphType = 'Arrow'
temporalStatistics1Display.GlyphTableIndexArray = 'None'
temporalStatistics1Display.GaussianRadius = 0.0009581604227423668
temporalStatistics1Display.SetScaleArray = ['POINTS', 'velocity_maximum']
temporalStatistics1Display.ScaleTransferFunction = 'PiecewiseFunction'
temporalStatistics1Display.OpacityArray = ['POINTS', 'velocity_maximum']
temporalStatistics1Display.OpacityTransferFunction = 'PiecewiseFunction'
temporalStatistics1Display.DataAxesGrid = 'GridAxesRepresentation'
temporalStatistics1Display.SelectionCellLabelFontFile = ''
temporalStatistics1Display.SelectionPointLabelFontFile = ''
temporalStatistics1Display.PolarAxes = 'PolarAxesRepresentation'
temporalStatistics1Display.ScalarOpacityUnitDistance = 0.004627432311725471

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
temporalStatistics1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.2924340069293976, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
temporalStatistics1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.2924340069293976, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
temporalStatistics1Display.DataAxesGrid.XTitleFontFile = ''
temporalStatistics1Display.DataAxesGrid.YTitleFontFile = ''
temporalStatistics1Display.DataAxesGrid.ZTitleFontFile = ''
temporalStatistics1Display.DataAxesGrid.XLabelFontFile = ''
temporalStatistics1Display.DataAxesGrid.YLabelFontFile = ''
temporalStatistics1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
temporalStatistics1Display.PolarAxes.PolarAxisTitleFontFile = ''
temporalStatistics1Display.PolarAxes.PolarAxisLabelFontFile = ''
temporalStatistics1Display.PolarAxes.LastRadialAxisTextFontFile = ''
temporalStatistics1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(mergeBlocks1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

CreateLayout('Layout #2')

# set active view
SetActiveView(None)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024L
# uncomment following to set a specific view size
# spreadSheetView1.ViewSize = [400, 400]

# get layout
layout2 = GetLayout()

# place view in the layout
layout2.AssignView(0, spreadSheetView1)

# show data in view
temporalStatistics1Display_1 = Show(temporalStatistics1, spreadSheetView1)

# export view
ExportView(outputFile, view=spreadSheetView1, FilterColumnsByVisibility=1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.1250970959663391, 0.18036294355988503, 0.6405672303782145]
renderView1.CameraFocalPoint = [0.1250970959663391, 0.18036294355988503, 0.0947991032153368]
renderView1.CameraParallelScale = 0.1414469546614823

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
print('Wrinting sol file')
with open(outputFile, 'r') as f:
    content = f.readlines()
content = content[1:]
content = [x.split()[3:6] for x in content]
# for x in content:
#     print(float(x[0]))
content = [' '.join(x) for x in content]
content = [x + '\n' for x in content]
nEl = len(content)

content = ''.join(content)

solText = (
        'MeshVersionFormatted 2 \nDimension 3 \nSolAtVertices\n' + str(nEl) + '\n1 2\n'
)
solText += str(content)
solText += 'End'
with open(outputFileSol, 'w') as f:
    f.write(solText     )
print('Out file {} written in {:6.2f}s '.format(outputFileSol, time.time()-t0))
