"""
三维空间点
"""
from CommonStruct import Point2D


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
        return '(%.4f, %.4f, %.4f)' % (self.__x, self.__y, self.__z)


if __name__ == "__main__":
    pass
