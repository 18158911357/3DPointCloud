"""
Box结构体
"""
from Commonstruct import Point3D


class Box3D:

    def __init__(self, maxPoint=Point3D(1, 1, 1), minPoint=Point3D(-1, -1, -1)):
        """

        Box初始化，两个点构造一个与世界坐标系平行的Box
        :param maxPoint:
        :param minPoint:
        """
        if isinstance(maxPoint, Point3D) and isinstance(minPoint, Point3D):
            self._maxPoint = maxPoint
            self._minPoint = minPoint
        else:
            self._maxPoint = None
            self._minPoint = None

    def translate(self, vector):
        """
        平移操作

        :param vector: 平移向量
        :return:
        """
        if isinstance(vector, Point3D):
            self._maxPoint += vector
            self._minPoint += vector

    def isNULL(self):
        """
        判断Box是否有效

        :return:
        """
        return self._minPoint is None and self._maxPoint is None

    def isEmpty(self):
        """
        判断Box是否为空

        :return:
        """
        return self._maxPoint == self._minPoint

    def centerPoint(self):
        """
        计算Box的中心点

        :return:
        """
        return (self._maxPoint + self._minPoint) / 2

    def volumn(self):
        # 体积
        return self.dimX() * self.dimY() * self.dimY()

    def dimX(self):
        # 长
        return abs(self._maxPoint.x - self._minPoint.x)

    def dimY(self):
        # 宽
        return abs(self._maxPoint.y - self._minPoint.y)

    def dimZ(self):
        # 高
        return abs(self._maxPoint.z - self._minPoint.z)

    @property
    def maxPoint(self):
        return self._maxPoint

    @property
    def minPoint(self):
        return self._minPoint

    @minPoint.setter
    def minPoint(self, minPoint):
        self._minPoint = minPoint

    @maxPoint.setter
    def maxPoint(self, maxPoint):
        self._maxPoint = maxPoint

    def __str__(self):
        return 'minPoint:%s, maxPoint:%s' % (self._minPoint, self._maxPoint)


if __name__ == '__main__':
    tBox = Box3D()
    print(tBox)
