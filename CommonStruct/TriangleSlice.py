from copy import deepcopy

from Point3D import *
from Triangle import *


class TriangleSlice:
    def __init__(self, xFacet=Point3D(), xVertex=Triangle()):
        """
        三角面片初始化函数

        :param xFacet: 法向量
        :param xVertex: 顶点(3个)
        """
        self.__facet = deepcopy(xFacet)
        self.__vertex = deepcopy(xVertex)

    @property
    def facet(self):
        return self.__facet

    @property
    def vertex(self):
        return self.__vertex

    @facet.setter
    def facet(self, xFacet):
        self.__facet = deepcopy(xFacet)

    @vertex.setter
    def vertex(self, xVertex):
        self.__vertex = deepcopy(xVertex)

    def __str__(self):
        return 'facet: %s, vectex: %s' % (self.__facet, self.__vertex)


if __name__ == '__main__':
    testTriangle = TriangleSlice()
    print(testTriangle)
