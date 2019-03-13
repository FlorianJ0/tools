#!/usr/bin/env python
import sys
from vmtk import pypes
from vmtk import vmtkscripts
import numpy as np
import vmtksurfacetonumpy
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
customscript = 'customScript'


class customScript(pypes.pypeScript):

    def __init__(self):
        pypes.pypeScript.__init__(self)
        self.Centerlines = None
        self.Surface = None

        self.RadiusArrayName = 'MaximumInscribedSphereRadius'
        self.ComputeCenterlines = 0

        self.BlankingArrayName = 'Blanking'
        self.GroupIdsArrayName = 'GroupIds'
        self.CenterlineIdsArrayName = 'CenterlineIds'
        self.TractIdsArrayName = 'TractIds'

        self.SetInputMembers([
            # ['Centerlines', 'i', 'vtkPolyData', 1, '', '', 'vmtksurfacereader'],
            ['Surface', 'i', 'vtkPolyData', 1, '', 'the input surface', 'vmtksurfacereader'],
            ['ComputeCenterlines', 'computectrl', 'bool', 1, '', 'if a surface is given, compute first the centerlines']

            # ['RadiusArrayName', 'radiusarray', 'str', 1],
            # ['GroupIdsArrayName', 'groupidsarray', 'str', 1],
            # ['CenterlineIdsArrayName', 'centerlineidsarray', 'str', 1],
            # ['TractIdsArrayName', 'tractidsarray', 'str', 1],
            # ['BlankingArrayName', 'blankingarray', 'str', 1],
        ])
        self.SetOutputMembers([
            # ['Centerlines', 'o', 'vtkPolyData', 1, '', '', 'vmtksurfacewriter'],
            # ['GroupIdsArrayName', 'groupidsarray', 'str', 1],
            # ['CenterlineIdsArrayName', 'centerlineidsarray', 'str', 1],
            # ['TractIdsArrayName', 'tractidsarray', 'str', 1],
            # ['BlankingArrayName', 'blankingarray', 'str', 1]
        ])

    def unit_vector(self, vector):
        # Returns the unit vector of the vector
        return vector / np.linalg.norm(vector)

    def angle_between(self, v1, v2):
        # Returns the angle in radians between vectors 'v1' and 'v2'::
        v1_u = self.unit_vector(v1)
        v2_u = self.unit_vector(v2)
        return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

    def Execute(self):
        print("Compute VC orientation")
        self.ctrliner = vmtkscripts.vmtkCenterlines()
        self.ctrliner.Surface = self.Surface
        self.ctrliner.Execute()
        self.Centerlines = self.ctrliner.Centerlines
        cc = self.Centerlines

        ptCoord = []

        for c in xrange(cc.GetNumberOfPoints()):
            ptCoord.append(cc.GetPoints().GetPoint(c))

        ptCoord = np.array(ptCoord)
        datamean = ptCoord.mean(axis=0)
        uu, dd, vv = np.linalg.svd(ptCoord - datamean)
        # vector of the general direction of the VC
        # print(vv[0], datamean, datamean+10*vv[0])
        VCvect = vv[0]

        if self.ComputeCenterlines:
            # print(self.Surface)
            self.ctrliner = vmtkscripts.vmtkCenterlines()
            self.ctrliner.Surface = self.Surface
            # self.ctrliner.SeedSelector = 'openprofiles'
            self.ctrliner.Execute()
            self.Centerlines = self.ctrliner.Centerlines
            # self.Surface = self.Centerlines
        else:
            self.Centerlines = self.Surface

        # if self.Centerlines == None:
        #     self.PrintError('DUMBASS')

        self.vmtkReader = vmtkscripts.vmtkSurfaceReader()

        self.vmtkRenderer = vmtkscripts.vmtkRenderer()
        self.vmtkRenderer.Initialize()
        self.SurfaceViewer = vmtkscripts.vmtkSurfaceViewer()

        # self.Surface = self.Centerlines
        self.SurfaceViewer.Surface = self.Surface
        self.SurfaceViewer.Execute()

        self.myattr = vmtkscripts.vmtkCenterlineAttributes()
        self.myattr.Centerlines = self.Centerlines
        self.myattr.Execute()

        self.mybranchextractor = vmtkscripts.vmtkBranchExtractor()
        self.mybranchextractor.Centerlines = self.myattr.Centerlines
        self.mybranchextractor.RadiusArrayName = self.RadiusArrayName
        self.mybranchextractor.Execute()

        self.ctrl = self.mybranchextractor.Centerlines

        self.mywriter = vmtkscripts.vmtkSurfaceWriter()
        self.mywriter.Surface = self.mybranchextractor.Centerlines
        self.mywriter.OutputFileName = '/home/florian/liverSim/morpho_analysis/test_surf_open_small_ctrlTESTbranc1.vtp'
        self.mywriter.Execute()

        self.mybifref = vmtkscripts.vmtkBifurcationReferenceSystems()
        self.mybifref.Centerlines = self.ctrl
        self.mybifref.RadiusArrayName = self.RadiusArrayName
        self.mybifref.BlankingArrayName = self.BlankingArrayName
        self.mybifref.GroupIdsArrayName = self.GroupIdsArrayName
        self.mybifref.CenterlineIdsArrayName = self.CenterlineIdsArrayName
        self.mybifref.TractIdsArrayName = self.TractIdsArrayName
        self.mybifref.Execute()

        self.myvect = vmtkscripts.vmtkBifurcationVectors()
        self.myvect.Centerlines = self.ctrl
        self.myvect.ReferenceSystems = self.mybifref.ReferenceSystems
        self.myvect.RadiusArrayName = self.RadiusArrayName
        self.myvect.BlankingArrayName = self.BlankingArrayName
        self.myvect.GroupIdsArrayName = self.GroupIdsArrayName
        self.myvect.TractIdsArrayName = self.TractIdsArrayName
        self.myvect.CenterlineIdsArrayName = self.CenterlineIdsArrayName
        self.myvect.ReferenceSystemsNormalArrayName = self.mybifref.ReferenceSystemsNormalArrayName
        self.myvect.ReferenceSystemsUpNormalArrayName = self.mybifref.ReferenceSystemsUpNormalArrayName
        self.myvect.Execute()

        '''TEMP'''
        self.mywriter = vmtkscripts.vmtkSurfaceWriter()
        self.mywriter.Surface = self.myvect.BifurcationVectors
        self.mywriter.OutputFileName = '/home/florian/liverSim/morpho_analysis/test_surf_open_small_bifvect.vtp'
        self.mywriter.Execute()

        self.mywriter.Surface = self.ctrl
        self.mywriter.OutputFileName = '/home/florian/liverSim/morpho_analysis/test_surf_open_small_ctrl.vtp'
        self.mywriter.Execute()
        '''/TEMP'''



        self.numpytator = vmtksurfacetonumpy.vmtkSurfaceToNumpy()
        self.numpytator.Surface = self.myvect.BifurcationVectors
        self.numpytator.Execute()
        vectData = self.numpytator.ArrayDict.values()

        cprint(figlet_format('Results!', font='bubble'))
        print('\n InPlaneBifurcationVectors angle:')
        print(np.degrees(self.angle_between(vectData[0]["InPlaneBifurcationVectors"][1, :],
                                            vectData[0]["InPlaneBifurcationVectors"][2, :])))
        # print('\n OutOfPlaneBifurcationVectors angle:')
        # print(np.degrees(self.angle_between(vectData[0]["OutOfPlaneBifurcationVectors"][1, :],
        #                                     vectData[0]["OutOfPlaneBifurcationVectors"][2, :])))
        print('\n bifurcation angle with the VC:')
        print(np.degrees(self.angle_between(vectData[0]["OutOfPlaneBifurcationVectors"][0, :],
                                            VCvect)))
        '''
        weighted average vector between the vectors pointing from the second 
        to the first reference point on each centerline
        '''
        print('\n global direction of the birfurcation:')
        print(vectData[0]["BifurcationVectors"][0, :])
        '''
        the origin of the bifurcation is defined as the barycenter of the four reference points
         weighted by the surface of the maximum inscribed sphere defined on the reference points. 
         The reason of the weighting is that small branches have less impact on the position of 
         the bifurcation origin
        '''
        print('\n Origin of the bifurcation:')
        print(vectData[1][0])
        pass


if __name__ == '__main__':
    main = pypes.pypeMain()
    main.Arguments = sys.argv
    main.Execute()
