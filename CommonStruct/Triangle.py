from copy import deepcopy

import math
from Point3D import *


class Triangle:
    def __init__(self, xVertex1=Point3D(), xVertex2=Point3D(), xVertex3=Point3D()):
        assert isinstance(xVertex1, Point3D) and \
               isinstance(xVertex2, Point3D) and \
               isinstance(xVertex3, Point3D)
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

    def centroid(self):
        """
        计算三角形的质心，三个点的平均值
        """
        centroid_x = (self.__vertex1.x + self.__vertex2.x + self.__vertex3.x) / 3
        centroid_y = (self.__vertex1.y + self.__vertex2.y + self.__vertex3.y) / 3
        centroid_z = (self.__vertex1.z + self.__vertex2.z + self.__vertex3.z) / 3
        return Point3D(centroid_x, centroid_y, centroid_z)

    def area(self):
        # 向量AB
        Vector_AB = Point3D((self.vertex2.x - self.vertex1.x),
                            (self.vertex2.y - self.vertex1.y),
                            (self.vertex2.z - self.vertex1.z))
        # 向量AC
        Vector_AC = Point3D((self.vertex3.x - self.vertex1.x),
                            (self.vertex3.y - self.vertex1.y),
                            (self.vertex3.z - self.vertex1.z))
        # 向量AB叉乘向量AC
        # | i  j  k |
        # |x1 y1 z1 |
        # |x2 y2 z2 |
        # (y1*z2-y2*z1, x2*z1-x1*z2, x1*y2-x2*y1)
        x_ABC = Point3D((Vector_AB.y * Vector_AC.z - Vector_AC.y * Vector_AB.z),
                        (Vector_AB.z * Vector_AC.x - Vector_AC.z * Vector_AB.x),
                        (Vector_AB.x * Vector_AC.y - Vector_AC.x * Vector_AB.y))
        Triangle_Area = math.sqrt(x_ABC.x * x_ABC.x + x_ABC.y * x_ABC.y + x_ABC.z * x_ABC.x) / 2
        return Triangle_Area

    def isInTriangle(self, xPoint):
        # 判断点是否在三角形内部
        # 通过面积的方式来判断，当点xPoint内部时，四个三角形的面积加起来是相等的
        triangle_1 = Triangle(xPoint, self.__vertex2, self.__vertex3)
        triangle_2 = Triangle(self.__vertex1, xPoint, self.__vertex3)
        triangle_3 = Triangle(self.__vertex1, self.__vertex2, xPoint)
        area1 = self.area()
        area2 = triangle_1.area()
        area3 = triangle_2.area()
        area4 = triangle_3.area()
        areaAll = area2 + area3 + area4
        if math.fabs(areaAll - area1) < area1 / 100:
            return True
        return False

    def __str__(self):
        return '[%s,%s,%s]' % (self.__vertex1, self.__vertex2, self.__vertex3)


if __name__ == '__main__':
    testPoint1 = Point3D(0, 0, 0)
    testPoint2 = Point3D(1, 0, 0)
    testPoint3 = Point3D(0, 1, 0)
    testTriangle = Triangle(testPoint1, testPoint2, testPoint3)
    print(testTriangle)
