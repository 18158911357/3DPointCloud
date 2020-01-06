from Point3D import *
from copy import deepcopy


class Line3D:
    def __init__(self, xOrigin=Point3D(0, 0, 0), xDirection=Point3D(1, 1, 0)):
        assert isinstance(xOrigin, Point3D) and isinstance(xDirection, Point3D)
        self.__origin = deepcopy(xOrigin)
        self.__direction = deepcopy(xDirection)

    @property
    def origin(self):
        return self.__origin

    @property
    def direction(self):
        return self.__direction

    @origin.setter
    def origin(self, xOrigin):
        self.__origin = deepcopy(xOrigin)

    @direction.setter
    def direction(self, xDirection):
        self.__direction = deepcopy(xDirection)

    def __str__(self):
        return 'origin:%s, direction:%s' % (self.origin, self.direction)


if __name__ == '__main__':
    tLine3D = Line3D()
    print(tLine3D)
