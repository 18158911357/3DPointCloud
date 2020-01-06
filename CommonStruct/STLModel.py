import struct
from Point3D import *
from TriangleSlice import *
from copy import deepcopy


class STLModel:
    def __init__(self, xListTri):
        """
        STL模型初始化
        :param xListTri: 三角片lSist
        """
        self.__listTri = deepcopy(xListTri)  # type: list

    @property
    def listTri(self):
        return self.__listTri

    @listTri.setter
    def listTri(self, xListTri):
        self.__listTri = deepcopy(xListTri)

    @staticmethod
    def ReadSTL(xPath):
        """
        从二进制文件中解析STL模型

        :param xPath: 文件路径
        :return: STL模型
        """
        List_TriSlice = LoadBrinary(xPath)
        return STLModel(List_TriSlice)

    def __len__(self):
        return len(self.__listTri)

    def __getitem__(self, xItem):
        return self.__listTri[xItem]

    def __str__(self):
        print('三角面片开始显示')
        for i, x in enumerate(self.__listTri):
            print(i, ':', x)
        return '三角面片显示结束'


###################
# region STL读取函数
def LoadBrinary(strPath):
    """
    读取STL二进制文件

    :param strPath:
    :return:
    """
    List_TriangleSlice = []
    with open(strPath, 'rb') as f:
        f.read(80)  # 流出80字节，文件名
        temp = f.read(4)  # 流出4字节，文件中结构体的数量
        count = struct.unpack('I', temp)[0]
        for i in range(count):
            List_TriangleSlice.append(TriangleSliceRead(f))
    return List_TriangleSlice


def TriangleSliceRead(f):
    """
    从字节流中读取三角片

    :param f:
    :return:
    """
    triSlice = TriangleSlice()
    triSlice.facet = PointRead(f)
    triSlice.vertex.vertex1 = PointRead(f)
    triSlice.vertex.vertex2 = PointRead(f)
    triSlice.vertex.vertex3 = PointRead(f)
    f.read(2)
    return triSlice


def PointRead(f):
    """
    从字节流中读取点(32位无符号整数，每次读取4个字节)

    :param f:
    :return:
    """
    point = Point3D()
    point.x = struct.unpack('f', f.read(4))[0]
    point.y = struct.unpack('f', f.read(4))[0]
    point.z = struct.unpack('f', f.read(4))[0]
    return point
# endregion
###################


if __name__ == '__main__':
    testPath = r'E:\项目\项目文件\3D玻璃50125\产品模型\L项目上表面.stl'
    testSTL = STLModel.ReadSTL(testPath)
    print('三角面片数量:', len(testSTL))
    print(testSTL)
