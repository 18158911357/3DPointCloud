"""
用于仿真程序从stl中获取所需要的数据，根本思想为计算三角面片与激光的交点
引入噪声的概念，每个交点的z坐标都会加入噪声
"""
from CommonStruct.Geometric import *


def createLine():
    # 构造线激光的线
    xDirection = Point3D(0, 0, -1)
    xOrigin = []
    xLineList = []
    for i in range(200):
        xOrigin.append(Point3D(i * 0.5 - 50, 0, 0))
        xLineList.append(Line3D(xOrigin[i], xDirection))
    return xLineList


def moveLine(xLineList, Ydelta):
    for i in xLineList:
        assert isinstance(i, Line3D)
        i.origin.y = i.origin.y + Ydelta


def calcIntersection_LineAndTriangleSlice(xLine, xTriangleSlice):
    assert isinstance(xTriangleSlice, TriangleSlice) and isinstance(xLine, Line3D)
    xPlane = Plane(xTriangleSlice.vertex.vertex1, xTriangleSlice.facet)
    xInterSectionPoint = calcIntersection_LineAndPlane(xLine, xPlane)
    if xInterSectionPoint and xTriangleSlice.vertex.isInTriangle(xInterSectionPoint):
        return xInterSectionPoint
    else:
        return None


def calcIntersection_LineAndPlane(xLine, xPlane):
    assert isinstance(xPlane, Plane) and isinstance(xLine, Line3D)
    tm1 = xLine.origin.x
    tm2 = xLine.origin.y
    tm3 = xLine.origin.z
    tv1 = xLine.direction.x
    tv2 = xLine.direction.y
    tv3 = xLine.direction.z
    tn1 = xPlane.point0.x
    tn2 = xPlane.point0.y
    tn3 = xPlane.point0.z
    tvp1 = xPlane.normVector().x
    tvp2 = xPlane.normVector().y
    tvp3 = xPlane.normVector().z
    if (tvp1 * tv1 + tvp2 * tv2 + tvp3 * tv3) != 0:
        temp = (tvp1 * (tn1 - tm1) + tvp2 * (tn2 - tm2) + tvp3 * (tn3 - tm3)) / \
               (tvp1 * tv1 + tvp2 * tv2 + tvp3 * tv3)
        return Point3D(tm1 + tv1 * temp, tm2 + tv2 * temp, tm3 + tv3 * temp)
    else:
        return None


def readModel(xSTLModelPath):
    xSTLModel = STLModel.ReadSTL(xSTLModelPath)
    return xSTLModel


if __name__ == '__main__':
    tSTLPath = r'D:\STLModel.stl'
    tSTLModel = readModel(tSTLPath).listTri
    # iline = Line3D(Point3D(0, 0, 1), Point3D(0, 0, -1))
    tLineList = createLine()
    tPointList = []
    xxx = 0
    for iline in tLineList:
        for ti in range(1):
            for x in tSTLModel:
                interSectionPoint = calcIntersection_LineAndTriangleSlice(iline, x)
                if interSectionPoint:
                    tPointList.append(interSectionPoint)
            xxx += 1
            print(xxx)
    tPointPath = r'D:\get.txt'
    print('共%d个点' % len(tPointList))
    with open(tPointPath, 'w') as f:
        for ti in tPointList:
            print(ti, file=f)
