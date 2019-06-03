"""
二维点
"""
import math


class Point2D:
    __slots__ = ('_x', '_y')

    def __init__(self, x=0.0, y=0.0):
        """
        初始化点坐标

        :param x: X坐标
        :param y: Y坐标
        """
        self._x = x
        self._y = y

    def __add__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self._x + other.x, self._y + other.y)
        elif isinstance(other, int):
            return Point2D(self._x + other, self._y + other)
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self._x - other.x, self._y - other.y)
        elif isinstance(other, int):
            return Point2D(self._x - other, self._y - other)
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, int) and other != 0:
            return Point2D(self._x / other, self._y / other)
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, int):
            return Point2D(self._x * other, self._y * other)
        else:
            return None

    def __eq__(self, other):
        return isinstance(other, Point2D) and self._x == other.x and self._y == other.y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    @staticmethod
    def norm(pt):
        """
        计算点pt到原点的距离

        :param pt: 输入的点
        :return: 点到原点的距离
        """
        return math.sqrt(pt.x * pt.x + pt.y * pt.y + pt.z * pt.z)

    @staticmethod
    def toPoint(other):
        """
        输入list类型的实例，转化为Point3D类型的实例

        :param other: 1*3 list实例
        :return: Point3D类型的实例
        """
        if len(other) == 2:
            return Point2D(other[1], other[2])
        else:
            return None

    def __str__(self):
        return '[%.4f, %.4f]' % (self._x, self._y)
