import math
from Point3D import *


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


if __name__ == '__main__':
    pass

