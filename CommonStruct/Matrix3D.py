import numpy
from Line3D import *
from Point3D import *


class Matrix3D:
    def __init__(self, xList):
        assert isinstance(xList, list)
        self.__data = numpy.array(xList)

    def __len__(self):
        return self.__data.size

    def shape(self):
        return self.__data.shape

    def __getitem__(self, xItem):
        return self.__data[xItem]

    def __mul__(self, xOther):
        if isinstance(xOther, Point3D):
            # 矩阵左乘向量，点
            tempX = float(self.__data[0][0] * xOther.x + self.__data[0][1] * xOther.y + self.__data[0][2] * xOther.z)
            tempY = float(self.__data[1][0] * xOther.x + self.__data[1][1] * xOther.y + self.__data[1][2] * xOther.z)
            tempZ = float(self.__data[2][0] * xOther.x + self.__data[2][1] * xOther.y + self.__data[2][2] * xOther.z)
            return Point3D(tempX, tempY, tempZ)
        elif isinstance(xOther, Line3D):
            # 矩阵左乘3D直线
            tempOrigin = self * xOther.origin
            tempDirection = self * xOther.direction
            return Line3D(tempOrigin, tempDirection)
        elif isinstance(xOther, Matrix3D):
            # 矩阵相乘
            return self.__data * xOther.__data
        elif isinstance(xOther, (int, float)):
            return self.__data * xOther
        else:
            return None

    @staticmethod
    def eye():
        return Matrix3D([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    def T(self):
        return list(zip(*self.__data))

    def trace(self):
        # 求矩阵的迹
        pass

    def __str__(self):
        return str(self.__data)


# 相似变换(待实现)
# 仿射变换(待实现)
# 射影变换(待实现)


if __name__ == '__main__':
    pass
