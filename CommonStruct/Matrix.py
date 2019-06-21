import numpy

ne = numpy.ndarray


class BaseMatrix:
    def __init__(self, xData):
        if isinstance(xData, list):
            self.__data = xData
