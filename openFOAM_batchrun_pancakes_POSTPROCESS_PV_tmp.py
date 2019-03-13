# trace generated using paraview version 5.6.0-343-g71e8f64
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
# set active view

case = 2
posx = 6.6106513e-05
posy = 4.78821313e-05
radius = 1e-05

paraview.simple._DisableFirstRenderCameraReset()
outputFileCsv = '/home/florian/pancake_noflow_10micron_'+str(case)+'.csv'
# create a new 'EnSight Reader'
dO255M1_DA_DPPIV_GS_pancakescase = EnSightReader(CaseFileName='/home/florian/OpenFOAM/florian-dev/run/pancanke_noflow_'+str(case)+'/DO255M1_DA_DPPIV_GS_pancakes.case')
dO255M1_DA_DPPIV_GS_pancakescase.CellArrays = ['Ct']
dO255M1_DA_DPPIV_GS_pancakescase.PointArrays = []

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1020, 801]

# show data in view
dO255M1_DA_DPPIV_GS_pancakescaseDisplay = Show(dO255M1_DA_DPPIV_GS_pancakescase, renderView1)

# get color transfer function/color map for 'Ct'
ctLUT = GetColorTransferFunction('Ct')

# get opacity transfer function/opacity map for 'Ct'
ctPWF = GetOpacityTransferFunction('Ct')

