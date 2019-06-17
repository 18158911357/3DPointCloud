from CommonStruct import Point3D
import numpy


class Line3D:
    def __init__(self, origin=Point3D(), direction=Point3D(1, 0, 0)):
        assert isinstance(origin, Point3D) and isinstance(direction, Point3D)
        self.__origin = origin
        self.__direction = direction

    @property
    def origin(self):
        return self.__origin

    @property
    def direction(self):
        return self.__direction

    @origin.setter
    def origin(self, origin):
        self.__origin = origin

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    def lineRotate(self, other):
        """
        用于计算直线的旋转，直线包含起始点与方向向量，旋转矩阵同时作用于点与向量，输出一个新的直线

        :param other:
        :return:
        """
        if isinstance(other, (numpy.ndarray, numpy.mat)):
            oriArray = numpy.array(self.origin.toList())
            dirArray = numpy.array(self.direction.toList())
            oriArray = numpy.dot(other, oriArray).tolist()
            dirArray = numpy.dot(other, dirArray).tolist()
            return Line3D(Point3D(*oriArray), Point3D(*dirArray))
        else:
            return None

    def __str__(self):
        return '[%.4f, %.4f, %.4f],[%.4f, %.4f, %.4f]' % (self.origin.x, self.origin.y, self.origin.z,
                                                          self.direction.x, self.direction.y, self.direction.z)
