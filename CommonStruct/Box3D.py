from CommonStruct import Point3D
from copy import deepcopy


class Box3D:
    def __init__(self, xMaxPoint=Point3D(1, 1, 1), xMinPoint=Point3D(-1, -1, -1)):
        """
        Box初始化，两个点构造一个与世界坐标系平行的Box
        :param xMaxPoint:
        :param xMinPoint:
        """
        assert isinstance(xMaxPoint, Point3D) and isinstance(xMinPoint, Point3D)
        self.__maxPoint = deepcopy(xMaxPoint)
        self.__minPoint = deepcopy(xMinPoint)

    def translate(self, xVector):
        """
        平移操作

        :param xVector: 平移向量
        :return:
        """
        if isinstance(xVector, Point3D):
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

    def volumn(self):
        # 体积
        return self.dimX() * self.dimY() * self.dimZ()

    def dimX(self):
        # 长
        return abs(self.__maxPoint.x - self.__minPoint.x)

    def dimY(self):
        # 宽
        return abs(self.__maxPoint.y - self.__minPoint.y)

    def dimZ(self):
        # 高
        return abs(self.__maxPoint.z - self.__minPoint.z)

    @property
    def maxPoint(self):
        return self.__maxPoint

    @property
    def minPoint(self):
        return self.__minPoint

    @minPoint.setter
    def minPoint(self, xMinPoint):
        self.__minPoint = deepcopy(xMinPoint)

    @maxPoint.setter
    def maxPoint(self, xMaxPoint):
        self.__maxPoint = deepcopy(xMaxPoint)

    def __str__(self):
        return 'minPoint:%s, maxPoint:%s' % (self.__minPoint, self.__maxPoint)


if __name__ == '__main__':
    testBox = Box3D()
    print(testBox.minPoint)
