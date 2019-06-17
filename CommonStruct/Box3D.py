"""
Box结构体
"""
from CommonStruct import Point3D


class Box3D:

    def __init__(self, xMaxPoint=Point3D(1, 1, 1), xMinPoint=Point3D(-1, -1, -1)):
        """

        Box初始化，两个点构造一个与世界坐标系平行的Box
        :param xMaxPoint:
        :param xMinPoint:
        """
        assert isinstance(xMaxPoint, Point3D) and isinstance(xMinPoint, Point3D)
        self.__maxPoint = xMaxPoint
        self.__minPoint = xMinPoint

    def translate(self, vector):
        """
        平移操作

        :param vector: 平移向量
        :return:
        """
        if isinstance(vector, Point3D):
            self.__maxPoint += vector
            self.__minPoint += vector

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
        return self.dimX() * self.dimY() * self.dimY()

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
    def minPoint(self, minPoint):
        self.__minPoint = minPoint

    @maxPoint.setter
    def maxPoint(self, maxPoint):
        self.__maxPoint = maxPoint

    def __str__(self):
        return 'minPoint:%s, maxPoint:%s' % (self.__minPoint, self.__maxPoint)


if __name__ == '__main__':
    tBox = Box3D()
    print(tBox)
