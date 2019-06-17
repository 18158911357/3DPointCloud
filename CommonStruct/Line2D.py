class Line2D:
    def __init__(self, xa, xb, xc):
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
