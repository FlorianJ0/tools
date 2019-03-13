#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 22:30:44 2018

@author: florian
"""

# trace generated using paraview version 5.6.0-RC2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
inFile = 'input'
fnameOut = 'output'


paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
bDCoHBC_stationnaryBleachingfoam = OpenFOAMReader(FileName=inFile)
bDCoHBC_stationnaryBleachingfoam.MeshRegions = ['internalMesh']
bDCoHBC_stationnaryBleachingfoam.CellArrays = ['Cb', 'Cb_0', 'Ct', 'Ct_0', 'Dt', 'U', 'ddt0(Cb)', 'ddt0(Ct)']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on bDCoHBC_stationnaryBleachingfoam
bDCoHBC_stationnaryBleachingfoam.CellArrays = ['Ct']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1329, 808]

# show data in view
bDCoHBC_stationnaryBleachingfoamDisplay = Show(bDCoHBC_stationnaryBleachingfoam, renderView1)

# trace defaults for the display properties.
bDCoHBC_stationnaryBleachingfoamDisplay.Representation = 'Surface'
bDCoHBC_stationnaryBleachingfoamDisplay.ColorArrayName = [None, '']
bDCoHBC_stationnaryBleachingfoamDisplay.OSPRayScaleArray = 'Ct'
bDCoHBC_stationnaryBleachingfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
bDCoHBC_stationnaryBleachingfoamDisplay.SelectOrientationVectors = 'Ct'
bDCoHBC_stationnaryBleachingfoamDisplay.ScaleFactor = 8.172300294972957e-06
bDCoHBC_stationnaryBleachingfoamDisplay.SelectScaleArray = 'Ct'
bDCoHBC_stationnaryBleachingfoamDisplay.GlyphType = 'Arrow'
bDCoHBC_stationnaryBleachingfoamDisplay.GlyphTableIndexArray = 'Ct'
bDCoHBC_stationnaryBleachingfoamDisplay.GaussianRadius = 4.0861501474864783e-07
bDCoHBC_stationnaryBleachingfoamDisplay.SetScaleArray = ['POINTS', 'Ct']
bDCoHBC_stationnaryBleachingfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
bDCoHBC_stationnaryBleachingfoamDisplay.OpacityArray = ['POINTS', 'Ct']
bDCoHBC_stationnaryBleachingfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
bDCoHBC_stationnaryBleachingfoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
bDCoHBC_stationnaryBleachingfoamDisplay.SelectionCellLabelFontFile = ''
bDCoHBC_stationnaryBleachingfoamDisplay.SelectionPointLabelFontFile = ''
bDCoHBC_stationnaryBleachingfoamDisplay.PolarAxes = 'PolarAxesRepresentation'
bDCoHBC_stationnaryBleachingfoamDisplay.ScalarOpacityUnitDistance = 2.6116419902960344e-06

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
bDCoHBC_stationnaryBleachingfoamDisplay.DataAxesGrid.XTitleFontFile = ''
bDCoHBC_stationnaryBleachingfoamDisplay.DataAxesGrid.YTitleFontFile = ''
bDCoHBC_stationnaryBleachingfoamDisplay.DataAxesGrid.ZTitleFontFile = ''
bDCoHBC_stationnaryBleachingfoamDisplay.DataAxesGrid.XLabelFontFile = ''
bDCoHBC_stationnaryBleachingfoamDisplay.DataAxesGrid.YLabelFontFile = ''
bDCoHBC_stationnaryBleachingfoamDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
bDCoHBC_stationnaryBleachingfoamDisplay.PolarAxes.PolarAxisTitleFontFile = ''
bDCoHBC_stationnaryBleachingfoamDisplay.PolarAxes.PolarAxisLabelFontFile = ''
bDCoHBC_stationnaryBleachingfoamDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
bDCoHBC_stationnaryBleachingfoamDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip1 = Clip(Input=bDCoHBC_stationnaryBleachingfoam)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'Ct']
clip1.Value = 7.499804087274242e-05

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [3.2749896234918197e-05, 9.75875009316951e-05, 2.8641620019698166e-05]

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [0.0, 1.0, 0.0]

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [0.0, 1.0, 0.0]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = [None, '']
clip1Display.OSPRayScaleArray = 'Ct'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'Ct'
clip1Display.ScaleFactor = 4.875703245943442e-06
clip1Display.SelectScaleArray = 'Ct'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'Ct'
clip1Display.GaussianRadius = 2.4378516229717205e-07
clip1Display.SetScaleArray = ['POINTS', 'Ct']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'Ct']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 2.682462582745188e-06

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleFontFile = ''
clip1Display.DataAxesGrid.YTitleFontFile = ''
clip1Display.DataAxesGrid.ZTitleFontFile = ''
clip1Display.DataAxesGrid.XLabelFontFile = ''
clip1Display.DataAxesGrid.YLabelFontFile = ''
clip1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(bDCoHBC_stationnaryBleachingfoam, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(Input=clip1)
pythonCalculator1.Expression = ''

# Properties modified on pythonCalculator1
pythonCalculator1.Expression = 'mean(Ct)'
pythonCalculator1.ArrayName = 'meanCt'

# show data in view
pythonCalculator1Display = Show(pythonCalculator1, renderView1)

# trace defaults for the display properties.
pythonCalculator1Display.Representation = 'Surface'
pythonCalculator1Display.ColorArrayName = [None, '']
pythonCalculator1Display.OSPRayScaleArray = 'Ct'
pythonCalculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator1Display.SelectOrientationVectors = 'Ct'
pythonCalculator1Display.ScaleFactor = 4.875703245943442e-06
pythonCalculator1Display.SelectScaleArray = 'Ct'
pythonCalculator1Display.GlyphType = 'Arrow'
pythonCalculator1Display.GlyphTableIndexArray = 'Ct'
pythonCalculator1Display.GaussianRadius = 2.4378516229717205e-07
pythonCalculator1Display.SetScaleArray = ['POINTS', 'Ct']
pythonCalculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator1Display.OpacityArray = ['POINTS', 'Ct']
pythonCalculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator1Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator1Display.SelectionCellLabelFontFile = ''
pythonCalculator1Display.SelectionPointLabelFontFile = ''
pythonCalculator1Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator1Display.ScalarOpacityUnitDistance = 2.682462582745188e-06

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator1Display.DataAxesGrid.XTitleFontFile = ''
pythonCalculator1Display.DataAxesGrid.YTitleFontFile = ''
pythonCalculator1Display.DataAxesGrid.ZTitleFontFile = ''
pythonCalculator1Display.DataAxesGrid.XLabelFontFile = ''
pythonCalculator1Display.DataAxesGrid.YLabelFontFile = ''
pythonCalculator1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
pythonCalculator1Display.PolarAxes.PolarAxisTitleFontFile = ''
pythonCalculator1Display.PolarAxes.PolarAxisLabelFontFile = ''
pythonCalculator1Display.PolarAxes.LastRadialAxisTextFontFile = ''
pythonCalculator1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(clip1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plot Data Over Time'
plotDataOverTime1 = PlotDataOverTime(Input=pythonCalculator1)

# Create a new 'Quartile Chart View'
quartileChartView1 = CreateView('QuartileChartView')
quartileChartView1.ViewSize = [660, 808]
quartileChartView1.ChartTitleFontFile = ''
quartileChartView1.LeftAxisTitleFontFile = ''
quartileChartView1.LeftAxisLabelFontFile = ''
quartileChartView1.BottomAxisTitleFontFile = ''
quartileChartView1.BottomAxisLabelFontFile = ''
quartileChartView1.RightAxisLabelFontFile = ''
quartileChartView1.TopAxisTitleFontFile = ''
quartileChartView1.TopAxisLabelFontFile = ''

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(2, quartileChartView1)

# show data in view
plotDataOverTime1Display = Show(plotDataOverTime1, quartileChartView1)

# trace defaults for the display properties.
plotDataOverTime1Display.AttributeType = 'Row Data'
plotDataOverTime1Display.UseIndexForXAxis = 0
plotDataOverTime1Display.XArrayName = 'Time'
plotDataOverTime1Display.SeriesVisibility = ['Ct ( block=1)', 'meanCt ( block=1)']
plotDataOverTime1Display.SeriesLabel = ['Ct ( block=1)', 'Ct ( block=1)', 'meanCt ( block=1)', 'meanCt ( block=1)', 'X ( block=1)', 'X ( block=1)', 'Y ( block=1)', 'Y ( block=1)', 'Z ( block=1)', 'Z ( block=1)', 'N ( block=1)', 'N ( block=1)', 'Time ( block=1)', 'Time ( block=1)', 'vtkValidPointMask ( block=1)', 'vtkValidPointMask ( block=1)']
plotDataOverTime1Display.SeriesColor = ['Ct ( block=1)', '0', '0', '0', 'meanCt ( block=1)', '0.89', '0.1', '0.11', 'X ( block=1)', '0.22', '0.49', '0.72', 'Y ( block=1)', '0.3', '0.69', '0.29', 'Z ( block=1)', '0.6', '0.31', '0.64', 'N ( block=1)', '1', '0.5', '0', 'Time ( block=1)', '0.65', '0.34', '0.16', 'vtkValidPointMask ( block=1)', '0', '0', '0']
plotDataOverTime1Display.SeriesPlotCorner = ['Ct ( block=1)', '0', 'meanCt ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime1Display.SeriesLabelPrefix = ''
plotDataOverTime1Display.SeriesLineStyle = ['Ct ( block=1)', '1', 'meanCt ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime1Display.SeriesLineThickness = ['Ct ( block=1)', '2', 'meanCt ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'N ( block=1)', '2', 'Time ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
plotDataOverTime1Display.SeriesMarkerStyle = ['Ct ( block=1)', '0', 'meanCt ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
quartileChartView1.Update()

# Properties modified on plotDataOverTime1Display
plotDataOverTime1Display.SeriesVisibility = ['meanCt ( block=1)']
plotDataOverTime1Display.SeriesColor = ['Ct ( block=1)', '0', '0', '0', 'meanCt ( block=1)', '0.889998', '0.100008', '0.110002', 'X ( block=1)', '0.220005', '0.489998', '0.719997', 'Y ( block=1)', '0.300008', '0.689998', '0.289998', 'Z ( block=1)', '0.6', '0.310002', '0.639994', 'N ( block=1)', '1', '0.500008', '0', 'Time ( block=1)', '0.650004', '0.340002', '0.160006', 'vtkValidPointMask ( block=1)', '0', '0', '0']
plotDataOverTime1Display.SeriesPlotCorner = ['Ct ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'meanCt ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime1Display.SeriesLineStyle = ['Ct ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'meanCt ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime1Display.SeriesLineThickness = ['Ct ( block=1)', '2', 'N ( block=1)', '2', 'Time ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'meanCt ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
plotDataOverTime1Display.SeriesMarkerStyle = ['Ct ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'meanCt ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']

# save data
SaveData(fnameOut, proxy=plotDataOverTime1, UseScientificNotation=1,
    WriteTimeSteps=1)