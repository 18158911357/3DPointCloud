class Line2D:
    def __init__(self, xa=1, xb=1, xc=0):
        """
        ax + by + c = 0

        :param xa:
        :param xb:
        :param xc:
        """
        assert isinstance(xa, (int, float)) and isinstance(xb, (int, float)) and isinstance(xc, (int, float))
        self.__a = xa
        self.__b = xb
        self.__c = xc

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @a.setter
    def a(self, xa):
        self.__a = xa

    @b.setter
    def b(self, xb):
        self.__b = xb

    @c.setter
    def c(self, xc):
        self.__c = xc

    def __str__(self):
        return 'Line2D:(%s, %s, %s)' % (self.__a, self.__b, self.__c)


if __name__ == '__main__':
    testLine = Line2D()
    print(testLine)