# trace defaults for the display properties.
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Representation = 'Surface'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.AmbientColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ColorArrayName = ['CELLS', 'Ct']
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DiffuseColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.LookupTable = ctLUT
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.MapScalars = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.MultiComponentsMapping = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.InterpolateScalarsBeforeMapping = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Opacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PointSize = 2.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.LineWidth = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.RenderLinesAsTubes = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.RenderPointsAsSpheres = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Interpolation = 'Gouraud'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Specular = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SpecularColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SpecularPower = 100.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Luminosity = 0.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Ambient = 0.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Diffuse = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.EdgeColor = [0.0, 0.0, 0.5]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.BackfaceRepresentation = 'Follow Frontface'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.BackfaceOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Position = [0.0, 0.0, 0.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Scale = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Orientation = [0.0, 0.0, 0.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Origin = [0.0, 0.0, 0.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Pickable = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Texture = None
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Triangulate = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.UseShaderReplacements = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ShaderReplacements = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.NonlinearSubdivisionLevel = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.UseDataPartitions = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OSPRayUseScaleArray = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OSPRayScaleArray = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OSPRayMaterial = 'None'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Orient = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OrientationMode = 'Direction'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectOrientationVectors = 'None'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Scaling = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ScaleMode = 'No Data Scaling Off'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ScaleFactor = 1.5944432203696123e-05
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectScaleArray = 'Ct'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.GlyphType = 'Arrow'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.UseGlyphTable = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.GlyphTableIndexArray = 'Ct'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.UseCompositeGlyphTable = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.UseGlyphCullingAndLOD = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.LODValues = []
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ColorByLODIndex = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.GaussianRadius = 7.972216101848062e-07
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ShaderPreset = 'Sphere'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.CustomTriangleScale = 3
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.Emissive = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ScaleByArray = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SetScaleArray = [None, '']
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ScaleArrayComponent = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.UseScaleFunction = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ScaleTransferFunction = 'PiecewiseFunction'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OpacityByArray = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OpacityArray = [None, '']
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OpacityArrayComponent = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OpacityTransferFunction = 'PiecewiseFunction'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid = 'GridAxesRepresentation'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionCellLabelBold = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionCellLabelFontFamily = 'Arial'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionCellLabelFontFile = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionCellLabelFontSize = 18
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionCellLabelItalic = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionCellLabelJustification = 'Left'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionCellLabelOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionCellLabelShadow = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionPointLabelBold = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionPointLabelFontFamily = 'Arial'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionPointLabelFontFile = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionPointLabelFontSize = 18
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionPointLabelItalic = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionPointLabelJustification = 'Left'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionPointLabelOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectionPointLabelShadow = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes = 'PolarAxesRepresentation'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ScalarOpacityFunction = ctPWF
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ScalarOpacityUnitDistance = 1.2863236123424107e-06
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SelectMapper = 'Projected tetra'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SamplingDimensions = [128, 128, 128]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.2855755373823543, 1.0, 0.5, 0.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.GlyphType.TipResolution = 6
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.GlyphType.TipRadius = 0.1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.GlyphType.TipLength = 0.35
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.GlyphType.ShaftResolution = 6
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.GlyphType.ShaftRadius = 0.03
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XTitle = 'X Axis'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YTitle = 'Y Axis'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZTitle = 'Z Axis'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XTitleFontFile = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XTitleBold = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XTitleItalic = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XTitleFontSize = 12
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XTitleShadow = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XTitleOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YTitleFontFile = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YTitleBold = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YTitleItalic = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YTitleFontSize = 12
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YTitleShadow = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YTitleOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZTitleFontFile = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZTitleBold = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZTitleItalic = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZTitleFontSize = 12
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZTitleShadow = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZTitleOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.FacesToRender = 63
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.CullBackface = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.CullFrontface = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ShowGrid = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ShowEdges = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ShowTicks = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.AxesToLabel = 63
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XLabelFontFile = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XLabelBold = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XLabelItalic = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XLabelFontSize = 12
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XLabelShadow = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XLabelOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YLabelFontFile = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YLabelBold = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YLabelItalic = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YLabelFontSize = 12
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YLabelShadow = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YLabelOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZLabelFontFile = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZLabelBold = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZLabelItalic = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZLabelFontSize = 12
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZLabelShadow = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZLabelOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XAxisPrecision = 2
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.XAxisLabels = []
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YAxisPrecision = 2
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.YAxisLabels = []
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZAxisPrecision = 2
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.Visibility = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.EnableCustomRange = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.CustomRange = [0.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisVisibility = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.RadialAxesVisibility = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.DrawRadialGridlines = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarArcsVisibility = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.DrawPolarArcsGridlines = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.NumberOfRadialAxes = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.AutoSubdividePolarAxis = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.NumberOfPolarAxis = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.MinimumRadius = 0.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.MinimumAngle = 0.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.MaximumAngle = 90.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.Ratio = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTitleVisibility = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarLabelVisibility = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.RadialLabelVisibility = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.RadialUnitsVisibility = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.ScreenSize = 10.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTitleFontFile = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTitleBold = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTitleItalic = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTitleShadow = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTitleFontSize = 12
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisLabelFontFile = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisLabelBold = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisLabelItalic = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisLabelShadow = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisLabelFontSize = 12
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisTextBold = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisTextItalic = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisTextShadow = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.EnableDistanceLOD = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.DistanceLODThreshold = 0.7
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.EnableViewAngleLOD = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarTicksVisibility = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.TickLocation = 'Both'
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.AxisTickVisibility = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.AxisMinorTickVisibility = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.ArcTickVisibility = 1
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.ArcMinorTickVisibility = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.DeltaAngleMajor = 10.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.DeltaAngleMinor = 5.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.ArcMajorTickSize = 0.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.ArcTickRatioSize = 0.3
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.ArcMajorTickThickness = 1.0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.ArcTickRatioThickness = 0.5
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.Use2DMode = 0
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
dO255M1_DA_DPPIV_GS_pancakescaseDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on dO255M1_DA_DPPIV_GS_pancakescase
dO255M1_DA_DPPIV_GS_pancakescase.CellArrays = ['Ct']

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Merge Blocks'
mergeBlocks1 = MergeBlocks(Input=dO255M1_DA_DPPIV_GS_pancakescase)
mergeBlocks1.MergePoints = 1

# show data in view
mergeBlocks1Display = Show(mergeBlocks1, renderView1)

# trace defaults for the display properties.
mergeBlocks1Display.Representation = 'Surface'
mergeBlocks1Display.AmbientColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.ColorArrayName = ['CELLS', 'Ct']
mergeBlocks1Display.DiffuseColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.LookupTable = ctLUT
mergeBlocks1Display.MapScalars = 1
mergeBlocks1Display.MultiComponentsMapping = 0
mergeBlocks1Display.InterpolateScalarsBeforeMapping = 1
mergeBlocks1Display.Opacity = 1.0
mergeBlocks1Display.PointSize = 2.0
mergeBlocks1Display.LineWidth = 1.0
mergeBlocks1Display.RenderLinesAsTubes = 0
mergeBlocks1Display.RenderPointsAsSpheres = 0
mergeBlocks1Display.Interpolation = 'Gouraud'
mergeBlocks1Display.Specular = 1.0
mergeBlocks1Display.SpecularColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.SpecularPower = 100.0
mergeBlocks1Display.Luminosity = 0.0
mergeBlocks1Display.Ambient = 0.0
mergeBlocks1Display.Diffuse = 1.0
mergeBlocks1Display.EdgeColor = [0.0, 0.0, 0.5]
mergeBlocks1Display.BackfaceRepresentation = 'Follow Frontface'
mergeBlocks1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.BackfaceOpacity = 1.0
mergeBlocks1Display.Position = [0.0, 0.0, 0.0]
mergeBlocks1Display.Scale = [1.0, 1.0, 1.0]
mergeBlocks1Display.Orientation = [0.0, 0.0, 0.0]
mergeBlocks1Display.Origin = [0.0, 0.0, 0.0]
mergeBlocks1Display.Pickable = 1
mergeBlocks1Display.Texture = None
mergeBlocks1Display.Triangulate = 0
mergeBlocks1Display.UseShaderReplacements = 0
mergeBlocks1Display.ShaderReplacements = ''
mergeBlocks1Display.NonlinearSubdivisionLevel = 1
mergeBlocks1Display.UseDataPartitions = 0
mergeBlocks1Display.OSPRayUseScaleArray = 0
mergeBlocks1Display.OSPRayScaleArray = ''
mergeBlocks1Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeBlocks1Display.OSPRayMaterial = 'None'
mergeBlocks1Display.Orient = 0
mergeBlocks1Display.OrientationMode = 'Direction'
mergeBlocks1Display.SelectOrientationVectors = 'None'
mergeBlocks1Display.Scaling = 0
mergeBlocks1Display.ScaleMode = 'No Data Scaling Off'
mergeBlocks1Display.ScaleFactor = 1.5944432203696123e-05
mergeBlocks1Display.SelectScaleArray = 'Ct'
mergeBlocks1Display.GlyphType = 'Arrow'
mergeBlocks1Display.UseGlyphTable = 0
mergeBlocks1Display.GlyphTableIndexArray = 'Ct'
mergeBlocks1Display.UseCompositeGlyphTable = 0
mergeBlocks1Display.UseGlyphCullingAndLOD = 0
mergeBlocks1Display.LODValues = []
mergeBlocks1Display.ColorByLODIndex = 0
mergeBlocks1Display.GaussianRadius = 7.972216101848062e-07
mergeBlocks1Display.ShaderPreset = 'Sphere'
mergeBlocks1Display.CustomTriangleScale = 3
mergeBlocks1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
mergeBlocks1Display.Emissive = 0
mergeBlocks1Display.ScaleByArray = 0
mergeBlocks1Display.SetScaleArray = [None, '']
mergeBlocks1Display.ScaleArrayComponent = 0
mergeBlocks1Display.UseScaleFunction = 1
mergeBlocks1Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeBlocks1Display.OpacityByArray = 0
mergeBlocks1Display.OpacityArray = [None, '']
mergeBlocks1Display.OpacityArrayComponent = 0
mergeBlocks1Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeBlocks1Display.DataAxesGrid = 'GridAxesRepresentation'
mergeBlocks1Display.SelectionCellLabelBold = 0
mergeBlocks1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
mergeBlocks1Display.SelectionCellLabelFontFamily = 'Arial'
mergeBlocks1Display.SelectionCellLabelFontFile = ''
mergeBlocks1Display.SelectionCellLabelFontSize = 18
mergeBlocks1Display.SelectionCellLabelItalic = 0
mergeBlocks1Display.SelectionCellLabelJustification = 'Left'
mergeBlocks1Display.SelectionCellLabelOpacity = 1.0
mergeBlocks1Display.SelectionCellLabelShadow = 0
mergeBlocks1Display.SelectionPointLabelBold = 0
mergeBlocks1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
mergeBlocks1Display.SelectionPointLabelFontFamily = 'Arial'
mergeBlocks1Display.SelectionPointLabelFontFile = ''
mergeBlocks1Display.SelectionPointLabelFontSize = 18
mergeBlocks1Display.SelectionPointLabelItalic = 0
mergeBlocks1Display.SelectionPointLabelJustification = 'Left'
mergeBlocks1Display.SelectionPointLabelOpacity = 1.0
mergeBlocks1Display.SelectionPointLabelShadow = 0
mergeBlocks1Display.PolarAxes = 'PolarAxesRepresentation'
mergeBlocks1Display.ScalarOpacityFunction = ctPWF
mergeBlocks1Display.ScalarOpacityUnitDistance = 1.2863236123424107e-06
mergeBlocks1Display.SelectMapper = 'Projected tetra'
mergeBlocks1Display.SamplingDimensions = [128, 128, 128]
mergeBlocks1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
mergeBlocks1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.2855755373823543, 1.0, 0.5, 0.0]
mergeBlocks1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
mergeBlocks1Display.GlyphType.TipResolution = 6
mergeBlocks1Display.GlyphType.TipRadius = 0.1
mergeBlocks1Display.GlyphType.TipLength = 0.35
mergeBlocks1Display.GlyphType.ShaftResolution = 6
mergeBlocks1Display.GlyphType.ShaftRadius = 0.03
mergeBlocks1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeBlocks1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
mergeBlocks1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeBlocks1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
mergeBlocks1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
mergeBlocks1Display.DataAxesGrid.XTitle = 'X Axis'
mergeBlocks1Display.DataAxesGrid.YTitle = 'Y Axis'
mergeBlocks1Display.DataAxesGrid.ZTitle = 'Z Axis'
mergeBlocks1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
mergeBlocks1Display.DataAxesGrid.XTitleFontFile = ''
mergeBlocks1Display.DataAxesGrid.XTitleBold = 0
mergeBlocks1Display.DataAxesGrid.XTitleItalic = 0
mergeBlocks1Display.DataAxesGrid.XTitleFontSize = 12
mergeBlocks1Display.DataAxesGrid.XTitleShadow = 0
mergeBlocks1Display.DataAxesGrid.XTitleOpacity = 1.0
mergeBlocks1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
mergeBlocks1Display.DataAxesGrid.YTitleFontFile = ''
mergeBlocks1Display.DataAxesGrid.YTitleBold = 0
mergeBlocks1Display.DataAxesGrid.YTitleItalic = 0
mergeBlocks1Display.DataAxesGrid.YTitleFontSize = 12
mergeBlocks1Display.DataAxesGrid.YTitleShadow = 0
mergeBlocks1Display.DataAxesGrid.YTitleOpacity = 1.0
mergeBlocks1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
mergeBlocks1Display.DataAxesGrid.ZTitleFontFile = ''
mergeBlocks1Display.DataAxesGrid.ZTitleBold = 0
mergeBlocks1Display.DataAxesGrid.ZTitleItalic = 0
mergeBlocks1Display.DataAxesGrid.ZTitleFontSize = 12
mergeBlocks1Display.DataAxesGrid.ZTitleShadow = 0
mergeBlocks1Display.DataAxesGrid.ZTitleOpacity = 1.0
mergeBlocks1Display.DataAxesGrid.FacesToRender = 63
mergeBlocks1Display.DataAxesGrid.CullBackface = 0
mergeBlocks1Display.DataAxesGrid.CullFrontface = 1
mergeBlocks1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.DataAxesGrid.ShowGrid = 0
mergeBlocks1Display.DataAxesGrid.ShowEdges = 1
mergeBlocks1Display.DataAxesGrid.ShowTicks = 1
mergeBlocks1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
mergeBlocks1Display.DataAxesGrid.AxesToLabel = 63
mergeBlocks1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
mergeBlocks1Display.DataAxesGrid.XLabelFontFile = ''
mergeBlocks1Display.DataAxesGrid.XLabelBold = 0
mergeBlocks1Display.DataAxesGrid.XLabelItalic = 0
mergeBlocks1Display.DataAxesGrid.XLabelFontSize = 12
mergeBlocks1Display.DataAxesGrid.XLabelShadow = 0
mergeBlocks1Display.DataAxesGrid.XLabelOpacity = 1.0
mergeBlocks1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
mergeBlocks1Display.DataAxesGrid.YLabelFontFile = ''
mergeBlocks1Display.DataAxesGrid.YLabelBold = 0
mergeBlocks1Display.DataAxesGrid.YLabelItalic = 0
mergeBlocks1Display.DataAxesGrid.YLabelFontSize = 12
mergeBlocks1Display.DataAxesGrid.YLabelShadow = 0
mergeBlocks1Display.DataAxesGrid.YLabelOpacity = 1.0
mergeBlocks1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
mergeBlocks1Display.DataAxesGrid.ZLabelFontFile = ''
mergeBlocks1Display.DataAxesGrid.ZLabelBold = 0
mergeBlocks1Display.DataAxesGrid.ZLabelItalic = 0
mergeBlocks1Display.DataAxesGrid.ZLabelFontSize = 12
mergeBlocks1Display.DataAxesGrid.ZLabelShadow = 0
mergeBlocks1Display.DataAxesGrid.ZLabelOpacity = 1.0
mergeBlocks1Display.DataAxesGrid.XAxisNotation = 'Mixed'
mergeBlocks1Display.DataAxesGrid.XAxisPrecision = 2
mergeBlocks1Display.DataAxesGrid.XAxisUseCustomLabels = 0
mergeBlocks1Display.DataAxesGrid.XAxisLabels = []
mergeBlocks1Display.DataAxesGrid.YAxisNotation = 'Mixed'
mergeBlocks1Display.DataAxesGrid.YAxisPrecision = 2
mergeBlocks1Display.DataAxesGrid.YAxisUseCustomLabels = 0
mergeBlocks1Display.DataAxesGrid.YAxisLabels = []
mergeBlocks1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
mergeBlocks1Display.DataAxesGrid.ZAxisPrecision = 2
mergeBlocks1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
mergeBlocks1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
mergeBlocks1Display.PolarAxes.Visibility = 0
mergeBlocks1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
mergeBlocks1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
mergeBlocks1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
mergeBlocks1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
mergeBlocks1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
mergeBlocks1Display.PolarAxes.EnableCustomRange = 0
mergeBlocks1Display.PolarAxes.CustomRange = [0.0, 1.0]
mergeBlocks1Display.PolarAxes.PolarAxisVisibility = 1
mergeBlocks1Display.PolarAxes.RadialAxesVisibility = 1
mergeBlocks1Display.PolarAxes.DrawRadialGridlines = 1
mergeBlocks1Display.PolarAxes.PolarArcsVisibility = 1
mergeBlocks1Display.PolarAxes.DrawPolarArcsGridlines = 1
mergeBlocks1Display.PolarAxes.NumberOfRadialAxes = 0
mergeBlocks1Display.PolarAxes.AutoSubdividePolarAxis = 1
mergeBlocks1Display.PolarAxes.NumberOfPolarAxis = 0
mergeBlocks1Display.PolarAxes.MinimumRadius = 0.0
mergeBlocks1Display.PolarAxes.MinimumAngle = 0.0
mergeBlocks1Display.PolarAxes.MaximumAngle = 90.0
mergeBlocks1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
mergeBlocks1Display.PolarAxes.Ratio = 1.0
mergeBlocks1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.PolarAxes.PolarAxisTitleVisibility = 1
mergeBlocks1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
mergeBlocks1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
mergeBlocks1Display.PolarAxes.PolarLabelVisibility = 1
mergeBlocks1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
mergeBlocks1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
mergeBlocks1Display.PolarAxes.RadialLabelVisibility = 1
mergeBlocks1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
mergeBlocks1Display.PolarAxes.RadialLabelLocation = 'Bottom'
mergeBlocks1Display.PolarAxes.RadialUnitsVisibility = 1
mergeBlocks1Display.PolarAxes.ScreenSize = 10.0
mergeBlocks1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
mergeBlocks1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
mergeBlocks1Display.PolarAxes.PolarAxisTitleFontFile = ''
mergeBlocks1Display.PolarAxes.PolarAxisTitleBold = 0
mergeBlocks1Display.PolarAxes.PolarAxisTitleItalic = 0
mergeBlocks1Display.PolarAxes.PolarAxisTitleShadow = 0
mergeBlocks1Display.PolarAxes.PolarAxisTitleFontSize = 12
mergeBlocks1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
mergeBlocks1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
mergeBlocks1Display.PolarAxes.PolarAxisLabelFontFile = ''
mergeBlocks1Display.PolarAxes.PolarAxisLabelBold = 0
mergeBlocks1Display.PolarAxes.PolarAxisLabelItalic = 0
mergeBlocks1Display.PolarAxes.PolarAxisLabelShadow = 0
mergeBlocks1Display.PolarAxes.PolarAxisLabelFontSize = 12
mergeBlocks1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
mergeBlocks1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
mergeBlocks1Display.PolarAxes.LastRadialAxisTextFontFile = ''
mergeBlocks1Display.PolarAxes.LastRadialAxisTextBold = 0
mergeBlocks1Display.PolarAxes.LastRadialAxisTextItalic = 0
mergeBlocks1Display.PolarAxes.LastRadialAxisTextShadow = 0
mergeBlocks1Display.PolarAxes.LastRadialAxisTextFontSize = 12
mergeBlocks1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
mergeBlocks1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
mergeBlocks1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
mergeBlocks1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
mergeBlocks1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
mergeBlocks1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
mergeBlocks1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
mergeBlocks1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
mergeBlocks1Display.PolarAxes.EnableDistanceLOD = 1
mergeBlocks1Display.PolarAxes.DistanceLODThreshold = 0.7
mergeBlocks1Display.PolarAxes.EnableViewAngleLOD = 1
mergeBlocks1Display.PolarAxes.ViewAngleLODThreshold = 0.7
mergeBlocks1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
mergeBlocks1Display.PolarAxes.PolarTicksVisibility = 1
mergeBlocks1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
mergeBlocks1Display.PolarAxes.TickLocation = 'Both'
mergeBlocks1Display.PolarAxes.AxisTickVisibility = 1
mergeBlocks1Display.PolarAxes.AxisMinorTickVisibility = 0
mergeBlocks1Display.PolarAxes.ArcTickVisibility = 1
mergeBlocks1Display.PolarAxes.ArcMinorTickVisibility = 0
mergeBlocks1Display.PolarAxes.DeltaAngleMajor = 10.0
mergeBlocks1Display.PolarAxes.DeltaAngleMinor = 5.0
mergeBlocks1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
mergeBlocks1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
mergeBlocks1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
mergeBlocks1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
mergeBlocks1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
mergeBlocks1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
mergeBlocks1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
mergeBlocks1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
mergeBlocks1Display.PolarAxes.ArcMajorTickSize = 0.0
mergeBlocks1Display.PolarAxes.ArcTickRatioSize = 0.3
mergeBlocks1Display.PolarAxes.ArcMajorTickThickness = 1.0
mergeBlocks1Display.PolarAxes.ArcTickRatioThickness = 0.5
mergeBlocks1Display.PolarAxes.Use2DMode = 0
mergeBlocks1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(dO255M1_DA_DPPIV_GS_pancakescase, renderView1)

# show color bar/color legend
mergeBlocks1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=mergeBlocks1)
cellDatatoPointData1.ProcessAllArrays = 1
cellDatatoPointData1.CellDataArraytoprocess = ['Ct']
cellDatatoPointData1.PassCellData = 0
cellDatatoPointData1.PieceInvariant = 0

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)

# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Surface'
cellDatatoPointData1Display.AmbientColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.ColorArrayName = ['POINTS', 'Ct']
cellDatatoPointData1Display.DiffuseColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.LookupTable = ctLUT
cellDatatoPointData1Display.MapScalars = 1
cellDatatoPointData1Display.MultiComponentsMapping = 0
cellDatatoPointData1Display.InterpolateScalarsBeforeMapping = 1
cellDatatoPointData1Display.Opacity = 1.0
cellDatatoPointData1Display.PointSize = 2.0
cellDatatoPointData1Display.LineWidth = 1.0
cellDatatoPointData1Display.RenderLinesAsTubes = 0
cellDatatoPointData1Display.RenderPointsAsSpheres = 0
cellDatatoPointData1Display.Interpolation = 'Gouraud'
cellDatatoPointData1Display.Specular = 1.0
cellDatatoPointData1Display.SpecularColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.SpecularPower = 100.0
cellDatatoPointData1Display.Luminosity = 0.0
cellDatatoPointData1Display.Ambient = 0.0
cellDatatoPointData1Display.Diffuse = 1.0
cellDatatoPointData1Display.EdgeColor = [0.0, 0.0, 0.5]
cellDatatoPointData1Display.BackfaceRepresentation = 'Follow Frontface'
cellDatatoPointData1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.BackfaceOpacity = 1.0
cellDatatoPointData1Display.Position = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.Scale = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.Orientation = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.Origin = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.Pickable = 1
cellDatatoPointData1Display.Texture = None
cellDatatoPointData1Display.Triangulate = 0
cellDatatoPointData1Display.UseShaderReplacements = 0
cellDatatoPointData1Display.ShaderReplacements = ''
cellDatatoPointData1Display.NonlinearSubdivisionLevel = 1
cellDatatoPointData1Display.UseDataPartitions = 0
cellDatatoPointData1Display.OSPRayUseScaleArray = 0
cellDatatoPointData1Display.OSPRayScaleArray = 'Ct'
cellDatatoPointData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OSPRayMaterial = 'None'
cellDatatoPointData1Display.Orient = 0
cellDatatoPointData1Display.OrientationMode = 'Direction'
cellDatatoPointData1Display.SelectOrientationVectors = 'Ct'
cellDatatoPointData1Display.Scaling = 0
cellDatatoPointData1Display.ScaleMode = 'No Data Scaling Off'
cellDatatoPointData1Display.ScaleFactor = 1.5944432203696123e-05
cellDatatoPointData1Display.SelectScaleArray = 'Ct'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.UseGlyphTable = 0
cellDatatoPointData1Display.GlyphTableIndexArray = 'Ct'
cellDatatoPointData1Display.UseCompositeGlyphTable = 0
cellDatatoPointData1Display.UseGlyphCullingAndLOD = 0
cellDatatoPointData1Display.LODValues = []
cellDatatoPointData1Display.ColorByLODIndex = 0
cellDatatoPointData1Display.GaussianRadius = 7.972216101848062e-07
cellDatatoPointData1Display.ShaderPreset = 'Sphere'
cellDatatoPointData1Display.CustomTriangleScale = 3
cellDatatoPointData1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
cellDatatoPointData1Display.Emissive = 0
cellDatatoPointData1Display.ScaleByArray = 0
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'Ct']
cellDatatoPointData1Display.ScaleArrayComponent = ''
cellDatatoPointData1Display.UseScaleFunction = 1
cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OpacityByArray = 0
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'Ct']
cellDatatoPointData1Display.OpacityArrayComponent = ''
cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData1Display.SelectionCellLabelBold = 0
cellDatatoPointData1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
cellDatatoPointData1Display.SelectionCellLabelFontFamily = 'Arial'
cellDatatoPointData1Display.SelectionCellLabelFontFile = ''
cellDatatoPointData1Display.SelectionCellLabelFontSize = 18
cellDatatoPointData1Display.SelectionCellLabelItalic = 0
cellDatatoPointData1Display.SelectionCellLabelJustification = 'Left'
cellDatatoPointData1Display.SelectionCellLabelOpacity = 1.0
cellDatatoPointData1Display.SelectionCellLabelShadow = 0
cellDatatoPointData1Display.SelectionPointLabelBold = 0
cellDatatoPointData1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
cellDatatoPointData1Display.SelectionPointLabelFontFamily = 'Arial'
cellDatatoPointData1Display.SelectionPointLabelFontFile = ''
cellDatatoPointData1Display.SelectionPointLabelFontSize = 18
cellDatatoPointData1Display.SelectionPointLabelItalic = 0
cellDatatoPointData1Display.SelectionPointLabelJustification = 'Left'
cellDatatoPointData1Display.SelectionPointLabelOpacity = 1.0
cellDatatoPointData1Display.SelectionPointLabelShadow = 0
cellDatatoPointData1Display.PolarAxes = 'PolarAxesRepresentation'
cellDatatoPointData1Display.ScalarOpacityFunction = ctPWF
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 1.2863236123424107e-06
cellDatatoPointData1Display.SelectMapper = 'Projected tetra'
cellDatatoPointData1Display.SamplingDimensions = [128, 128, 128]
cellDatatoPointData1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
cellDatatoPointData1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.2855755373823543, 1.0, 0.5, 0.0]
cellDatatoPointData1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
cellDatatoPointData1Display.GlyphType.TipResolution = 6
cellDatatoPointData1Display.GlyphType.TipRadius = 0.1
cellDatatoPointData1Display.GlyphType.TipLength = 0.35
cellDatatoPointData1Display.GlyphType.ShaftResolution = 6
cellDatatoPointData1Display.GlyphType.ShaftRadius = 0.03
cellDatatoPointData1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cellDatatoPointData1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.009999999776482582, 1.0, 0.5, 0.0]
cellDatatoPointData1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cellDatatoPointData1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.009999999776482582, 1.0, 0.5, 0.0]
cellDatatoPointData1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
cellDatatoPointData1Display.DataAxesGrid.XTitle = 'X Axis'
cellDatatoPointData1Display.DataAxesGrid.YTitle = 'Y Axis'
cellDatatoPointData1Display.DataAxesGrid.ZTitle = 'Z Axis'
cellDatatoPointData1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
cellDatatoPointData1Display.DataAxesGrid.XTitleFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.XTitleBold = 0
cellDatatoPointData1Display.DataAxesGrid.XTitleItalic = 0
cellDatatoPointData1Display.DataAxesGrid.XTitleFontSize = 12
cellDatatoPointData1Display.DataAxesGrid.XTitleShadow = 0
cellDatatoPointData1Display.DataAxesGrid.XTitleOpacity = 1.0
cellDatatoPointData1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
cellDatatoPointData1Display.DataAxesGrid.YTitleFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.YTitleBold = 0
cellDatatoPointData1Display.DataAxesGrid.YTitleItalic = 0
cellDatatoPointData1Display.DataAxesGrid.YTitleFontSize = 12
cellDatatoPointData1Display.DataAxesGrid.YTitleShadow = 0
cellDatatoPointData1Display.DataAxesGrid.YTitleOpacity = 1.0
cellDatatoPointData1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
cellDatatoPointData1Display.DataAxesGrid.ZTitleFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.ZTitleBold = 0
cellDatatoPointData1Display.DataAxesGrid.ZTitleItalic = 0
cellDatatoPointData1Display.DataAxesGrid.ZTitleFontSize = 12
cellDatatoPointData1Display.DataAxesGrid.ZTitleShadow = 0
cellDatatoPointData1Display.DataAxesGrid.ZTitleOpacity = 1.0
cellDatatoPointData1Display.DataAxesGrid.FacesToRender = 63
cellDatatoPointData1Display.DataAxesGrid.CullBackface = 0
cellDatatoPointData1Display.DataAxesGrid.CullFrontface = 1
cellDatatoPointData1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.DataAxesGrid.ShowGrid = 0
cellDatatoPointData1Display.DataAxesGrid.ShowEdges = 1
cellDatatoPointData1Display.DataAxesGrid.ShowTicks = 1
cellDatatoPointData1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
cellDatatoPointData1Display.DataAxesGrid.AxesToLabel = 63
cellDatatoPointData1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
cellDatatoPointData1Display.DataAxesGrid.XLabelFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.XLabelBold = 0
cellDatatoPointData1Display.DataAxesGrid.XLabelItalic = 0
cellDatatoPointData1Display.DataAxesGrid.XLabelFontSize = 12
cellDatatoPointData1Display.DataAxesGrid.XLabelShadow = 0
cellDatatoPointData1Display.DataAxesGrid.XLabelOpacity = 1.0
cellDatatoPointData1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
cellDatatoPointData1Display.DataAxesGrid.YLabelFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.YLabelBold = 0
cellDatatoPointData1Display.DataAxesGrid.YLabelItalic = 0
cellDatatoPointData1Display.DataAxesGrid.YLabelFontSize = 12
cellDatatoPointData1Display.DataAxesGrid.YLabelShadow = 0
cellDatatoPointData1Display.DataAxesGrid.YLabelOpacity = 1.0
cellDatatoPointData1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
cellDatatoPointData1Display.DataAxesGrid.ZLabelFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.ZLabelBold = 0
cellDatatoPointData1Display.DataAxesGrid.ZLabelItalic = 0
cellDatatoPointData1Display.DataAxesGrid.ZLabelFontSize = 12
cellDatatoPointData1Display.DataAxesGrid.ZLabelShadow = 0
cellDatatoPointData1Display.DataAxesGrid.ZLabelOpacity = 1.0
cellDatatoPointData1Display.DataAxesGrid.XAxisNotation = 'Mixed'
cellDatatoPointData1Display.DataAxesGrid.XAxisPrecision = 2
cellDatatoPointData1Display.DataAxesGrid.XAxisUseCustomLabels = 0
cellDatatoPointData1Display.DataAxesGrid.XAxisLabels = []
cellDatatoPointData1Display.DataAxesGrid.YAxisNotation = 'Mixed'
cellDatatoPointData1Display.DataAxesGrid.YAxisPrecision = 2
cellDatatoPointData1Display.DataAxesGrid.YAxisUseCustomLabels = 0
cellDatatoPointData1Display.DataAxesGrid.YAxisLabels = []
cellDatatoPointData1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
cellDatatoPointData1Display.DataAxesGrid.ZAxisPrecision = 2
cellDatatoPointData1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
cellDatatoPointData1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
cellDatatoPointData1Display.PolarAxes.Visibility = 0
cellDatatoPointData1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
cellDatatoPointData1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
cellDatatoPointData1Display.PolarAxes.EnableCustomRange = 0
cellDatatoPointData1Display.PolarAxes.CustomRange = [0.0, 1.0]
cellDatatoPointData1Display.PolarAxes.PolarAxisVisibility = 1
cellDatatoPointData1Display.PolarAxes.RadialAxesVisibility = 1
cellDatatoPointData1Display.PolarAxes.DrawRadialGridlines = 1
cellDatatoPointData1Display.PolarAxes.PolarArcsVisibility = 1
cellDatatoPointData1Display.PolarAxes.DrawPolarArcsGridlines = 1
cellDatatoPointData1Display.PolarAxes.NumberOfRadialAxes = 0
cellDatatoPointData1Display.PolarAxes.AutoSubdividePolarAxis = 1
cellDatatoPointData1Display.PolarAxes.NumberOfPolarAxis = 0
cellDatatoPointData1Display.PolarAxes.MinimumRadius = 0.0
cellDatatoPointData1Display.PolarAxes.MinimumAngle = 0.0
cellDatatoPointData1Display.PolarAxes.MaximumAngle = 90.0
cellDatatoPointData1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
cellDatatoPointData1Display.PolarAxes.Ratio = 1.0
cellDatatoPointData1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleVisibility = 1
cellDatatoPointData1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
cellDatatoPointData1Display.PolarAxes.PolarLabelVisibility = 1
cellDatatoPointData1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
cellDatatoPointData1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
cellDatatoPointData1Display.PolarAxes.RadialLabelVisibility = 1
cellDatatoPointData1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
cellDatatoPointData1Display.PolarAxes.RadialLabelLocation = 'Bottom'
cellDatatoPointData1Display.PolarAxes.RadialUnitsVisibility = 1
cellDatatoPointData1Display.PolarAxes.ScreenSize = 10.0
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleFontFile = ''
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleBold = 0
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleItalic = 0
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleShadow = 0
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleFontSize = 12
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelFontFile = ''
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelBold = 0
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelItalic = 0
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelShadow = 0
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelFontSize = 12
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextFontFile = ''
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextBold = 0
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextItalic = 0
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextShadow = 0
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextFontSize = 12
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
cellDatatoPointData1Display.PolarAxes.EnableDistanceLOD = 1
cellDatatoPointData1Display.PolarAxes.DistanceLODThreshold = 0.7
cellDatatoPointData1Display.PolarAxes.EnableViewAngleLOD = 1
cellDatatoPointData1Display.PolarAxes.ViewAngleLODThreshold = 0.7
cellDatatoPointData1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
cellDatatoPointData1Display.PolarAxes.PolarTicksVisibility = 1
cellDatatoPointData1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
cellDatatoPointData1Display.PolarAxes.TickLocation = 'Both'
cellDatatoPointData1Display.PolarAxes.AxisTickVisibility = 1
cellDatatoPointData1Display.PolarAxes.AxisMinorTickVisibility = 0
cellDatatoPointData1Display.PolarAxes.ArcTickVisibility = 1
cellDatatoPointData1Display.PolarAxes.ArcMinorTickVisibility = 0
cellDatatoPointData1Display.PolarAxes.DeltaAngleMajor = 10.0
cellDatatoPointData1Display.PolarAxes.DeltaAngleMinor = 5.0
cellDatatoPointData1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
cellDatatoPointData1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
cellDatatoPointData1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
cellDatatoPointData1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
cellDatatoPointData1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
cellDatatoPointData1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
cellDatatoPointData1Display.PolarAxes.ArcMajorTickSize = 0.0
cellDatatoPointData1Display.PolarAxes.ArcTickRatioSize = 0.3
cellDatatoPointData1Display.PolarAxes.ArcMajorTickThickness = 1.0
cellDatatoPointData1Display.PolarAxes.ArcTickRatioThickness = 0.5
cellDatatoPointData1Display.PolarAxes.Use2DMode = 0
cellDatatoPointData1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(mergeBlocks1, renderView1)

