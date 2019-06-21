import math
import numpy as np
import matplotlib.pyplot as plt


def lineFromPoints(point1, point2):
    k = (point2[1] - point1[1]) / (point2[0] - point1[0])
    b = - point1[0] * k + point1[1]
    return [k, b]


def distanceToLine(xPoint, xLine):
    temp1 = xLine[0] * xPoint[0] - xPoint[1] + xLine[1]
    temp2 = math.sqrt(xLine[0] * xLine[0] + 1)
    return temp1 / temp2


# 输出列表中在直线上方最远的点的下标
# 如果所有的点都在直线的下方，则输出-1
def getMaxPoint(xPointList, xline):
    tempDistance = []
    tempPointList = []
    for iPoint in xPointList:
        tempDis = distanceToLine(iPoint, xline)
        if tempDis < 0:
            tempDistance.append(tempDis)
            tempPointList.append(iPoint)
    if tempDistance:
        maxIndex = tempDistance.index(min(tempDistance))
        tempIndex = xPointList.index(tempPointList[maxIndex])
        return tempPointList[maxIndex], tempIndex
    else:
        return -1, -1


def listSplit(xList, xIndex):
    return xList[0:xIndex], xList[xIndex+1:]


def testWork(xStartPoint, xEndPoint, xPointList):
    beginLine = lineFromPoints(xStartPoint, xEndPoint)
    maxPoint, maxIndex = getMaxPoint(xPointList, beginLine)
    if maxIndex is not -1:
        subList1, subList2 = listSplit(xPointList, maxIndex)
        print(maxPoint)
        if len(subList1) > 0:
            subStartPoint = xStartPoint
            subEndPoint = xPointList[maxIndex]
            testWork(subStartPoint, subEndPoint, subList1)
        if len(subList2) > 0:
            subStartPoint = xPointList[maxIndex]
            subEndPoint = xEndPoint
            testWork(subStartPoint, subEndPoint, subList2)


# 定义起始点和终止点
startPoint = (-1, np.random.uniform(0, 1))
endPoint = (20, np.random.uniform(0, 1))

# 定义两点之间的随机边缘
x = list(range(20))
y = list(np.random.rand(20))
plt.scatter(*startPoint, color='black')
plt.scatter(*endPoint, color='black')
plt.scatter(x, y, c='r', marker='*')
plt.plot(x, y, 'b--')
plt.show()
allPoint = list(zip(x, y))
print('***********************************************')
testWork(startPoint, endPoint, allPoint)
