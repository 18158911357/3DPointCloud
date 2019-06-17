"""
三维空间点
"""
import math, numpy

from CommonStruct import Point2D


class Point3D:
    __slots__ = ('__x', '__y', '__z')

    def __init__(self, x=0.0, y=0.0, z=0.0):
        """
        初始化点坐标

        :param x: X坐标
        :param y: Y坐标
        :param z: Z坐标
        """
        self.__x = x
        self.__y = y
        self.__z = z

    def __add__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
        elif isinstance(other, (int, float)):
            return Point3D(self.__x + other, self.__y + other, self.__z + other)
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
        elif isinstance(other, (int, float)):
            return Point3D(self.__x - other, self.__y - other, self.__z - other)
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            return Point3D(self.__x / other, self.__y / other, self.__z / other)
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Point3D(self.__x * other, self.__y * other, self.__z * other)
        else:
            return None

    def __eq__(self, other):
        return isinstance(other, Point3D) and self.__x == other.x and self.__y == other.y and self.__z == other.z

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
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    @z.setter
    def z(self, z):
        self.__z = z

    def norm(self):
        """
        计算点pt到原点的距离

        :return:
        """
        return math.sqrt(self.__x * self.__x + self.__y * self.__y + self.__z * self.__z)

    def projectionXY(self):
        return Point2D(self.x, self.y)

    @staticmethod
    def crossMultiply(point1, point2):
        """
        向量叉乘(向量积、外积)

        :param point1:
        :param point2:
        :return:
        """
        tempX = point1.y * point2.z - point1.z * point2.y
        tempY = point1.x * point2.z - point1.z * point2.x
        tempZ = point1.x * point2.y - point1.y * point2.x
        return Point3D(tempX, tempY, tempZ)

    @staticmethod
    def dotMultiply(point1, point2):
        """
        向量点乘(数量积、内积)

        :param point1:
        :param point2:
        :return:
        """
        return point1.x * point2.x + point1.y * point2.y + point1.z * point2.z

    def __str__(self):
        return '(%.4f, %.4f, %.4f)' % (self.__x, self.__y, self.__z)


if __name__ == "__main__":
    pass