# show color bar/color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip1 = Clip(Input=cellDatatoPointData1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'Ct']
clip1.Value = 0.004999999888241291
clip1.Invert = 1
clip1.Crinkleclip = 0
clip1.Exact = 0

# init the 'Plane' selected for 'ClipType'
# clip1.ClipType.Origin = [7.91687461685342e-05, 7.92852182058823e-05, 1.9562974785003462e-05]
# clip1.ClipType.Normal = [1.0, 0.0, 0.0]
# clip1.ClipType.Offset = 0.0

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# Properties modified on clip1.ClipType
# clip1.ClipType.Center = [1.33245134e-05, 7.44170804e-05, 0.0]
# clip1.ClipType.Axis = [0.0, 0.0, 1.0]
# clip1.ClipType.Radius = 5e-06

# Properties modified on clip1
clip1.ClipType = 'Cylinder'

# Properties modified on clip1.ClipType
clip1.ClipType.Center = [posx, posy, 0.0]
clip1.ClipType.Axis = [0.0, 0.0, 1.0]
clip1.ClipType.Radius = radius

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.AmbientColor = [1.0, 1.0, 1.0]
clip1Display.ColorArrayName = ['POINTS', 'Ct']
clip1Display.DiffuseColor = [1.0, 1.0, 1.0]
clip1Display.LookupTable = ctLUT
clip1Display.MapScalars = 1
clip1Display.MultiComponentsMapping = 0
clip1Display.InterpolateScalarsBeforeMapping = 1
clip1Display.Opacity = 1.0
clip1Display.PointSize = 2.0
clip1Display.LineWidth = 1.0
clip1Display.RenderLinesAsTubes = 0
clip1Display.RenderPointsAsSpheres = 0
clip1Display.Interpolation = 'Gouraud'
clip1Display.Specular = 1.0
clip1Display.SpecularColor = [1.0, 1.0, 1.0]
clip1Display.SpecularPower = 100.0
clip1Display.Luminosity = 0.0
clip1Display.Ambient = 0.0
clip1Display.Diffuse = 1.0
clip1Display.EdgeColor = [0.0, 0.0, 0.5]
clip1Display.BackfaceRepresentation = 'Follow Frontface'
clip1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
clip1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
clip1Display.BackfaceOpacity = 1.0
clip1Display.Position = [0.0, 0.0, 0.0]
clip1Display.Scale = [1.0, 1.0, 1.0]
clip1Display.Orientation = [0.0, 0.0, 0.0]
clip1Display.Origin = [0.0, 0.0, 0.0]
clip1Display.Pickable = 1
clip1Display.Texture = None
clip1Display.Triangulate = 0
clip1Display.UseShaderReplacements = 0
clip1Display.ShaderReplacements = ''
clip1Display.NonlinearSubdivisionLevel = 1
clip1Display.UseDataPartitions = 0
clip1Display.OSPRayUseScaleArray = 0
clip1Display.OSPRayScaleArray = 'Ct'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.OSPRayMaterial = 'None'
clip1Display.Orient = 0
clip1Display.OrientationMode = 'Direction'
clip1Display.SelectOrientationVectors = 'Ct'
clip1Display.Scaling = 0
clip1Display.ScaleMode = 'No Data Scaling Off'
clip1Display.ScaleFactor = 2.678160105418215e-06
clip1Display.SelectScaleArray = 'Ct'
clip1Display.GlyphType = 'Arrow'
clip1Display.UseGlyphTable = 0
clip1Display.GlyphTableIndexArray = 'Ct'
clip1Display.UseCompositeGlyphTable = 0
clip1Display.UseGlyphCullingAndLOD = 0
clip1Display.LODValues = []
clip1Display.ColorByLODIndex = 0
clip1Display.GaussianRadius = 1.3390800527091073e-07
clip1Display.ShaderPreset = 'Sphere'
clip1Display.CustomTriangleScale = 3
clip1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
clip1Display.Emissive = 0
clip1Display.ScaleByArray = 0
clip1Display.SetScaleArray = ['POINTS', 'Ct']
clip1Display.ScaleArrayComponent = ''
clip1Display.UseScaleFunction = 1
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityByArray = 0
clip1Display.OpacityArray = ['POINTS', 'Ct']
clip1Display.OpacityArrayComponent = ''
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelBold = 0
clip1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
clip1Display.SelectionCellLabelFontFamily = 'Arial'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionCellLabelFontSize = 18
clip1Display.SelectionCellLabelItalic = 0
clip1Display.SelectionCellLabelJustification = 'Left'
clip1Display.SelectionCellLabelOpacity = 1.0
clip1Display.SelectionCellLabelShadow = 0
clip1Display.SelectionPointLabelBold = 0
clip1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
clip1Display.SelectionPointLabelFontFamily = 'Arial'
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.SelectionPointLabelFontSize = 18
clip1Display.SelectionPointLabelItalic = 0
clip1Display.SelectionPointLabelJustification = 'Left'
clip1Display.SelectionPointLabelOpacity = 1.0
clip1Display.SelectionPointLabelShadow = 0
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = ctPWF
clip1Display.ScalarOpacityUnitDistance = 9.305298968381146e-07
clip1Display.SelectMapper = 'Projected tetra'
clip1Display.SamplingDimensions = [128, 128, 128]
clip1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.2855755373823543, 1.0, 0.5, 0.0]
clip1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
clip1Display.GlyphType.TipResolution = 6
clip1Display.GlyphType.TipRadius = 0.1
clip1Display.GlyphType.TipLength = 0.35
clip1Display.GlyphType.ShaftResolution = 6
clip1Display.GlyphType.ShaftRadius = 0.03
clip1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.009999999776482582, 1.0, 0.5, 0.0]
clip1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.009999999776482582, 1.0, 0.5, 0.0]
clip1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitle = 'X Axis'
clip1Display.DataAxesGrid.YTitle = 'Y Axis'
clip1Display.DataAxesGrid.ZTitle = 'Z Axis'
clip1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
clip1Display.DataAxesGrid.XTitleFontFile = ''
clip1Display.DataAxesGrid.XTitleBold = 0
clip1Display.DataAxesGrid.XTitleItalic = 0
clip1Display.DataAxesGrid.XTitleFontSize = 12
clip1Display.DataAxesGrid.XTitleShadow = 0
clip1Display.DataAxesGrid.XTitleOpacity = 1.0
clip1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
clip1Display.DataAxesGrid.YTitleFontFile = ''
clip1Display.DataAxesGrid.YTitleBold = 0
clip1Display.DataAxesGrid.YTitleItalic = 0
clip1Display.DataAxesGrid.YTitleFontSize = 12
clip1Display.DataAxesGrid.YTitleShadow = 0
clip1Display.DataAxesGrid.YTitleOpacity = 1.0
clip1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
clip1Display.DataAxesGrid.ZTitleFontFile = ''
clip1Display.DataAxesGrid.ZTitleBold = 0
clip1Display.DataAxesGrid.ZTitleItalic = 0
clip1Display.DataAxesGrid.ZTitleFontSize = 12
clip1Display.DataAxesGrid.ZTitleShadow = 0
clip1Display.DataAxesGrid.ZTitleOpacity = 1.0
clip1Display.DataAxesGrid.FacesToRender = 63
clip1Display.DataAxesGrid.CullBackface = 0
clip1Display.DataAxesGrid.CullFrontface = 1
clip1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.ShowGrid = 0
clip1Display.DataAxesGrid.ShowEdges = 1
clip1Display.DataAxesGrid.ShowTicks = 1
clip1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
clip1Display.DataAxesGrid.AxesToLabel = 63
clip1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
clip1Display.DataAxesGrid.XLabelFontFile = ''
clip1Display.DataAxesGrid.XLabelBold = 0
clip1Display.DataAxesGrid.XLabelItalic = 0
clip1Display.DataAxesGrid.XLabelFontSize = 12
clip1Display.DataAxesGrid.XLabelShadow = 0
clip1Display.DataAxesGrid.XLabelOpacity = 1.0
clip1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
clip1Display.DataAxesGrid.YLabelFontFile = ''
clip1Display.DataAxesGrid.YLabelBold = 0
clip1Display.DataAxesGrid.YLabelItalic = 0
clip1Display.DataAxesGrid.YLabelFontSize = 12
clip1Display.DataAxesGrid.YLabelShadow = 0
clip1Display.DataAxesGrid.YLabelOpacity = 1.0
clip1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
clip1Display.DataAxesGrid.ZLabelFontFile = ''
clip1Display.DataAxesGrid.ZLabelBold = 0
clip1Display.DataAxesGrid.ZLabelItalic = 0
clip1Display.DataAxesGrid.ZLabelFontSize = 12
clip1Display.DataAxesGrid.ZLabelShadow = 0
clip1Display.DataAxesGrid.ZLabelOpacity = 1.0
clip1Display.DataAxesGrid.XAxisNotation = 'Mixed'
clip1Display.DataAxesGrid.XAxisPrecision = 2
clip1Display.DataAxesGrid.XAxisUseCustomLabels = 0
clip1Display.DataAxesGrid.XAxisLabels = []
clip1Display.DataAxesGrid.YAxisNotation = 'Mixed'
clip1Display.DataAxesGrid.YAxisPrecision = 2
clip1Display.DataAxesGrid.YAxisUseCustomLabels = 0
clip1Display.DataAxesGrid.YAxisLabels = []
clip1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
clip1Display.DataAxesGrid.ZAxisPrecision = 2
clip1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
clip1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.Visibility = 0
clip1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
clip1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
clip1Display.PolarAxes.EnableCustomRange = 0
clip1Display.PolarAxes.CustomRange = [0.0, 1.0]
clip1Display.PolarAxes.PolarAxisVisibility = 1
clip1Display.PolarAxes.RadialAxesVisibility = 1
clip1Display.PolarAxes.DrawRadialGridlines = 1
clip1Display.PolarAxes.PolarArcsVisibility = 1
clip1Display.PolarAxes.DrawPolarArcsGridlines = 1
clip1Display.PolarAxes.NumberOfRadialAxes = 0
clip1Display.PolarAxes.AutoSubdividePolarAxis = 1
clip1Display.PolarAxes.NumberOfPolarAxis = 0
clip1Display.PolarAxes.MinimumRadius = 0.0
clip1Display.PolarAxes.MinimumAngle = 0.0
clip1Display.PolarAxes.MaximumAngle = 90.0
clip1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
clip1Display.PolarAxes.Ratio = 1.0
clip1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.PolarAxisTitleVisibility = 1
clip1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
clip1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
clip1Display.PolarAxes.PolarLabelVisibility = 1
clip1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
clip1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
clip1Display.PolarAxes.RadialLabelVisibility = 1
clip1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
clip1Display.PolarAxes.RadialLabelLocation = 'Bottom'
clip1Display.PolarAxes.RadialUnitsVisibility = 1
clip1Display.PolarAxes.ScreenSize = 10.0
clip1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
clip1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
clip1Display.PolarAxes.PolarAxisTitleBold = 0
clip1Display.PolarAxes.PolarAxisTitleItalic = 0
clip1Display.PolarAxes.PolarAxisTitleShadow = 0
clip1Display.PolarAxes.PolarAxisTitleFontSize = 12
clip1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
clip1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
clip1Display.PolarAxes.PolarAxisLabelBold = 0
clip1Display.PolarAxes.PolarAxisLabelItalic = 0
clip1Display.PolarAxes.PolarAxisLabelShadow = 0
clip1Display.PolarAxes.PolarAxisLabelFontSize = 12
clip1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
clip1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip1Display.PolarAxes.LastRadialAxisTextBold = 0
clip1Display.PolarAxes.LastRadialAxisTextItalic = 0
clip1Display.PolarAxes.LastRadialAxisTextShadow = 0
clip1Display.PolarAxes.LastRadialAxisTextFontSize = 12
clip1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
clip1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
clip1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
clip1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
clip1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
clip1Display.PolarAxes.EnableDistanceLOD = 1
clip1Display.PolarAxes.DistanceLODThreshold = 0.7
clip1Display.PolarAxes.EnableViewAngleLOD = 1
clip1Display.PolarAxes.ViewAngleLODThreshold = 0.7
clip1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
clip1Display.PolarAxes.PolarTicksVisibility = 1
clip1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
clip1Display.PolarAxes.TickLocation = 'Both'
clip1Display.PolarAxes.AxisTickVisibility = 1
clip1Display.PolarAxes.AxisMinorTickVisibility = 0
clip1Display.PolarAxes.ArcTickVisibility = 1
clip1Display.PolarAxes.ArcMinorTickVisibility = 0
clip1Display.PolarAxes.DeltaAngleMajor = 10.0
clip1Display.PolarAxes.DeltaAngleMinor = 5.0
clip1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
clip1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
clip1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
clip1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
clip1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
clip1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
clip1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
clip1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
clip1Display.PolarAxes.ArcMajorTickSize = 0.0
clip1Display.PolarAxes.ArcTickRatioSize = 0.3
clip1Display.PolarAxes.ArcMajorTickThickness = 1.0
clip1Display.PolarAxes.ArcTickRatioThickness = 0.5
clip1Display.PolarAxes.Use2DMode = 0
clip1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(cellDatatoPointData1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip2 = Clip(Input=clip1)
clip2.ClipType = 'Plane'
clip2.Scalars = ['POINTS', 'Ct']
clip2.Value = 0.004999999888241291
clip2.Invert = 1
clip2.Crinkleclip = 0
clip2.Exact = 0

# init the 'Plane' selected for 'ClipType'
# clip2.ClipType.Origin = [1.3657795079780044e-05, 7.432668644469231e-05, 1.3430900358102349e-05]
# clip2.ClipType.Normal = [1.0, 0.0, 0.0]
clip2.ClipType.Offset = 0.0

# Properties modified on clip2.ClipType
# clip2.ClipType.Origin = [1.3657795079780044e-05, 7.432668644469231e-05, 1e-06]
clip2.ClipType.Normal = [0.0, 0.0, 1.0]

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [1.3657795079780044e-05, 7.432668644469231e-05, 1e-06]
clip2.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip2Display = Show(clip2, renderView1)

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.AmbientColor = [1.0, 1.0, 1.0]
clip2Display.ColorArrayName = ['POINTS', 'Ct']
clip2Display.DiffuseColor = [1.0, 1.0, 1.0]
clip2Display.LookupTable = ctLUT
clip2Display.MapScalars = 1
clip2Display.MultiComponentsMapping = 0
clip2Display.InterpolateScalarsBeforeMapping = 1
clip2Display.Opacity = 1.0
clip2Display.PointSize = 2.0
clip2Display.LineWidth = 1.0
clip2Display.RenderLinesAsTubes = 0
clip2Display.RenderPointsAsSpheres = 0
clip2Display.Interpolation = 'Gouraud'
clip2Display.Specular = 1.0
clip2Display.SpecularColor = [1.0, 1.0, 1.0]
clip2Display.SpecularPower = 100.0
clip2Display.Luminosity = 0.0
clip2Display.Ambient = 0.0
clip2Display.Diffuse = 1.0
clip2Display.EdgeColor = [0.0, 0.0, 0.5]
clip2Display.BackfaceRepresentation = 'Follow Frontface'
clip2Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
clip2Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
clip2Display.BackfaceOpacity = 1.0
clip2Display.Position = [0.0, 0.0, 0.0]
clip2Display.Scale = [1.0, 1.0, 1.0]
clip2Display.Orientation = [0.0, 0.0, 0.0]
clip2Display.Origin = [0.0, 0.0, 0.0]
clip2Display.Pickable = 1
clip2Display.Texture = None
clip2Display.Triangulate = 0
clip2Display.UseShaderReplacements = 0
clip2Display.ShaderReplacements = ''
clip2Display.NonlinearSubdivisionLevel = 1
clip2Display.UseDataPartitions = 0
clip2Display.OSPRayUseScaleArray = 0
clip2Display.OSPRayScaleArray = 'Ct'
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.OSPRayMaterial = 'None'
clip2Display.Orient = 0
clip2Display.OrientationMode = 'Direction'
clip2Display.SelectOrientationVectors = 'Ct'
clip2Display.Scaling = 0
clip2Display.ScaleMode = 'No Data Scaling Off'
clip2Display.ScaleFactor = 8.23428126750514e-07
clip2Display.SelectScaleArray = 'Ct'
clip2Display.GlyphType = 'Arrow'
clip2Display.UseGlyphTable = 0
clip2Display.GlyphTableIndexArray = 'Ct'
clip2Display.UseCompositeGlyphTable = 0
clip2Display.UseGlyphCullingAndLOD = 0
clip2Display.LODValues = []
clip2Display.ColorByLODIndex = 0
clip2Display.GaussianRadius = 4.11714063375257e-08
clip2Display.ShaderPreset = 'Sphere'
clip2Display.CustomTriangleScale = 3
clip2Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
clip2Display.Emissive = 0
clip2Display.ScaleByArray = 0
clip2Display.SetScaleArray = ['POINTS', 'Ct']
clip2Display.ScaleArrayComponent = ''
clip2Display.UseScaleFunction = 1
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityByArray = 0
clip2Display.OpacityArray = ['POINTS', 'Ct']
clip2Display.OpacityArrayComponent = ''
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.SelectionCellLabelBold = 0
clip2Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
clip2Display.SelectionCellLabelFontFamily = 'Arial'
clip2Display.SelectionCellLabelFontFile = ''
clip2Display.SelectionCellLabelFontSize = 18
clip2Display.SelectionCellLabelItalic = 0
clip2Display.SelectionCellLabelJustification = 'Left'
clip2Display.SelectionCellLabelOpacity = 1.0
clip2Display.SelectionCellLabelShadow = 0
clip2Display.SelectionPointLabelBold = 0
clip2Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
clip2Display.SelectionPointLabelFontFamily = 'Arial'
clip2Display.SelectionPointLabelFontFile = ''
clip2Display.SelectionPointLabelFontSize = 18
clip2Display.SelectionPointLabelItalic = 0
clip2Display.SelectionPointLabelJustification = 'Left'
clip2Display.SelectionPointLabelOpacity = 1.0
clip2Display.SelectionPointLabelShadow = 0
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityFunction = ctPWF
clip2Display.ScalarOpacityUnitDistance = 4.1009972013808627e-07
clip2Display.SelectMapper = 'Projected tetra'
clip2Display.SamplingDimensions = [128, 128, 128]
clip2Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip2Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.2855755373823543, 1.0, 0.5, 0.0]
clip2Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
clip2Display.GlyphType.TipResolution = 6
clip2Display.GlyphType.TipRadius = 0.1
clip2Display.GlyphType.TipLength = 0.35
clip2Display.GlyphType.ShaftResolution = 6
clip2Display.GlyphType.ShaftRadius = 0.03
clip2Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display.ScaleTransferFunction.Points = [0.0010993856703862548, 0.0, 0.5, 0.0, 0.009999999776482582, 1.0, 0.5, 0.0]
clip2Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display.OpacityTransferFunction.Points = [0.0010993856703862548, 0.0, 0.5, 0.0, 0.009999999776482582, 1.0, 0.5, 0.0]
clip2Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip2Display.DataAxesGrid.XTitle = 'X Axis'
clip2Display.DataAxesGrid.YTitle = 'Y Axis'
clip2Display.DataAxesGrid.ZTitle = 'Z Axis'
clip2Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
clip2Display.DataAxesGrid.XTitleFontFamily = 'Arial'
clip2Display.DataAxesGrid.XTitleFontFile = ''
clip2Display.DataAxesGrid.XTitleBold = 0
clip2Display.DataAxesGrid.XTitleItalic = 0
clip2Display.DataAxesGrid.XTitleFontSize = 12
clip2Display.DataAxesGrid.XTitleShadow = 0
clip2Display.DataAxesGrid.XTitleOpacity = 1.0
clip2Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
clip2Display.DataAxesGrid.YTitleFontFamily = 'Arial'
clip2Display.DataAxesGrid.YTitleFontFile = ''
clip2Display.DataAxesGrid.YTitleBold = 0
clip2Display.DataAxesGrid.YTitleItalic = 0
clip2Display.DataAxesGrid.YTitleFontSize = 12
clip2Display.DataAxesGrid.YTitleShadow = 0
clip2Display.DataAxesGrid.YTitleOpacity = 1.0
clip2Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
clip2Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
clip2Display.DataAxesGrid.ZTitleFontFile = ''
clip2Display.DataAxesGrid.ZTitleBold = 0
clip2Display.DataAxesGrid.ZTitleItalic = 0
clip2Display.DataAxesGrid.ZTitleFontSize = 12
clip2Display.DataAxesGrid.ZTitleShadow = 0
clip2Display.DataAxesGrid.ZTitleOpacity = 1.0
clip2Display.DataAxesGrid.FacesToRender = 63
clip2Display.DataAxesGrid.CullBackface = 0
clip2Display.DataAxesGrid.CullFrontface = 1
clip2Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
clip2Display.DataAxesGrid.ShowGrid = 0
clip2Display.DataAxesGrid.ShowEdges = 1
clip2Display.DataAxesGrid.ShowTicks = 1
clip2Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
clip2Display.DataAxesGrid.AxesToLabel = 63
clip2Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
clip2Display.DataAxesGrid.XLabelFontFamily = 'Arial'
clip2Display.DataAxesGrid.XLabelFontFile = ''
clip2Display.DataAxesGrid.XLabelBold = 0
clip2Display.DataAxesGrid.XLabelItalic = 0
clip2Display.DataAxesGrid.XLabelFontSize = 12
clip2Display.DataAxesGrid.XLabelShadow = 0
clip2Display.DataAxesGrid.XLabelOpacity = 1.0
clip2Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
clip2Display.DataAxesGrid.YLabelFontFamily = 'Arial'
clip2Display.DataAxesGrid.YLabelFontFile = ''
clip2Display.DataAxesGrid.YLabelBold = 0
clip2Display.DataAxesGrid.YLabelItalic = 0
clip2Display.DataAxesGrid.YLabelFontSize = 12
clip2Display.DataAxesGrid.YLabelShadow = 0
clip2Display.DataAxesGrid.YLabelOpacity = 1.0
clip2Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
clip2Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
clip2Display.DataAxesGrid.ZLabelFontFile = ''
clip2Display.DataAxesGrid.ZLabelBold = 0
clip2Display.DataAxesGrid.ZLabelItalic = 0
clip2Display.DataAxesGrid.ZLabelFontSize = 12
clip2Display.DataAxesGrid.ZLabelShadow = 0
clip2Display.DataAxesGrid.ZLabelOpacity = 1.0
clip2Display.DataAxesGrid.XAxisNotation = 'Mixed'
clip2Display.DataAxesGrid.XAxisPrecision = 2
clip2Display.DataAxesGrid.XAxisUseCustomLabels = 0
clip2Display.DataAxesGrid.XAxisLabels = []
clip2Display.DataAxesGrid.YAxisNotation = 'Mixed'
clip2Display.DataAxesGrid.YAxisPrecision = 2
clip2Display.DataAxesGrid.YAxisUseCustomLabels = 0
clip2Display.DataAxesGrid.YAxisLabels = []
clip2Display.DataAxesGrid.ZAxisNotation = 'Mixed'
clip2Display.DataAxesGrid.ZAxisPrecision = 2
clip2Display.DataAxesGrid.ZAxisUseCustomLabels = 0
clip2Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip2Display.PolarAxes.Visibility = 0
clip2Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
clip2Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
clip2Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
clip2Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
clip2Display.PolarAxes.EnableCustomRange = 0
clip2Display.PolarAxes.CustomRange = [0.0, 1.0]
clip2Display.PolarAxes.PolarAxisVisibility = 1
clip2Display.PolarAxes.RadialAxesVisibility = 1
clip2Display.PolarAxes.DrawRadialGridlines = 1
clip2Display.PolarAxes.PolarArcsVisibility = 1
clip2Display.PolarAxes.DrawPolarArcsGridlines = 1
clip2Display.PolarAxes.NumberOfRadialAxes = 0
clip2Display.PolarAxes.AutoSubdividePolarAxis = 1
clip2Display.PolarAxes.NumberOfPolarAxis = 0
clip2Display.PolarAxes.MinimumRadius = 0.0
clip2Display.PolarAxes.MinimumAngle = 0.0
clip2Display.PolarAxes.MaximumAngle = 90.0
clip2Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
clip2Display.PolarAxes.Ratio = 1.0
clip2Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.PolarAxisTitleVisibility = 1
clip2Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
clip2Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
clip2Display.PolarAxes.PolarLabelVisibility = 1
clip2Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
clip2Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
clip2Display.PolarAxes.RadialLabelVisibility = 1
clip2Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
clip2Display.PolarAxes.RadialLabelLocation = 'Bottom'
clip2Display.PolarAxes.RadialUnitsVisibility = 1
clip2Display.PolarAxes.ScreenSize = 10.0
clip2Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.PolarAxisTitleOpacity = 1.0
clip2Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
clip2Display.PolarAxes.PolarAxisTitleFontFile = ''
clip2Display.PolarAxes.PolarAxisTitleBold = 0
clip2Display.PolarAxes.PolarAxisTitleItalic = 0
clip2Display.PolarAxes.PolarAxisTitleShadow = 0
clip2Display.PolarAxes.PolarAxisTitleFontSize = 12
clip2Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.PolarAxisLabelOpacity = 1.0
clip2Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
clip2Display.PolarAxes.PolarAxisLabelFontFile = ''
clip2Display.PolarAxes.PolarAxisLabelBold = 0
clip2Display.PolarAxes.PolarAxisLabelItalic = 0
clip2Display.PolarAxes.PolarAxisLabelShadow = 0
clip2Display.PolarAxes.PolarAxisLabelFontSize = 12
clip2Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
clip2Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
clip2Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip2Display.PolarAxes.LastRadialAxisTextBold = 0
clip2Display.PolarAxes.LastRadialAxisTextItalic = 0
clip2Display.PolarAxes.LastRadialAxisTextShadow = 0
clip2Display.PolarAxes.LastRadialAxisTextFontSize = 12
clip2Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
clip2Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
clip2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
clip2Display.PolarAxes.SecondaryRadialAxesTextBold = 0
clip2Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
clip2Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
clip2Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
clip2Display.PolarAxes.EnableDistanceLOD = 1
clip2Display.PolarAxes.DistanceLODThreshold = 0.7
clip2Display.PolarAxes.EnableViewAngleLOD = 1
clip2Display.PolarAxes.ViewAngleLODThreshold = 0.7
clip2Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
clip2Display.PolarAxes.PolarTicksVisibility = 1
clip2Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
clip2Display.PolarAxes.TickLocation = 'Both'
clip2Display.PolarAxes.AxisTickVisibility = 1
clip2Display.PolarAxes.AxisMinorTickVisibility = 0
clip2Display.PolarAxes.ArcTickVisibility = 1
clip2Display.PolarAxes.ArcMinorTickVisibility = 0
clip2Display.PolarAxes.DeltaAngleMajor = 10.0
clip2Display.PolarAxes.DeltaAngleMinor = 5.0
clip2Display.PolarAxes.PolarAxisMajorTickSize = 0.0
clip2Display.PolarAxes.PolarAxisTickRatioSize = 0.3
clip2Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
clip2Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
clip2Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
clip2Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
clip2Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
clip2Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
clip2Display.PolarAxes.ArcMajorTickSize = 0.0
clip2Display.PolarAxes.ArcTickRatioSize = 0.3
clip2Display.PolarAxes.ArcMajorTickThickness = 1.0
clip2Display.PolarAxes.ArcTickRatioThickness = 0.5
clip2Display.PolarAxes.Use2DMode = 0
clip2Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plot Data Over Time'
plotDataOverTime1 = PlotDataOverTime(Input=clip2)
plotDataOverTime1.FieldAssociation = 'Points'
plotDataOverTime1.OnlyReportSelectionStatistics = 1

