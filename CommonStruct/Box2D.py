from CommonStruct.Point2D import Point2D
from copy import deepcopy


class Box2D:
    def __init__(self, xMinPoint=Point2D(-1, -1), xMaxPoint=Point2D(1, 1)):
        """
        Box初始化，两个点构造一个与世界坐标系平行的Box
        :param xMaxPoint:
        :param xMinPoint:
        """
        assert isinstance(xMaxPoint, Point2D) and isinstance(xMinPoint, Point2D)
        self.__minPoint = xMinPoint
        self.__maxPoint = xMaxPoint

    def translate(self, xVector):
        """
        平移操作

        :param xVector: 平移向量
        :return:
        """
        if isinstance(xVector, Point2D):
            self.__maxPoint += xVector
            self.__minPoint += xVector

    def isEmpty(self):
        """
        判断Box是否为空

        :return:
        """
        return self.__maxPoint == self.__minPoint

    def centerPoint(self):
        """
        计算Box的中心点

        :return:
        """
        return (self.__maxPoint + self.__minPoint) / 2

    def area(self):
        # 面积
        return self.dimX() * self.dimY()

    def dimX(self):
        # 长
        return abs(self.__maxPoint.x - self.__minPoint.x)

    def dimY(self):
        # 宽
        return abs(self.__maxPoint.y - self.__minPoint.y)

    @property
    def maxPoint(self):
        return self.__maxPoint

    @property
    def minPoint(self):
        return self.__minPoint

    @minPoint.setter
    def minPoint(self, xMinPoint):
        self.__minPoint = xMinPoint

    @maxPoint.setter
    def maxPoint(self, xMaxPoint):
        self.__maxPoint = xMaxPoint

    def __str__(self):
        return 'minPoint:%s, maxPoint:%s' % (self.__minPoint, self.__minPoint)


if __name__ == '__main__':
    tBox = Box2D()
    print(tBox)
