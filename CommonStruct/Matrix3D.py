import numpy
from CommonStruct import Line3D, Point3D


class Matrix3D:
    def __init__(self, xList):
        assert isinstance(xList, list)
        self.data = numpy.array(xList)

    def __len__(self):
        return self.data.size

    def shape(self):
        return self.data.shape

    def __getitem__(self, xItem):
        sample = self.data[xItem]
        return sample

    def __mul__(self, xOther):
        if isinstance(xOther, Point3D):
            # 矩阵左乘向量，点
            tempX = float(self.data[0][0] * xOther.x + self.data[0][1] * xOther.y + self.data[0][2] * xOther.z)
            tempY = float(self.data[1][0] * xOther.x + self.data[1][1] * xOther.y + self.data[1][2] * xOther.z)
            tempZ = float(self.data[2][0] * xOther.x + self.data[2][1] * xOther.y + self.data[2][2] * xOther.z)
            return Point3D(tempX, tempY, tempZ)
        elif isinstance(xOther, Line3D):
            # 矩阵左乘3D直线
            tempOrigin = self * xOther.origin
            tempDirection = self * xOther.direction
            return Line3D(tempOrigin, tempDirection)
        else:
            return None

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    testList = [[1.000000e+00, 0.000000e+00, 0.000000e+00],
                [0.000000e+00, 6.123234e-17, -1.000000e+00],
                [0.000000e+00, 1.000000e+00, 6.123234e-17]]
    testMatrix = Matrix3D(testList)
    testPoint = Point3D(0, 0, 2)
    resultPoint = testMatrix * testPoint
    print(resultPoint)