# Create a new 'Quartile Chart View'
quartileChartView1 = CreateView('QuartileChartView')
quartileChartView1.UseCache = 0
quartileChartView1.ViewSize = [505, 801]
quartileChartView1.ChartTitle = ''
quartileChartView1.ChartTitleAlignment = 'Center'
quartileChartView1.ChartTitleFontFamily = 'Arial'
quartileChartView1.ChartTitleFontFile = ''
quartileChartView1.ChartTitleFontSize = 18
quartileChartView1.ChartTitleBold = 0
quartileChartView1.ChartTitleItalic = 0
quartileChartView1.ChartTitleColor = [0.0, 0.0, 0.0]
quartileChartView1.ShowLegend = 1
quartileChartView1.LegendLocation = 'TopRight'
quartileChartView1.SortByXAxis = 0
quartileChartView1.LegendPosition = [0, 0]
quartileChartView1.LegendFontFamily = 'Arial'
quartileChartView1.LegendFontFile = ''
quartileChartView1.LegendFontSize = 12
quartileChartView1.LegendBold = 0
quartileChartView1.LegendItalic = 0
quartileChartView1.TooltipNotation = 'Mixed'
quartileChartView1.TooltipPrecision = 6
quartileChartView1.HideTimeMarker = 0
quartileChartView1.LeftAxisTitle = ''
quartileChartView1.ShowLeftAxisGrid = 1
quartileChartView1.LeftAxisGridColor = [0.95, 0.95, 0.95]
quartileChartView1.LeftAxisColor = [0.0, 0.0, 0.0]
quartileChartView1.LeftAxisTitleFontFamily = 'Arial'
quartileChartView1.LeftAxisTitleFontFile = ''
quartileChartView1.LeftAxisTitleFontSize = 18
quartileChartView1.LeftAxisTitleBold = 1
quartileChartView1.LeftAxisTitleItalic = 0
quartileChartView1.LeftAxisTitleColor = [0.0, 0.0, 0.0]
quartileChartView1.LeftAxisLogScale = 0
quartileChartView1.LeftAxisUseCustomRange = 0
quartileChartView1.LeftAxisRangeMinimum = 0.0
quartileChartView1.LeftAxisRangeMaximum = 1.0
quartileChartView1.ShowLeftAxisLabels = 1
quartileChartView1.LeftAxisLabelNotation = 'Mixed'
quartileChartView1.LeftAxisLabelPrecision = 2
quartileChartView1.LeftAxisUseCustomLabels = 0
quartileChartView1.LeftAxisLabels = []
quartileChartView1.LeftAxisLabelFontFamily = 'Arial'
quartileChartView1.LeftAxisLabelFontFile = ''
quartileChartView1.LeftAxisLabelFontSize = 12
quartileChartView1.LeftAxisLabelBold = 0
quartileChartView1.LeftAxisLabelItalic = 0
quartileChartView1.LeftAxisLabelColor = [0.0, 0.0, 0.0]
quartileChartView1.BottomAxisTitle = ''
quartileChartView1.ShowBottomAxisGrid = 1
quartileChartView1.BottomAxisGridColor = [0.95, 0.95, 0.95]
quartileChartView1.BottomAxisColor = [0.0, 0.0, 0.0]
quartileChartView1.BottomAxisTitleFontFamily = 'Arial'
quartileChartView1.BottomAxisTitleFontFile = ''
quartileChartView1.BottomAxisTitleFontSize = 18
quartileChartView1.BottomAxisTitleBold = 1
quartileChartView1.BottomAxisTitleItalic = 0
quartileChartView1.BottomAxisTitleColor = [0.0, 0.0, 0.0]
quartileChartView1.BottomAxisLogScale = 0
quartileChartView1.BottomAxisUseCustomRange = 0
quartileChartView1.BottomAxisRangeMinimum = 0.0
quartileChartView1.BottomAxisRangeMaximum = 1.0
quartileChartView1.ShowBottomAxisLabels = 1
quartileChartView1.BottomAxisLabelNotation = 'Mixed'
quartileChartView1.BottomAxisLabelPrecision = 2
quartileChartView1.BottomAxisUseCustomLabels = 0
quartileChartView1.BottomAxisLabels = []
quartileChartView1.BottomAxisLabelFontFamily = 'Arial'
quartileChartView1.BottomAxisLabelFontFile = ''
quartileChartView1.BottomAxisLabelFontSize = 12
quartileChartView1.BottomAxisLabelBold = 0
quartileChartView1.BottomAxisLabelItalic = 0
quartileChartView1.BottomAxisLabelColor = [0.0, 0.0, 0.0]
quartileChartView1.RightAxisTitle = ''
quartileChartView1.ShowRightAxisGrid = 1
quartileChartView1.RightAxisGridColor = [0.95, 0.95, 0.95]
quartileChartView1.RightAxisColor = [0.0, 0.0, 0.0]
quartileChartView1.RightAxisTitleFontFamily = 'Arial'
quartileChartView1.RightAxisTitleFontFile = 'Arial'
quartileChartView1.RightAxisTitleFontSize = 18
quartileChartView1.RightAxisTitleBold = 1
quartileChartView1.RightAxisTitleItalic = 0
quartileChartView1.RightAxisTitleColor = [0.0, 0.0, 0.0]
quartileChartView1.RightAxisLogScale = 0
quartileChartView1.RightAxisUseCustomRange = 0
quartileChartView1.RightAxisRangeMinimum = 0.0
quartileChartView1.RightAxisRangeMaximum = 1.0
quartileChartView1.ShowRightAxisLabels = 1
quartileChartView1.RightAxisLabelNotation = 'Mixed'
quartileChartView1.RightAxisLabelPrecision = 2
quartileChartView1.RightAxisUseCustomLabels = 0
quartileChartView1.RightAxisLabels = []
quartileChartView1.RightAxisLabelFontFamily = 'Arial'
quartileChartView1.RightAxisLabelFontFile = ''
quartileChartView1.RightAxisLabelFontSize = 12
quartileChartView1.RightAxisLabelBold = 0
quartileChartView1.RightAxisLabelItalic = 0
quartileChartView1.RightAxisLabelColor = [0.0, 0.0, 0.0]
quartileChartView1.TopAxisTitle = ''
quartileChartView1.ShowTopAxisGrid = 1
quartileChartView1.TopAxisGridColor = [0.95, 0.95, 0.95]
quartileChartView1.TopAxisColor = [0.0, 0.0, 0.0]
quartileChartView1.TopAxisTitleFontFamily = 'Arial'
quartileChartView1.TopAxisTitleFontFile = ''
quartileChartView1.TopAxisTitleFontSize = 18
quartileChartView1.TopAxisTitleBold = 1
quartileChartView1.TopAxisTitleItalic = 0
quartileChartView1.TopAxisTitleColor = [0.0, 0.0, 0.0]
quartileChartView1.TopAxisLogScale = 0
quartileChartView1.TopAxisUseCustomRange = 0
quartileChartView1.TopAxisRangeMinimum = 0.0
quartileChartView1.TopAxisRangeMaximum = 1.0
quartileChartView1.ShowTopAxisLabels = 1
quartileChartView1.TopAxisLabelNotation = 'Mixed'
quartileChartView1.TopAxisLabelPrecision = 2
quartileChartView1.TopAxisUseCustomLabels = 0
quartileChartView1.TopAxisLabels = []
quartileChartView1.TopAxisLabelFontFamily = 'Arial'
quartileChartView1.TopAxisLabelFontFile = ''
quartileChartView1.TopAxisLabelFontSize = 12
quartileChartView1.TopAxisLabelBold = 0
quartileChartView1.TopAxisLabelItalic = 0
quartileChartView1.TopAxisLabelColor = [0.0, 0.0, 0.0]

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(2, quartileChartView1)

