"""
三角形
"""
from CommonStruct import Point3D
from copy import deepcopy


class Triangle:
    def __init__(self, xVertex1, xVertex2, xVertex3):
        assert isinstance(xVertex1, Point3D) and isinstance(xVertex2, Point3D) and isinstance(xVertex3, Point3D)
        self.__vertex1 = deepcopy(xVertex1)
        self.__vertex2 = deepcopy(xVertex2)
        self.__vertex3 = deepcopy(xVertex3)

    @property
    def vertex1(self):
        return self.__vertex1

    @property
    def vertex2(self):
        return self.__vertex2

    @property
    def vertex3(self):
        return self.__vertex3

    @vertex1.setter
    def vertex1(self, xVertex1):
        self.__vertex1 = deepcopy(xVertex1)

    @vertex2.setter
    def vertex2(self, xVertex2):
        self.__vertex2 = deepcopy(xVertex2)

    @vertex3.setter
    def vertex3(self, xVertex3):
        self.__vertex3 = deepcopy(xVertex3)

    def __str__(self):
        return '[%s,%s,%s]' % (self.__vertex1, self.__vertex2, self.__vertex3)


if __name__ == '__main__':
    testPoint1 = Point3D(0, 0, 0)
    testPoint2 = Point3D(1, 0, 0)
    testPoint3 = Point3D(0, 1, 0)
    testTriangle = Triangle(testPoint1, testPoint2, testPoint3)
    testPoint1.x = 2
    print(testPoint1)
    print(testTriangle)
