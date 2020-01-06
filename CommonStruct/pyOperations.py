import math


def crossMultiply(xPoint1, xPoint2):
    if isinstance(xPoint1, Point3D) and isinstance(xPoint2, Point3D):
        # 三维向量叉乘，求同时垂直于两个向量的向量
        tempX = xPoint1.y * xPoint2.z - xPoint1.z * xPoint2.y
        tempY = xPoint1.x * xPoint2.z - xPoint1.z * xPoint2.x
        tempZ = xPoint1.x * xPoint2.y - xPoint1.y * xPoint2.x
        return Point3D(tempX, tempY, tempZ)
    else:
        return None


def dotMultiply(xPoint1, xPoint2):
    if isinstance(xPoint1, Point3D) and isinstance(xPoint2, Point3D):
        # 三维向量点乘，可用于计算投影或者夹角
        return xPoint1.x * xPoint2.x + xPoint1.y * xPoint2.y + xPoint1.z * xPoint2.z
    else:
        return None


def angleOfVector(xPoint1, xPoint2):
    # 求两个向量的夹角
    theta = dotMultiply(xPoint1, xPoint2) / (xPoint1.norm() * xPoint2.norm())
    return math.acos(theta)


# def numMul(xNum: (int, float), xQuaternion: Quaternion):
#     # 数乘
#     assert isinstance(xNum, (int, float)) and isinstance(xQuaternion, Quaternion)
#     return Quaternion(xQuaternion.s * xNum, xQuaternion * xNum)
#
#
# def dotMul(xQuaternion: Quaternion, yQuaternion: Quaternion):
#     # 点乘
#     assert isinstance(xQuaternion, Quaternion) and isinstance(yQuaternion, Quaternion)
#     tempS = xQuaternion.s * yQuaternion.s
#     tempVx = xQuaternion.v.x * yQuaternion.v.x
#     tempVy = xQuaternion.v.y * yQuaternion.v.y
#     tempVz = xQuaternion.v.z * yQuaternion.v.z
#     return Quaternion(tempS, Point3D(tempVx, tempVy, tempVz))
#
#
# def Rotate(xPoint, xQuaternion):
#     # 用四元数表示旋转，计算结果为纯虚四元数，虚部的三个分量表示旋转后的3D点坐标
#     assert isinstance(xPoint, Point3D) and isinstance(xQuaternion, Quaternion)
#     xP = Quaternion(0, xPoint)
#     tempQuaternion = xQuaternion * xP * xQuaternion.inverseQuaternion()
#     if tempQuaternion.s == 0:
#         return tempQuaternion.v
#     else:
#         print('输入的四元数有误')
#         return None
#
#
# def matrixToQuaternion(xMatrix):
#     # 由矩阵到四元数的转换
#     assert isinstance(xMatrix, Matrix3D)
#     tempQ0 = (xMatrix.trace() + 1) ** 0.5 / 2
#     tempQ1 = (xMatrix[1][2] - xMatrix[2][1]) / (4 * tempQ0)
#     tempQ2 = (xMatrix[2][0] - xMatrix[0][2]) / (4 * tempQ0)
#     tempQ3 = (xMatrix[0][1] - xMatrix[1][0]) / (4 * tempQ0)
#     return Quaternion(tempQ0, Point3D(tempQ1, tempQ2, tempQ3))
#
#
# def quaternionToMatrix(xQuaternion):
#     # 由四元数到矩阵的转换
#     assert isinstance(xQuaternion, Quaternion)
#     tempQ0 = xQuaternion.s
#     tempQ1 = xQuaternion.v.x
#     tempQ2 = xQuaternion.v.y
#     tempQ3 = xQuaternion.v.z
#     R00 = 1 - 2 * tempQ2 ** 2 - 2 * tempQ3 ** 2
#     R01 = 2 * tempQ1 * tempQ2 + 2 * tempQ0 * tempQ3
#     R02 = 2 * tempQ1 * tempQ3 - 2 * tempQ0 * tempQ2
#     R10 = 2 * tempQ1 * tempQ2 - 2 * tempQ0 * tempQ3
#     R11 = 1 - 2 * tempQ1 ** 2 - 2 * tempQ3 ** 2
#     R12 = 2 * tempQ2 * tempQ3 + 2 * tempQ0 * tempQ1
#     R20 = 2 * tempQ1 * tempQ3 + 2 * tempQ0 * tempQ2
#     R21 = 2 * tempQ2 * tempQ3 - 2 * tempQ0 * tempQ1
#     R22 = 1 - 2 * tempQ1 ** 2 - 2 * tempQ2 ** 2
#     return Matrix3D([[R00, R01, R02], [R10, R11, R12], [R20, R21, R22]])


if __name__ == '__main__':
    from Geometric import Point3D
    pass