# show data in view
plotDataOverTime1Display = Show(plotDataOverTime1, quartileChartView1)

# trace defaults for the display properties.
plotDataOverTime1Display.CompositeDataSetIndex = [1]
plotDataOverTime1Display.AttributeType = 'Row Data'
plotDataOverTime1Display.UseIndexForXAxis = 0
plotDataOverTime1Display.XArrayName = 'Time'
plotDataOverTime1Display.SeriesVisibility = ['Ct (stats)']
plotDataOverTime1Display.SeriesLabel = ['Ct (stats)', 'Ct (stats)', 'X (stats)', 'X (stats)', 'Y (stats)', 'Y (stats)', 'Z (stats)', 'Z (stats)', 'N (stats)', 'N (stats)', 'Time (stats)', 'Time (stats)', 'vtkValidPointMask (stats)', 'vtkValidPointMask (stats)']
plotDataOverTime1Display.SeriesColor = ['Ct (stats)', '0', '0', '0', 'X (stats)', '0.89', '0.1', '0.11', 'Y (stats)', '0.22', '0.49', '0.72', 'Z (stats)', '0.3', '0.69', '0.29', 'N (stats)', '0.6', '0.31', '0.64', 'Time (stats)', '1', '0.5', '0', 'vtkValidPointMask (stats)', '0.65', '0.34', '0.16']
plotDataOverTime1Display.SeriesPlotCorner = ['Ct (stats)', '0', 'X (stats)', '0', 'Y (stats)', '0', 'Z (stats)', '0', 'N (stats)', '0', 'Time (stats)', '0', 'vtkValidPointMask (stats)', '0']
plotDataOverTime1Display.SeriesLabelPrefix = ''
plotDataOverTime1Display.SeriesLineStyle = ['Ct (stats)', '1', 'X (stats)', '1', 'Y (stats)', '1', 'Z (stats)', '1', 'N (stats)', '1', 'Time (stats)', '1', 'vtkValidPointMask (stats)', '1']
plotDataOverTime1Display.SeriesLineThickness = ['Ct (stats)', '2', 'X (stats)', '2', 'Y (stats)', '2', 'Z (stats)', '2', 'N (stats)', '2', 'Time (stats)', '2', 'vtkValidPointMask (stats)', '2']
plotDataOverTime1Display.SeriesMarkerStyle = ['Ct (stats)', '0', 'X (stats)', '0', 'Y (stats)', '0', 'Z (stats)', '0', 'N (stats)', '0', 'Time (stats)', '0', 'vtkValidPointMask (stats)', '0']
plotDataOverTime1Display.ShowQuartiles = 1
plotDataOverTime1Display.ShowRanges = 1
plotDataOverTime1Display.ShowAverage = 1
plotDataOverTime1Display.ShowMedian = 0
plotDataOverTime1Display.ShowMinimum = 0
plotDataOverTime1Display.ShowMaximum = 0

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
quartileChartView1.Update()

# save data
SaveData(outputFileCsv, proxy=plotDataOverTime1, Precision=5,
    UseScientificNotation=1,
    FieldDelimiter=',',
    WriteTimeSteps=0)
