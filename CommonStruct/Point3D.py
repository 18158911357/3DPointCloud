from Point2D import *
from Matrix3D import *


class Point3D:
    def __init__(self, xx=0.0, xy=0.0, xz=0.0):
        """
        初始化点坐标
        """
        assert isinstance(xx, (int, float)) and isinstance(xy, (int, float)) and isinstance(xz, (int, float))
        self.__x = xx
        self.__y = xy
        self.__z = xz

    def __add__(self, xOther):
        if isinstance(xOther, Point3D):
            return Point3D(self.__x + xOther.x, self.__y + xOther.y, self.__z + xOther.z)
        elif isinstance(xOther, (int, float)):
            return Point3D(self.__x + xOther, self.__y + xOther, self.__z + xOther)
        else:
            return None

    def __sub__(self, xOther):
        if isinstance(xOther, Point3D):
            return Point3D(self.__x - xOther.x, self.__y - xOther.y, self.__z - xOther.z)
        elif isinstance(xOther, (int, float)):
            return Point3D(self.__x - xOther, self.__y - xOther, self.__z - xOther)
        else:
            return None

    def __truediv__(self, xOther):
        if isinstance(xOther, (int, float)) and xOther != 0:
            return Point3D(self.__x / xOther, self.__y / xOther, self.__z / xOther)
        else:
            return None

    def __mul__(self, xOther):
        if isinstance(xOther, (int, float)):
            return Point3D(self.__x * xOther, self.__y * xOther, self.__z * xOther)
        elif isinstance(xOther, Point3D):
            # 将Point3D相乘理解为1*3的矩阵相乘，列向量乘以行向量
            temp1 = [self.x * xOther.x, self.x * xOther.y, self.x * xOther.z]
            temp2 = [self.y * xOther.x, self.y * xOther.y, self.y * xOther.z]
            temp3 = [self.z * xOther.x, self.z * xOther.y, self.z * xOther.z]
            tempList = [temp1, temp2, temp3]
            return Matrix3D(tempList)
        else:
            return None

    def __eq__(self, xOther):
        return isinstance(xOther, Point3D) and self.__x == xOther.x and self.__y == xOther.y and self.__z == xOther.z

    def toList(self):
        return [self.__x, self.__y, self.__z]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def x(self, xx):
        self.__x = xx

    @y.setter
    def y(self, xy):
        self.__y = xy

    @z.setter
    def z(self, xz):
        self.__z = xz

    def norm(self):
        """
        计算点pt到原点的距离
        """
        return (self.__x * self.__x + self.__y * self.__y + self.__z * self.__z) ** 0.5

    def projectionXY(self):
        return Point2D(self.x, self.y)

    def __str__(self):
        return '(%s, %s, %s)' % (self.__x, self.__y, self.__z)


if __name__ == "__main__":
    testPoint1 = Point3D(1, 1, 1)
    testPoint2 = Point3D(2, 2, 2)
    print(testPoint1 * testPoint2)

