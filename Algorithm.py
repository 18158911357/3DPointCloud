from numpy import *
from Commonstruct import *


def Rodrigues(_x):
    """
    罗德里格斯变换
    -x = [nx,ny,nz],\n
    [x,y,z]为单位向量，表示旋转轴,\n
    n表示旋转角度,\n
    计算旋转矩阵\n

    :return: 变换矩阵
    """
    theta = Vector3D.norm(_x)
    s = math.sin(theta)
    c = math.cos(theta)
    c1 = 1.0 - c
    if theta == 0:
        itheta = 0
    else:
        itheta = 1 / theta
    _x = _x * itheta
    ax = Vector3D.toArray(_x)

    rrt = array([[ax[0] * ax[0], ax[0] * ax[1], ax[0] * ax[2]],
                 [ax[1] * ax[0], ax[1] * ax[1], ax[1] * ax[2]],
                 [ax[2] * ax[0], ax[2] * ax[1], ax[2] * ax[2]]])
    r_x = array([[0, -ax[2], ax[1]],
                 [ax[2], 0, -ax[0]],
                 [-ax[1], ax[0], 0]])
    ae = eye(3)
    r = c * ae + c1 * rrt + s * r_x
    return r


def CoordinateMatrix(_axis, _theta):
    """
    坐标系变换：通过输入旋转轴与旋转角度，输出3D坐标系旋转的矩阵

    :param _axis: 旋转轴，可选为‘x,y,z’
    :param _theta: 旋转角度
    :return: 坐标系旋转矩阵
    """
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


def RotateMatrix(_axis, _theta):
    """
    旋转矩阵：通过输入旋转轴与旋转角度，输出3D旋转的矩阵

    :param _axis: 旋转轴，可选为‘x,y,z’
    :param _theta: 旋转角度
    :return: 旋转矩阵
    """
    cTheta = cos(_theta)
    sTheta = sin(_theta)
    if _axis == 'x':
        return array([[1, 0, 0], [0, cTheta, -sTheta], [0, sTheta, cTheta]])
    elif _axis == 'y':
        return array([[cTheta, 0, sTheta], [0, 1, 0], [-sTheta, 0, cTheta]])
    elif _axis == 'z':
        return array([[cTheta, -sTheta, 0], [sTheta, cTheta, 0], [0, 0, 1]])
    else:
        return None


if __name__ == '__main__':
    x = Vector3D(0, 0, 1)
    print(Rodrigues(x))
    print('\n')
    print(RotateMatrix('z', 1))
