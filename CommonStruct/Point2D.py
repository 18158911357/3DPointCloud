"""
二维点
"""
import math


class Point2D:
    __slots__ = ('__x', '__y')

    def __init__(self, xx=0.0, xy=0.0):
        """
        初始化点坐标

        :param x: X坐标
        :param y: Y坐标
        """
        self.__x = xx
        self.__y = xy

    def __add__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.__x + other.x, self.__y + other.y)
        elif isinstance(other, int):
            return Point2D(self.__x + other, self.__y + other)
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.__x - other.x, self.__y - other.y)
        elif isinstance(other, int):
            return Point2D(self.__x - other, self.__y - other)
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, int) and other != 0:
            return Point2D(self.__x / other, self.__y / other)
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, int):
            return Point2D(self.__x * other, self.__y * other)
        else:
            return None

    def __eq__(self, other):
        return isinstance(other, Point2D) and self.__x == other.x and self.__y == other.y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, xx):
        self.__x = xx

    @y.setter
    def y(self, xy):
        self.__y = xy

    def norm(self):
        """
        计算点pt到原点的距离

        :return: 点到原点的距离
        """
        return math.sqrt(self.__x * self.__x + self.__y * self.__y)

    def __str__(self):
        return '[%.4f, %.4f]' % (self.__x, self.__y)
