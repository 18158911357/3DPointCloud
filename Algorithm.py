from numpy import *

from Commonstruct import *


def Rodrigues(_x):
    """
    罗德里格斯变换
    -x = [nx,ny,nz],\n
    [x,y,z]为单位向量，表示旋转轴,\n
    n表示旋转角度,\n
    计算旋转矩阵\n

    :return: 变换矩阵
    """
    theta = Vector3D.norm(_x)
    s = math.sin(theta)
    c = math.cos(theta)
    c1 = 1.0 - c
    if theta == 0:
        itheta = 0
    else:
        itheta = 1 / theta
    _x = _x * itheta
    ax = Vector3D.toArray(_x)

    rrt = array([[ax[0] * ax[0], ax[0] * ax[1], ax[0] * ax[2]],
                 [ax[1] * ax[0], ax[1] * ax[1], ax[1] * ax[2]],
                 [ax[2] * ax[0], ax[2] * ax[1], ax[2] * ax[2]]])
    r_x = array([[0, -ax[2], ax[1]],
                 [ax[2], 0, -ax[0]],
                 [-ax[1], ax[0], 0]])
    ae = eye(3)
    r = c * ae + c1 * rrt + s * r_x
    return r


def CoordinateMatrix(_axis, _theta):
    """
    坐标系变换：通过输入旋转轴与旋转角度，输出3D坐标系旋转的矩阵

    :param _axis: 旋转轴，可选为‘x,y,z’
    :param _theta: 旋转角度
    :return: 坐标系旋转矩阵
    """
    cTheta = cos(_theta)
    sTheta = sin(_theta)
    if _axis == 'x':
        return array([[1, 0, 0], [0, cTheta, sTheta], [0, -sTheta, cTheta]])
    elif _axis == 'y':
        return array([[cTheta, 0, -sTheta], [0, 1, 0], [sTheta, 0, cTheta]])
    elif _axis == 'z':
        return array([[cTheta, sTheta, 0], [-sTheta, cTheta, 0], [0, 0, 1]])
    else:
        return None


def RotateMatrix(_axis, _theta):
    """
    旋转矩阵：通过输入旋转轴与旋转角度，输出3D旋转的矩阵

    :param _axis: 旋转轴，可选为‘x,y,z’
    :param _theta: 旋转角度
    :return: 旋转矩阵
    """
    cTheta = cos(_theta)
    sTheta = sin(_theta)
    if _axis == 'x':
        return array([[1, 0, 0], [0, cTheta, -sTheta], [0, sTheta, cTheta]])
    elif _axis == 'y':
        return array([[cTheta, 0, sTheta], [0, 1, 0], [-sTheta, 0, cTheta]])
    elif _axis == 'z':
        return array([[cTheta, -sTheta, 0], [sTheta, cTheta, 0], [0, 0, 1]])
    else:
        return None


def GetLineEndPoints(xPointIn, xResultLine):
    """
    以集中的点、计算得到的2D线段，计算端点

    :param xPointIn:
    :param xResultLine:
    :return:
    """
    EndPoints = []
    if not xPointIn:
        return EndPoints
    nPtNum = len(xPointIn)
    if nPtNum < 2:
        return EndPoints
    # 获取XY坐标的最大值最小值
    tempPointIn = list(zip(*xPointIn))
    dXMax = max(tempPointIn[1])
    dXMin = min(tempPointIn[1])
    dYMax = max(tempPointIn[2])
    dYMin = min(tempPointIn[2])
    # 计算线段的两个端点
    # 这边进行判断考虑了直线的斜率趋近于0和趋近于无穷大的情况
    if abs(dXMax - dXMin) > abs(dYMax - dYMin):
        startX = dXMin
        endX = dXMax
        startY = -(xResultLine.a * startX + xResultLine.c) / xResultLine.b
        endY = -(xResultLine.a * endX + xResultLine.c) / xResultLine.b
    else:
        startY = dYMin
        endY = dYMax
        startX = -(xResultLine.b * startY + xResultLine.c) / xResultLine.a
        endX = -(xResultLine.b * endY + xResultLine.c) / xResultLine.a
    EndPoints = [[startX, startY], [endX, endY]]
    return EndPoints


def CalLine_Parall_Line(xPointsIn, xLineRef, xExcludeNum, xAverageNum, xDistMethod='Avg'):
    """
    根据参考线计算平行线

    :param xPointsIn: 点云
    :param xLineRef: 参考线
    :param xDistMethod: 计算平移量的方式
    :param xExcludeNum: 滤除点数
    :param xAverageNum: 平均点数
    :return:
    """
    nPtNum = len(xPointsIn)
    if nPtNum == 0:
        return None
    pointRef = xPointsIn[nPtNum / 2]
    # 计算所有点到参考直线的距离
    tempDist = Geom_Dist_Point_Line(pointRef, xLineRef)
    nSign = tempDist // abs(tempDist)
    nDist = []
    for x, i in enumerate(xPointsIn):
        assert isinstance(x, list)
        xPoint = Point3D(*x)
        nDist[i] = Geom_Dist_Point_Line(xPoint, xLineRef) * nSign
    if xDistMethod == 'Avg':
        nLineShift = average(nDist)
    else:
        if xDistMethod == 'Max':
            sort(nDist, reverse=True)
        else:
            sort(nDist)
        if xAverageNum == 0:
            xExcludeNum = 0
            xAverageNum = 1
        elif xExcludeNum + xAverageNum > nPtNum:
            xExcludeNum = 0
            xAverageNum = 1
        nLineShift = average(nDist[xExcludeNum:xExcludeNum + xAverageNum])
    a = xLineRef.a
    b = xLineRef.b
    c = xLineRef.c - nLineShift * nSign
    lineOut = Line2D(a, b, c)
    return lineOut


def Geom_Dist_Point_Line(xPoint, xLine):
    # Ax+By+C
    return xLine.a * xPoint.x + xLine.b * xPoint.y + xLine.c


def FitLineRobust():
    """
    鲁棒直线拟合

    :return:
    """
    pass


if __name__ == '__main__':
    pass
