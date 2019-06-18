class Point2D:
    def __init__(self, xx=0.0, xy=0.0):
        """
        初始化点坐标

        :param xx: X坐标
        :param xy: Y坐标
        """
        self.__x = xx
        self.__y = xy

    def __add__(self, xOther):
        if isinstance(xOther, Point2D):
            return Point2D(self.__x + xOther.x, self.__y + xOther.y)
        elif isinstance(xOther, (int, float)):
            return Point2D(self.__x + xOther, self.__y + xOther)
        else:
            return None

    def __sub__(self, xOther):
        if isinstance(xOther, Point2D):
            return Point2D(self.__x - xOther.x, self.__y - xOther.y)
        elif isinstance(xOther, (int, float)):
            return Point2D(self.__x - xOther, self.__y - xOther)
        else:
            return None

    def __truediv__(self, xOther):
        if isinstance(xOther, (int, float)) and xOther != 0:
            return Point2D(self.__x / xOther, self.__y / xOther)
        else:
            return None

    def __mul__(self, xOther):
        if isinstance(xOther, (int, float)):
            return Point2D(self.__x * xOther, self.__y * xOther)
        else:
            return None

    def __eq__(self, xOther):
        return isinstance(xOther, Point2D) and self.__x == xOther.x and self.__y == xOther.y

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
        return (self.__x * self.__x + self.__y * self.__y) ** 0.5

    def tolist(self):
        return [self.x, self.y]

    def __str__(self):
        return '[%.4f, %.4f]' % (self.__x, self.__y)


if __name__ == '__main__':
    testPoint = Point2D()
    print(testPoint)
