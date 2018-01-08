import struct
import vtk

fname = "/home/florian/Downloads/toto.rawiv"
outfname = "/home/florian/Downloads/toto.vti"
with open(fname, 'rb') as f:
    PacketHeader = f.read(68)
    dataImg = f.read()

img = {}

img['minXYZ']   =	struct.unpack('>fff',PacketHeader[0:12])
img['maxXYZ']   =	struct.unpack('>fff',PacketHeader[12:24])
img['numVerts'] =	struct.unpack('>I',PacketHeader[24:28])
img['numCells'] =	struct.unpack('>I',PacketHeader[28:32])
img['dimXYZ']   =	struct.unpack('>III',PacketHeader[32:44])
img['originXYZ']    =	struct.unpack('>fff',PacketHeader[44:56])
img['spanXYZ']  =	struct.unpack('>fff',PacketHeader[56:68])

nbytes = len(dataImg)
elsize = nbytes/img['numCells'][0]
nelements = img['numVerts'][0]

toto = struct.unpack('>'+str(nelements)+'?',dataImg)
toto = list(toto)
toto[toto==True] = 1
toto[toto==False] = 0


imageData = vtk.vtkImageData()
imageData.SetDimensions(img['dimXYZ'][0], img['dimXYZ'][1], img['dimXYZ'][2])

if vtk.VTK_MAJOR_VERSION <= 5:
    imageData.SetNumberOfScalarComponents(1)
    imageData.SetScalarTypeToDouble()
else:
    imageData.AllocateScalars(vtk.VTK_DOUBLE, 1)

dims = imageData.GetDimensions()
print dims
k=0
for z in range(dims[2]):
    if z%(dims[2]/8) == 0:
        print 100-(z*100/dims[2]),' % restant.\n'
    for y in range(dims[1]):
        for x in range(dims[0]):
            imageData.SetScalarComponentFromDouble(x, y, z, 0, toto[k])
            k+=1



contour = vtk.vtkDiscreteMarchingCubes()
if vtk.VTK_MAJOR_VERSION <= 5:
    contour.SetInput(imageData.GetOutput())
else:
    contour.SetInputConnection(imageData.GetOutputPort())

writer = vtk.vtkXMLImageDataWriter()
writer.SetFileName(outfname)
if vtk.VTK_MAJOR_VERSION <= 5:
    writer.SetInputConnection(imageData.GetProducerPort())
else:
    writer.SetInputData(imageData)
writer.Write()