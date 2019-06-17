from Commonstruct.Point2D import Point2D


class Box2D:
    def __init__(self, xminPoint=Point2D(-1, -1), xmaxPoint=Point2D(1, 1)):
        self._minPoint = xminPoint
        self._maxPoint = xmaxPoint

    def __str__(self):
        return 'minPoint:%s, maxPoint:%s' % (self._minPoint, self._maxPoint)


if __name__ == '__main__':
    tBox = Box2D()
    print(tBox)
