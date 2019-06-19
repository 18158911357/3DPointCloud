from CommonStruct import *

EPSILONS = 1e-5


def average(xNumList):
    return sum(xNumList) / len(xNumList)


def Rodrigues(xVector):
    """
    罗德里格斯变换
    -x = [nx,ny,nz],\n
    [x,y,z]为单位向量，表示旋转轴,\n
    n表示旋转角度,\n
    计算旋转矩阵\n

    :return: 变换矩阵
    """
    assert isinstance(xVector, Point3D)
    theta = xVector.norm()
    s = math.sin(theta)
    c = math.cos(theta)
    c1 = 1.0 - c
    if theta == 0:
        itheta = 0
    else:
        itheta = 1 / theta
    xVector = xVector * itheta
    ax = Point3D.toArray(xVector)

    rrt = Matrix3D([[ax[0] * ax[0], ax[0] * ax[1], ax[0] * ax[2]],
                    [ax[1] * ax[0], ax[1] * ax[1], ax[1] * ax[2]],
                    [ax[2] * ax[0], ax[2] * ax[1], ax[2] * ax[2]]])
    r_x = Matrix3D([[0, -ax[2], ax[1]],
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
    cTheta = math.cos(_theta)
    sTheta = math.sin(_theta)
    if _axis == 'x':
        return Matrix3D([[1, 0, 0], [0, cTheta, sTheta], [0, -sTheta, cTheta]])
    elif _axis == 'y':
        return Matrix3D([[cTheta, 0, -sTheta], [0, 1, 0], [sTheta, 0, cTheta]])
    elif _axis == 'z':
        return Matrix3D([[cTheta, sTheta, 0], [-sTheta, cTheta, 0], [0, 0, 1]])
    else:
        return None


def RotateMatrix(_axis, _theta):
    """
    旋转矩阵：通过输入旋转轴与旋转角度，输出3D旋转的矩阵

    :param _axis: 旋转轴，可选为‘x,y,z’
    :param _theta: 旋转角度
    :return: 旋转矩阵
    """
    cTheta = math.cos(_theta)
    sTheta = math.sin(_theta)
    if _axis == 'x':
        return Matrix3D([[1, 0, 0], [0, cTheta, -sTheta], [0, sTheta, cTheta]])
    elif _axis == 'y':
        return Matrix3D([[cTheta, 0, sTheta], [0, 1, 0], [-sTheta, 0, cTheta]])
    elif _axis == 'z':
        return Matrix3D([[cTheta, -sTheta, 0], [sTheta, cTheta, 0], [0, 0, 1]])
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
    dXMax = max(tempPointIn[0])
    dXMin = min(tempPointIn[0])
    dYMax = max(tempPointIn[1])
    dYMin = min(tempPointIn[1])
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
            sorted(nDist, reverse=True)
        else:
            sorted(nDist)
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


def Find2DBox(xPointsIn):
    """
    计算可以包含xPointIn的最小矩阵(2D)

    :param xPointsIn:
    :return:
    """
    tempPoints = list(zip(*xPointsIn))
    dXMax = max(tempPoints[0])
    dXMin = min(tempPoints[0])
    dYMax = max(tempPoints[1])
    dYMin = min(tempPoints[1])
    maxPoint = Point2D(dXMax, dYMax)
    minPoint = Point2D(dXMin, dYMin)
    min2DBox = Box2D(minPoint, maxPoint)
    return min2DBox


def Find3DBox(xPointsIn):
    """
    计算可以包含xPointIn的最小长方体(3D)

    :param xPointsIn:
    :return:
    """
    tempPoints = list(zip(*xPointsIn))
    dXMax = max(tempPoints[0])
    dXMin = min(tempPoints[0])
    dYMax = max(tempPoints[1])
    dYMin = min(tempPoints[1])
    dZMax = max(tempPoints[2])
    dZMin = min(tempPoints[2])
    maxPoint = Point3D(dXMax, dYMax, dZMax)
    minPoint = Point3D(dXMin, dYMin, dZMin)
    min3DBox = Box3D(minPoint, maxPoint)
    return min3DBox


def IntersectionLine(xPlane1, xPlane2):
    """
    求取两个平面的交线

    :param xPlane1:
    :param xPlane2:
    :return:
    """
    assert isinstance(xPlane1, Plane) and isinstance(xPlane2, Plane)
    xVector1 = xPlane1.normVector()
    xVector2 = xPlane2.normVector()
    tempDelta = xVector2 - xVector1
    if abs(tempDelta.x) < EPSILONS and abs(tempDelta.y) < EPSILONS and abs(tempDelta.z) < EPSILONS:
        return None
    lineDirection = crossMultiply(xVector1, xVector2)
    lineDirection = lineDirection / lineDirection.norm()
    # 必须考虑平面与坐标系接近平行的情况，不然可能使直线无限长
    xPoint1 = xPlane1.point0
    xPoint2 = xPlane2.point0
    xD1 = -dotMultiply(xVector1, xPoint1)
    xD2 = -dotMultiply(xVector2, xPoint2)
    maxAxis = max([lineDirection.x, lineDirection.y, lineDirection.z])
    if maxAxis == lineDirection.x:  # 偏向于X轴
        xA1, xA2, xB1, xB2 = xVector1.y, xVector2.y, xVector1.z, xVector2.z
        tempX = 0
        tempY = (xB1 * xD2 - xB2 * xD1) / (xA1 * xB2 - xA2 * xB1)
        tempZ = (xA2 * xD1 - xA1 * xD2) / (xA1 * xB2 - xA2 * xB1)
        startPoint = Point3D(tempX, tempY, tempZ)
        tempX = 100
        xD1 = xD1 + xVector1.x * tempX
        xD2 = xD2 + xVector2.x * tempX
        tempY = (xB1 * xD2 - xB2 * xD1) / (xA1 * xB2 - xA2 * xB1)
        tempZ = (xA2 * xD1 - xA1 * xD2) / (xA1 * xB2 - xA2 * xB1)
        endPoint = Point3D(tempX, tempY, tempZ)
    elif maxAxis == lineDirection.y:  # 偏向于y轴
        xA1, xA2, xB1, xB2 = xVector1.x, xVector2.x, xVector1.z, xVector2.z
        tempY = 0
        tempX = (xB1 * xD2 - xB2 * xD1) / (xA1 * xB2 - xA2 * xB1)
        tempZ = (xA2 * xD1 - xA1 * xD2) / (xA1 * xB2 - xA2 * xB1)
        startPoint = Point3D(tempX, tempY, tempZ)
        tempY = 100
        xD1 = xD1 + xVector1.y * tempY
        xD2 = xD2 + xVector2.y * tempY
        tempX = (xB1 * xD2 - xB2 * xD1) / (xA1 * xB2 - xA2 * xB1)
        tempZ = (xA2 * xD1 - xA1 * xD2) / (xA1 * xB2 - xA2 * xB1)
        endPoint = Point3D(tempX, tempY, tempZ)
    else:  # 偏向于z轴
        xA1, xA2, xB1, xB2 = xVector1.x, xVector2.x, xVector1.y, xVector2.y
        tempZ = 0
        tempX = (xB1 * xD2 - xB2 * xD1) / (xA1 * xB2 - xA2 * xB1)
        tempY = (xA2 * xD1 - xA1 * xD2) / (xA1 * xB2 - xA2 * xB1)
        startPoint = Point3D(tempX, tempY, tempZ)
        tempZ = 100
        xD1 = xD1 + xVector1.z * tempZ
        xD2 = xD2 + xVector2.z * tempZ
        tempX = (xB1 * xD2 - xB2 * xD1) / (xA1 * xB2 - xA2 * xB1)
        tempY = (xA2 * xD1 - xA1 * xD2) / (xA1 * xB2 - xA2 * xB1)
        endPoint = Point3D(tempX, tempY, tempZ)
    # 返回直线的方向，起始点，终止点
    return lineDirection, startPoint, endPoint


if __name__ == '__main__':
    ttt = RotateMatrix('x', math.pi / 2)
    print(ttt)
