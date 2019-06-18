from CommonStruct import Point3D


class Line3D:
    def __init__(self, xOrigin=Point3D(), xDirection=Point3D(1, 1, 0)):
        assert isinstance(xOrigin, Point3D) and isinstance(xDirection, Point3D)
        self.__origin = xOrigin
        self.__direction = xDirection

    @property
    def origin(self):
        return self.__origin

    @property
    def direction(self):
        return self.__direction

    @origin.setter
    def origin(self, xOrigin):
        self.__origin = xOrigin

    @direction.setter
    def direction(self, xDirection):
        self.__direction = xDirection

    def __str__(self):
        return 'origin:%s, direction:%s' % (self.origin, self.direction)


if __name__ == '__main__':
    testLine = Line3D()
    print(testLine)
