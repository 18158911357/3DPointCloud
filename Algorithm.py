import math
from CommonStruct.Geometric import *

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
    # ax = Point3D.toArray(xVector)

    rrt = xVector * xVector
    r_x = Matrix3D([[0, -xVector.z, xVector.y],
                    [xVector.z, 0, -xVector.x],
                    [-xVector.y, xVector.x, 0]])
    ae = Matrix3D.eye()
    r = ae * c + r_x * s + rrt * c1
    return r
    pass


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


def CalLineParallLine(xPointsIn, xLineRef, xExcludeNum, xAverageNum, xDistMethod='Avg'):
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


def CalLinePerpendLine(xPointsIn, xLineRef, xPointRef, xExcludeNum, xAverageNum, xDistMethod='Avg'):
    """
    计算垂线，本质是改变参考线的方向，然后计算平行线

    :param xPointsIn:
    :param xLineRef:
    :param xPointRef:
    :param xExcludeNum:
    :param xAverageNum:
    :param xDistMethod:
    :return:
    """
    tempLineRefParall = Line2D()
    tempLineRefParall.a = -xLineRef.b
    tempLineRefParall.b = xLineRef.a
    tempLineRefParall.c = -xLineRef.a * xPointRef.x - xLineRef.b * xPointRef.y
    CalLineParallLine(xPointsIn, tempLineRefParall, xExcludeNum, xAverageNum, xDistMethod)


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
    lineDirection = pyOperations.crossMultiply(xVector1, xVector2)
    lineDirection = lineDirection / lineDirection.norm()
    # 必须考虑平面与坐标系接近平行的情况，不然可能使直线无限长
    xPoint1 = xPlane1.point0
    xPoint2 = xPlane2.point0
    xD1 = -pyOperations.dotMultiply(xVector1, xPoint1)
    xD2 = -pyOperations.dotMultiply(xVector2, xPoint2)
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


def isPoint2DInPolygon(xPoint, xVertices):
    """
        判断点是否在多边形内部
        1. 被测点是否在两个相邻点纵坐标范围内
        2. 被测点是否在i，j两点的连线之下
        3. 取反：以被测点为起点，作一条平行于x轴的射线，看该射线与多边形相交的点数
            取反的次数即为射线与多边形的交点
                若相交的点数为奇数，则表示点在多边形内部
                若相交的点为偶数，则表示点在多边形外部

    :param xPoint:
    :param xVertices:
    :return:
    """
    assert isinstance(xPoint, Point2D) and isinstance(xVertices, list)
    bRet = False
    j = len(xVertices) - 1
    for i in range(len(xVertices)):
        if ((xVertices[i].y < xPoint.y) and (xVertices[j].y >= xPoint.y)) \
                or ((xVertices[i].y >= xPoint.y) and (xVertices[j].y < xPoint.y)):
            if xVertices[i].x + (xPoint.y - xVertices[i].y) / (xVertices[j].y - xVertices[i].y) * (
                    xVertices[j].x - xVertices[i].x) < xPoint.x:
                bRet = not bRet
        j = i
    return bRet


def isPoint3DInPolygon(xPoint, xProjectPlane, xVectics):
    """
    判断点是否在3D多边形内（注意3D多边形与多面体的区别），点在坐标平面上
    实际上是先将3D多边形投影到坐标平面上，然后判断点是否在2D多边形内

    :param xPoint:
    :param xProjectPlane:
    :param xVectics:
    :return:
    """
    bRet = False
    j = len(xVectics) - 1
    tempVectics = []
    if xProjectPlane == 'XY':
        for x in xVectics:
            tempVectics.append(Point3D(x.x, x.y))
    elif xProjectPlane == 'XZ':
        for x in xVectics:
            tempVectics.append(Point3D(x.x, x.z))
    elif xProjectPlane == 'YZ':
        for x in xVectics:
            tempVectics.append(Point3D(x.y, x.z))
    else:
        pass
    for i in range(len(tempVectics)):
        if ((tempVectics[i].y < xPoint.y) and (tempVectics[j].y >= xPoint.y)) \
                or ((tempVectics[i].y >= xPoint.y) and (tempVectics[j].y < xPoint.y)):
            if tempVectics[i].x + (xPoint.y - tempVectics[i].y) / (tempVectics[j].y - tempVectics[i].y) * (
                    tempVectics[j].x - tempVectics[i].x) < xPoint.x:
                bRet = not bRet
        j = i
    return bRet


if __name__ == '__main__':
    ttt = RotateMatrix('x', math.pi / 2)
    print(ttt)
