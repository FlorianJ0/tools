import struct
import vtk
import sys
from vmtk import pypes
import numpy as np
# fname = sys.argv[1]
# outfname = sys.argv[2]
fname = "/home/florian/liverSim/test_convert/CHARBONNIER^ERIC^GILBERT-1.2.840.113704.7.32.1.2.840.113704.1.111.11064.1445517251.25-REC-477.rawiv"
outfname = "/home/florian/liverSim/test_convert/toto.vti"
outSurfName = outfname[:-4]+'_surf.vtp'


print '\n reading ', fname
with open(fname, 'rb') as f:
    PacketHeader = f.read(68)
    dataImg = f.read()

img = {'minXYZ': struct.unpack('>fff', PacketHeader[0:12]), 'maxXYZ': struct.unpack('>fff', PacketHeader[12:24]),
       'numVerts': struct.unpack('>I', PacketHeader[24:28]), 'numCells': struct.unpack('>I', PacketHeader[28:32]),
       'dimXYZ': struct.unpack('>III', PacketHeader[32:44]), 'originXYZ': struct.unpack('>fff', PacketHeader[44:56]),
       'spanXYZ': struct.unpack('>fff', PacketHeader[56:68])}
print img
nbytes = len(dataImg)
elsize = nbytes / img['numCells'][0]
nelements = img['numVerts'][0]

toto = struct.unpack('>' + str(nelements) + 'B', dataImg)

print '\n done reading \n creating image'
toto = list(toto)
print max(toto)
m = np.indices([np.int(max(toto))])
m = list(m[0])
print 'indices in volue :', m
# toto[toto == True] = 1
# toto[toto == False] = 0

dx = (img['maxXYZ'][0] - img['minXYZ'][0]) / img['dimXYZ'][0]
dy = (img['maxXYZ'][1] - img['minXYZ'][1]) / img['dimXYZ'][1]
dz = (img['maxXYZ'][2] - img['minXYZ'][2]) / img['dimXYZ'][2]

imageData = vtk.vtkImageData()
imageData.SetDimensions(img['dimXYZ'][0], img['dimXYZ'][1], img['dimXYZ'][2])
imageData.SetSpacing(img['spanXYZ'][0], img['spanXYZ'][1], img['spanXYZ'][2])
imageData.SetOrigin(img['minXYZ'][0], img['minXYZ'][1], img['minXYZ'][2])
# print img

if vtk.VTK_MAJOR_VERSION <= 5:
    imageData.SetNumberOfScalarComponents(1)
    imageData.SetScalarTypeToDouble()
else:
    imageData.AllocateScalars(vtk.VTK_INT, 1)

dims = imageData.GetDimensions()
print 'image size: ', dims
k = 0
r = 1  # reduction coeff for quick tests
for z in range(dims[2] / r):
    if z % (dims[2] / 8) == 0:
        print 100 - (z * 100 / dims[2] / r), ' % restant.\n'
    for y in range(dims[1]):
        for x in range(dims[0] / r):
            imageData.SetScalarComponentFromFloat(x, y, z, 0, toto[k])
            k += 1

print 'writing...'

writer = vtk.vtkXMLImageDataWriter()
writer.SetFileName(outfname)
if vtk.VTK_MAJOR_VERSION <= 5:
    writer.SetInputConnection(imageData.GetProducerPort())
else:
    writer.SetInputData(imageData)
writer.Write()
print outfname, ' written\n\nbyebye'


MC = 'vmtkmarchingcubes -ifile  ' + outfname + '  -l 0.5 -ofile ' + outSurfName + '  --pipe vmtksurfaceviewer'
myPype = pypes.PypeRun(MC)
