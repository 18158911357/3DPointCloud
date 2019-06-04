"""
坐标系变换
"""

from numpy import *


def RotateMatrix(_axis, _theta):
    _theta = _theta * math.pi / 180
    cTheta = cos(_theta)
    sTheta = sin(_theta)
    if _axis == 'x':
        return array([[1, 0, 0], [0, cTheta, sTheta], [0, -sTheta, cTheta]])
    elif _axis == 'y':
        return array([[cTheta, 0, -sTheta], [0, 1, 0], [sTheta, 0, cTheta]])
    elif _axis == 'z':
        return array([[cTheta, sTheta, 0], [-sTheta, cTheta, 0], [0, 0, 1]])
    else:
        return None


if __name__ == '__main__':
    axis = 'z'
    theta = 90
    print(RotateMatrix(axis, theta))
