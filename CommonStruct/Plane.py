from copy import deepcopy
from CommonStruct import Point3D, Operations


class Plane:
    def __init__(self, *args):
        if len(args) == 2:  # 点法式构造  A(x-x0)+B(y-y0)+C(z-z0)=0
            xPoint, xVector = args
            self.__point0 = deepcopy(xPoint)
            if xVector.z == 0:
                self.__point1 = deepcopy(self.__point0)
                self.__point1.z += 1
                self.__point2 = Point3D(0, 0, 0)
                self.__point2.x = self.__point0.x - (self.__point1.z - self.__point0.z) * xVector.y
                self.__point2.y = self.__point0.y + (self.__point1.z - self.__point0.z) * xVector.x
                self.__point2.z = self.__point0.z + (self.__point1.x - self.__point0.x) * xVector.y - \
                                  (self.__point1.y - self.__point0.y) * xVector.x
            else:
                temp = Operations.dotMultiply(xPoint, xVector)
                self.__point1 = Point3D(xPoint.x, xPoint.y + 1, 0)
                self.__point2 = Point3D(xPoint.x + 1, xPoint.y, 0)
                self.__point1.z = (temp - xVector.x * self.__point1.x - xVector.y * self.__point1.y) / xVector.z
                self.__point2.z = (temp - xVector.x * self.__point2.x - xVector.y * self.__point2.y) / xVector.z
        elif len(args) == 3:  # 三点式构造
            self.__point0 = args[0]
            self.__point1 = args[1]
            self.__point2 = args[2]
        else:
            self.__point0 = None
            self.__point1 = None
            self.__point2 = None

    def normVector(self):
        """
        返回平面的法向量
        :return:
        """
        vector1 = self.__point1 - self.__point0
        vector2 = self.__point2 - self.__point0
        vector3 = Operations.crossMultiply(vector1, vector2)
        return vector3 / vector3.norm()  # 单位化

    def __str__(self):
        return '[%s,\n %s,\n %s]' % (self.__point0, self.__point1, self.__point2)


if __name__ == '__main__':
    pt1 = Point3D(1, 1, 1)
    pt2 = Point3D(1, 2, 2)
    pt3 = Point3D(1, 2, 1)
    ttt = Plane(pt1, pt2, pt3)
    print(ttt.normVector())
