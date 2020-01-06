from copy import deepcopy
import math
from Matrix3D import *
from Point3D import *


# 四元数
class Quaternion:
    def __init__(self, xs, xv):
        assert isinstance(xs, (int, float))
        assert isinstance(xv, (Point3D,))
        self.__s = xs
        self.__v = deepcopy(xv)

    def __str__(self):
        tempStr = [self.__s, str(self.__v)]
        return str(tempStr)

    def __add__(self, other):
        assert isinstance(other, Quaternion)
        return Quaternion(self.__s + other.__s, self.__v + other.__v)

    def __sub__(self, other):
        assert isinstance(other, Quaternion)
        return Quaternion(self.__s - other.__s, self.__v - other.__v)

    def __mul__(self, other):
        assert isinstance(other, Quaternion)
        tempS = self.__s * other.__s - self.__v.x * other.__v.x - self.__v.y * other.__v.y - self.__v.z * other.__v.z
        tempVx = self.__s * other.__v.x + self.__v.x * other.__s + self.__v.y * other.__v.z - self.__v.z * other.__v.y
        tempVy = self.__s * other.__v.y - self.__v.x * other.__v.z + self.__v.y * other.__s + self.__v.z * other.__v.x
        tempVz = self.__s * other.__v.z + self.__v.x + other.__v.y - self.__v.y * other.__v.x + self.__v.z * other.__s
        return Quaternion(tempS, Point3D(tempVx, tempVy, tempVz))

    def conjugateQuaternion(self):
        # 共轭四元数
        tempS = self.__s
        tempVx = -self.__v.x
        tempVy = -self.__v.y
        tempVz = -self.__v.z
        return Quaternion(tempS, Point3D(tempVx, tempVy, tempVz))

    def norm(self):
        # 模
        return (self.__s ** 2 + self.__v.x ** 2 + self.__v.y ** 2 + self.__v.z ** 2) ** 0.5

    def inverseQuaternion(self):
        # 四元数的逆
        tempNorm = self.norm()
        tempS = self.__s / tempNorm
        tempV = self.__v / tempNorm
        return Quaternion(tempS, tempV)

    def rotatePrint(self):
        # 打印四元数对应的旋转角度与旋转轴
        xTheta = 2 * math.acos(self.__s)
        xAxis = self.__v / math.sin(xTheta / 2)
        print('旋转角度为：', xTheta, end=' ')
        print('旋转轴为：', xAxis)

    @property
    def s(self):
        return self.__s

    @property
    def v(self):
        return self.__v

    @s.setter
    def s(self, xS):
        self.__s = xS

    @v.setter
    def v(self, xV):
        self.__v = xV


def numMul(xNum: (int, float), xQuaternion: Quaternion):
    # 数乘
    assert isinstance(xNum, (int, float)) and isinstance(xQuaternion, Quaternion)
    return Quaternion(xQuaternion.s * xNum, xQuaternion * xNum)


def dotMul(xQuaternion: Quaternion, yQuaternion: Quaternion):
    # 点乘
    assert isinstance(xQuaternion, Quaternion) and isinstance(yQuaternion, Quaternion)
    tempS = xQuaternion.s * yQuaternion.s
    tempVx = xQuaternion.v.x * yQuaternion.v.x
    tempVy = xQuaternion.v.y * yQuaternion.v.y
    tempVz = xQuaternion.v.z * yQuaternion.v.z
    return Quaternion(tempS, Point3D(tempVx, tempVy, tempVz))


def Rotate(xPoint, xQuaternion):
    # 用四元数表示旋转，计算结果为纯虚四元数，虚部的三个分量表示旋转后的3D点坐标
    assert isinstance(xPoint, Point3D) and isinstance(xQuaternion, Quaternion)
    xP = Quaternion(0, xPoint)
    tempQuaternion = xQuaternion * xP * xQuaternion.inverseQuaternion()
    if tempQuaternion.s == 0:
        return tempQuaternion.v
    else:
        print('输入的四元数有误')
        return None


def matrixToQuaternion(xMatrix):
    # 由矩阵到四元数的转换
    assert isinstance(xMatrix, Matrix3D)
    tempQ0 = (xMatrix.trace() + 1) ** 0.5 / 2
    tempQ1 = (xMatrix[1][2] - xMatrix[2][1]) / (4 * tempQ0)
    tempQ2 = (xMatrix[2][0] - xMatrix[0][2]) / (4 * tempQ0)
    tempQ3 = (xMatrix[0][1] - xMatrix[1][0]) / (4 * tempQ0)
    return Quaternion(tempQ0, Point3D(tempQ1, tempQ2, tempQ3))


def quaternionToMatrix(xQuaternion):
    # 由四元数到矩阵的转换
    assert isinstance(xQuaternion, Quaternion)
    tempQ0 = xQuaternion.s
    tempQ1 = xQuaternion.v.x
    tempQ2 = xQuaternion.v.y
    tempQ3 = xQuaternion.v.z
    R00 = 1 - 2 * tempQ2 ** 2 - 2 * tempQ3 ** 2
    R01 = 2 * tempQ1 * tempQ2 + 2 * tempQ0 * tempQ3
    R02 = 2 * tempQ1 * tempQ3 - 2 * tempQ0 * tempQ2
    R10 = 2 * tempQ1 * tempQ2 - 2 * tempQ0 * tempQ3
    R11 = 1 - 2 * tempQ1 ** 2 - 2 * tempQ3 ** 2
    R12 = 2 * tempQ2 * tempQ3 + 2 * tempQ0 * tempQ1
    R20 = 2 * tempQ1 * tempQ3 + 2 * tempQ0 * tempQ2
    R21 = 2 * tempQ2 * tempQ3 - 2 * tempQ0 * tempQ1
    R22 = 1 - 2 * tempQ1 ** 2 - 2 * tempQ2 ** 2
    return Matrix3D([[R00, R01, R02], [R10, R11, R12], [R20, R21, R22]])


if __name__ == '__main__':
    testQuaternion = Quaternion(1, Point3D(1, 2, 3))
    print(testQuaternion)
