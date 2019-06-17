from CommonStruct.Point2D import Point2D


class Box2D:
    def __init__(self, xMinPoint=Point2D(-1, -1), xMaxPoint=Point2D(1, 1)):
        assert isinstance(xMaxPoint, Point2D) and isinstance(xMinPoint, Point2D)
        self.__minPoint = xMinPoint
        self.__minPoint = xMaxPoint

    def __str__(self):
        return 'minPoint:%s, maxPoint:%s' % (self.__minPoint, self.__minPoint)


if __name__ == '__main__':
    tBox = Box2D()
    print(tBox)
