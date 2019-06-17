from Commonstruct.Point3D import Point3D
from copy import deepcopy


class Plane:
    def __init__(self, *args):
        if len(args) == 2:  # 点法式构造
            xPoint, xVector = args
            self.point0 = xPoint
            if xVector.z == 0:
                self.point1 = deepcopy(self.point0)
                self.point1.z += 1
                self.point2 = Point3D(0, 0, 0)
                self.point2.x = self.point0.x - (self.point1.z - self.point0.z) * xVector.y
                self.point2.y = self.point0.y + (self.point1.z - self.point0.z) * xVector.x
                self.point2.z = self.point0.z + (self.point1.x - self.point0.x) * xVector.y - \
                                (self.point1.y - self.point0.y) * xVector.x
            else:
                temp = xVector.x * xPoint.x + xVector.y * xPoint.y + xVector.z * xPoint.z
                self.point1 = Point3D(xPoint.x, xPoint.y + 1, 0)
                self.point2 = Point3D(xPoint.x + 1, xPoint.y, 0)
                self.point1.z = (temp - xVector.x * self.point1.x - xVector.y * self.point1.y) / xVector.z
                self.point2.z = (temp - xVector.x * self.point2.x - xVector.y * self.point2.y) / xVector.z
        elif len(args) == 3:  # 三点式构造
            self.point0 = args[0]
            self.point1 = args[1]
            self.point2 = args[2]
        else:
            self.point0 = None
            self.point1 = None
            self.point2 = None

    def normVector(self):
        """
        返回平面的法向量
        :return:
        """
        vector1 = self.point1 - self.point0
        vector1 = self.point2 - self.point0
        return vector1

    def __str__(self):
        return '[%s,\n %s,\n %s]' % (self.point0, self.point1, self.point2)


if __name__ == '__main__':
    pt1 = Point3D(1, 1, 1)
    pt2 = Point3D(1, 0, 0)
    ttt = Plane(pt1, pt2)
    print(ttt)
