from copy import deepcopy

from CommonStruct.Point3D import Point3D


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


if __name__ == '__main__':
    testQuaternion = Quaternion(1, Point3D(1, 2, 3))
    print(testQuaternion)
