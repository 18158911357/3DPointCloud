import numpy
from CommonStruct import Line3D, Point3D


class Matrix3D:
    def __init__(self, xList):
        assert isinstance(xList, list)
        self.__Data = numpy.array(xList)

    def __len__(self):
        return self.__Data.size

    def shape(self):
        return self.__Data.shape

    def __getitem__(self, xItem):
        return self.__Data[xItem]

    def __mul__(self, xOther):
        if isinstance(xOther, Point3D):
            # 矩阵左乘向量，点
            tempX = float(self.__Data[0][0] * xOther.x + self.__Data[0][1] * xOther.y + self.__Data[0][2] * xOther.z)
            tempY = float(self.__Data[1][0] * xOther.x + self.__Data[1][1] * xOther.y + self.__Data[1][2] * xOther.z)
            tempZ = float(self.__Data[2][0] * xOther.x + self.__Data[2][1] * xOther.y + self.__Data[2][2] * xOther.z)
            return Point3D(tempX, tempY, tempZ)
        elif isinstance(xOther, Line3D):
            # 矩阵左乘3D直线
            tempOrigin = self * xOther.origin
            tempDirection = self * xOther.direction
            return Line3D(tempOrigin, tempDirection)
        elif isinstance(xOther, Matrix3D):
            # 矩阵相乘
            temp
        else:
            return None

    def __str__(self):
        return str(self.__Data)


if __name__ == '__main__':
    testList = [[1, 0, 0],
                [0, 0, -1],
                [0, 1, 0]]
    testMatrix = Matrix3D(testList)
    testList = [[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]
    print(testMatrix)
    testPoint = Point3D(0, 0, 2)
    resultPoint = testMatrix * testPoint
    print(resultPoint)
