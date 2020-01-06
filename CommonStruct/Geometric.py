from copy import deepcopy
from math import *
import pyOperations
import struct
import numpy


class Point2D:
    def __init__(self, xx=0.0, xy=0.0):
        """
        初始化点坐标

        :param xx: X坐标
        :param xy: Y坐标
        """
        self.__x = xx
        self.__y = xy

    def __add__(self, xOther):
        if isinstance(xOther, Point2D):
            return Point2D(self.__x + xOther.x, self.__y + xOther.y)
        elif isinstance(xOther, (int, float)):
            return Point2D(self.__x + xOther, self.__y + xOther)
        else:
            return None

    def __sub__(self, xOther):
        if isinstance(xOther, Point2D):
            return Point2D(self.__x - xOther.x, self.__y - xOther.y)
        elif isinstance(xOther, (int, float)):
            return Point2D(self.__x - xOther, self.__y - xOther)
        else:
            return None

    def __truediv__(self, xOther):
        if isinstance(xOther, (int, float)) and xOther != 0:
            return Point2D(self.__x / xOther, self.__y / xOther)
        else:
            return None

    def __mul__(self, xOther):
        if isinstance(xOther, (int, float)):
            return Point2D(self.__x * xOther, self.__y * xOther)
        else:
            return None

    def __eq__(self, xOther):
        return isinstance(xOther, Point2D) and self.__x == xOther.x and self.__y == xOther.y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, xx):
        self.__x = xx

    @y.setter
    def y(self, xy):
        self.__y = xy

    def norm(self):
        """
        计算点pt到原点的距离

        :return: 点到原点的距离
        """
        return (self.__x * self.__x + self.__y * self.__y) ** 0.5

    def tolist(self):
        return [self.x, self.y]

    def __str__(self):
        return '[%.4f, %.4f]' % (self.__x, self.__y)


class Point3D:
    def __init__(self, xx=0.0, xy=0.0, xz=0.0):
        """
        初始化点坐标
        """
        assert isinstance(xx, (int, float)) and isinstance(xy, (int, float)) and isinstance(xz, (int, float))
        self.__x = xx
        self.__y = xy
        self.__z = xz

    def __add__(self, xOther):
        if isinstance(xOther, Point3D):
            return Point3D(self.__x + xOther.x, self.__y + xOther.y, self.__z + xOther.z)
        elif isinstance(xOther, (int, float)):
            return Point3D(self.__x + xOther, self.__y + xOther, self.__z + xOther)
        else:
            return None

    def __sub__(self, xOther):
        if isinstance(xOther, Point3D):
            return Point3D(self.__x - xOther.x, self.__y - xOther.y, self.__z - xOther.z)
        elif isinstance(xOther, (int, float)):
            return Point3D(self.__x - xOther, self.__y - xOther, self.__z - xOther)
        else:
            return None

    def __truediv__(self, xOther):
        if isinstance(xOther, (int, float)) and xOther != 0:
            return Point3D(self.__x / xOther, self.__y / xOther, self.__z / xOther)
        else:
            return None

    def __mul__(self, xOther):
        if isinstance(xOther, (int, float)):
            return Point3D(self.__x * xOther, self.__y * xOther, self.__z * xOther)
        elif isinstance(xOther, Point3D):
            # 将Point3D相乘理解为1*3的矩阵相乘，列向量乘以行向量
            temp1 = [self.x * xOther.x, self.x * xOther.y, self.x * xOther.z]
            temp2 = [self.y * xOther.x, self.y * xOther.y, self.y * xOther.z]
            temp3 = [self.z * xOther.x, self.z * xOther.y, self.z * xOther.z]
            tempList = [temp1, temp2, temp3]
            return Matrix3D(tempList)
        else:
            return None

    def __eq__(self, xOther):
        return isinstance(xOther, Point3D) and self.__x == xOther.x and self.__y == xOther.y and self.__z == xOther.z

    def toList(self):
        return [self.__x, self.__y, self.__z]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def x(self, xx):
        self.__x = xx

    @y.setter
    def y(self, xy):
        self.__y = xy

    @z.setter
    def z(self, xz):
        self.__z = xz

    def norm(self):
        """
        计算点pt到原点的距离
        """
        return (self.__x * self.__x + self.__y * self.__y + self.__z * self.__z) ** 0.5

    def projectionXY(self):
        return Point2D(self.x, self.y)

    def __str__(self):
        return '(%s, %s, %s)' % (self.__x, self.__y, self.__z)


class Line2D:
    def __init__(self, xa=1, xb=1, xc=0):
        """
        ax + by + c = 0

        :param xa:
        :param xb:
        :param xc:
        """
        assert isinstance(xa, (int, float)) and isinstance(xb, (int, float)) and isinstance(xc, (int, float))
        self.__a = xa
        self.__b = xb
        self.__c = xc

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @a.setter
    def a(self, xa):
        self.__a = xa

    @b.setter
    def b(self, xb):
        self.__b = xb

    @c.setter
    def c(self, xc):
        self.__c = xc

    def __str__(self):
        return 'Line2D:(%s, %s, %s)' % (self.__a, self.__b, self.__c)


class Line3D:
    def __init__(self, xOrigin=Point3D(0, 0, 0), xDirection=Point3D(1, 1, 0)):
        assert isinstance(xOrigin, Point3D) and isinstance(xDirection, Point3D)
        self.__origin = deepcopy(xOrigin)
        self.__direction = deepcopy(xDirection)

    @property
    def origin(self):
        return self.__origin

    @property
    def direction(self):
        return self.__direction

    @origin.setter
    def origin(self, xOrigin):
        self.__origin = deepcopy(xOrigin)

    @direction.setter
    def direction(self, xDirection):
        self.__direction = deepcopy(xDirection)

    def __str__(self):
        return 'origin:%s, direction:%s' % (self.origin, self.direction)


class Box2D:
    def __init__(self, xMinPoint=Point2D(-1, -1), xMaxPoint=Point2D(1, 1)):
        """
        Box初始化，两个点构造一个与世界坐标系平行的Box
        :param xMaxPoint:
        :param xMinPoint:
        """
        assert isinstance(xMaxPoint, Point2D) and isinstance(xMinPoint, Point2D)
        self.__minPoint = deepcopy(xMinPoint)
        self.__maxPoint = deepcopy(xMaxPoint)

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
        self.__minPoint = deepcopy(xMinPoint)

    @maxPoint.setter
    def maxPoint(self, xMaxPoint):
        self.__maxPoint = deepcopy(xMaxPoint)

    def __str__(self):
        return 'minPoint:%s, maxPoint:%s' % (self.__minPoint, self.__maxPoint)


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
    def minPoint(self):
        return self.__minPoint

    @property
    def maxPoint(self):
        return self.__maxPoint

    @minPoint.setter
    def minPoint(self, xMinPoint):
        self.__minPoint = deepcopy(xMinPoint)

    @maxPoint.setter
    def maxPoint(self, xMaxPoint):
        self.__maxPoint = deepcopy(xMaxPoint)

    def __str__(self):
        return 'minPoint:%s, maxPoint:%s' % (self.__minPoint, self.__maxPoint)


class Plane:
    def __init__(self, *args):
        if len(args) == 2:  # 点法式构造  A(x-x0)+B(y-y0)+C(z-z0)=0
            xPoint, xVector = args
            self.__point0 = deepcopy(xPoint)
            if xVector.z == 0:
                self.__point1 = deepcopy(self.__point0)
                self.__point1.z += 1
                self.__point2 = Point3D(0, 0, 0)
                self.__point2.x = self.__point0.x - (self.__point1.z - self.__point0.z) * xVector.y
                self.__point2.y = self.__point0.y + (self.__point1.z - self.__point0.z) * xVector.x
                self.__point2.z = self.__point0.z + (self.__point1.x - self.__point0.x) * xVector.y - (
                        self.__point1.y - self.__point0.y) * xVector.x
            else:
                temp = pyOperations.dotMultiply(xPoint, xVector)
                self.__point1 = Point3D(xPoint.x, xPoint.y + 1, 0)
                self.__point2 = Point3D(xPoint.x + 1, xPoint.y, 0)
                self.__point1.z = (temp - xVector.x * self.__point1.x - xVector.y * self.__point1.y) / xVector.z
                self.__point2.z = (temp - xVector.x * self.__point2.x - xVector.y * self.__point2.y) / xVector.z
        elif len(args) == 3:  # 三点式构造
            self.__point0 = args[0]
            self.__point1 = args[1]
            self.__point2 = args[2]
        else:
            self.__point0 = None
            self.__point1 = None
            self.__point2 = None

    def normVector(self):
        """
        返回平面的法向量
        :return:
        """
        vector1 = self.__point1 - self.__point0
        vector2 = self.__point2 - self.__point0
        vector3 = pyOperations.crossMultiply(vector1, vector2)
        return vector3 / vector3.norm()  # 单位化

    @property
    def point0(self):
        return self.__point0

    @property
    def point1(self):
        return self.__point1

    @property
    def point2(self):
        return self.__point2

    @point0.setter
    def point0(self, xPoint):
        self.__point0 = xPoint

    @point1.setter
    def point1(self, xPoint):
        self.__point1 = xPoint

    @point2.setter
    def point2(self, xPoint):
        self.__point2 = xPoint

    def __str__(self):
        return '[%s,\n %s,\n %s]' % (self.__point0, self.__point1, self.__point2)


class Triangle:
    def __init__(self, xVertex1=Point3D(), xVertex2=Point3D(), xVertex3=Point3D()):
        assert isinstance(xVertex1, Point3D) and \
               isinstance(xVertex2, Point3D) and \
               isinstance(xVertex3, Point3D)
        self.__vertex1 = deepcopy(xVertex1)
        self.__vertex2 = deepcopy(xVertex2)
        self.__vertex3 = deepcopy(xVertex3)

    @property
    def vertex1(self):
        return self.__vertex1

    @property
    def vertex2(self):
        return self.__vertex2

    @property
    def vertex3(self):
        return self.__vertex3

    @vertex1.setter
    def vertex1(self, xVertex1):
        self.__vertex1 = deepcopy(xVertex1)

    @vertex2.setter
    def vertex2(self, xVertex2):
        self.__vertex2 = deepcopy(xVertex2)

    @vertex3.setter
    def vertex3(self, xVertex3):
        self.__vertex3 = deepcopy(xVertex3)

    def centroid(self):
        """
        计算三角形的质心，三个点的平均值
        """
        centroid_x = (self.__vertex1.x + self.__vertex2.x + self.__vertex3.x) / 3
        centroid_y = (self.__vertex1.y + self.__vertex2.y + self.__vertex3.y) / 3
        centroid_z = (self.__vertex1.z + self.__vertex2.z + self.__vertex3.z) / 3
        return Point3D(centroid_x, centroid_y, centroid_z)

    def area(self):
        # 向量AB
        Vector_AB = Point3D((self.vertex2.x - self.vertex1.x),
                            (self.vertex2.y - self.vertex1.y),
                            (self.vertex2.z - self.vertex1.z))
        # 向量AC
        Vector_AC = Point3D((self.vertex3.x - self.vertex1.x),
                            (self.vertex3.y - self.vertex1.y),
                            (self.vertex3.z - self.vertex1.z))
        # 向量AB叉乘向量AC
        # | i  j  k |
        # |x1 y1 z1 |
        # |x2 y2 z2 |
        # (y1*z2-y2*z1, x2*z1-x1*z2, x1*y2-x2*y1)
        x_ABC = Point3D((Vector_AB.y * Vector_AC.z - Vector_AC.y * Vector_AB.z),
                        (Vector_AB.z * Vector_AC.x - Vector_AC.z * Vector_AB.x),
                        (Vector_AB.x * Vector_AC.y - Vector_AC.x * Vector_AB.y))
        Triangle_Area = sqrt(x_ABC.x * x_ABC.x + x_ABC.y * x_ABC.y + x_ABC.z * x_ABC.x) / 2
        return Triangle_Area

    def isInTriangle(self, xPoint):
        # 判断点是否在三角形内部
        # 通过面积的方式来判断，当点xPoint内部时，四个三角形的面积加起来是相等的
        triangle_1 = Triangle(xPoint, self.__vertex2, self.__vertex3)
        triangle_2 = Triangle(self.__vertex1, xPoint, self.__vertex3)
        triangle_3 = Triangle(self.__vertex1, self.__vertex2, xPoint)
        area1 = self.area()
        area2 = triangle_1.area()
        area3 = triangle_2.area()
        area4 = triangle_3.area()
        areaAll = area2 + area3 + area4
        if fabs(areaAll - area1) < area1 / 100:
            return True
        return False

    def __str__(self):
        return '[%s,%s,%s]' % (self.__vertex1, self.__vertex2, self.__vertex3)


class TriangleSlice:
    def __init__(self, xFacet=Point3D(), xVertex=Triangle()):
        """
        三角面片初始化函数

        :param xFacet: 法向量
        :param xVertex: 顶点(3个)
        """
        self.__facet = deepcopy(xFacet)
        self.__vertex = deepcopy(xVertex)

    @property
    def facet(self):
        return self.__facet

    @property
    def vertex(self):
        return self.__vertex

    @facet.setter
    def facet(self, xFacet):
        self.__facet = deepcopy(xFacet)

    @vertex.setter
    def vertex(self, xVertex):
        self.__vertex = deepcopy(xVertex)

    def __str__(self):
        return 'facet: %s, vectex: %s' % (self.__facet, self.__vertex)


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

    def ReadSTL(self, xPath):
        """
        从二进制文件中解析STL模型

        :param xPath: 文件路径
        :return: STL模型
        """
        List_TriSlice = self.LoadBrinary(xPath)
        return STLModel(List_TriSlice)

    ###################
    # region STL读取函数
    def LoadBrinary(self, strPath):
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
                List_TriangleSlice.append(self.TriangleSliceRead(f))
        return List_TriangleSlice

    def TriangleSliceRead(self, f):
        """
        从字节流中读取三角片

        :param f:
        :return:
        """
        triSlice = TriangleSlice()
        triSlice.facet = self.PointRead(f)
        triSlice.vertex.vertex1 = self.PointRead(f)
        triSlice.vertex.vertex2 = self.PointRead(f)
        triSlice.vertex.vertex3 = self.PointRead(f)
        f.read(2)
        return triSlice

    @staticmethod
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

    def __len__(self):
        return len(self.__listTri)

    def __getitem__(self, xItem):
        return self.__listTri[xItem]

    def __str__(self):
        print('三角面片开始显示')
        for i, x in enumerate(self.__listTri):
            print(i, ':', x)
        return '三角面片显示结束'


class Matrix3D:
    def __init__(self, xList):
        assert isinstance(xList, list)
        self.__data = numpy.array(xList)

    def __len__(self):
        return self.__data.size

    def shape(self):
        return self.__data.shape

    def __getitem__(self, xItem):
        return self.__data[xItem]

    def __mul__(self, xOther):
        if isinstance(xOther, Point3D):
            # 矩阵左乘向量，点
            tempX = float(self.__data[0][0] * xOther.x + self.__data[0][1] * xOther.y + self.__data[0][2] * xOther.z)
            tempY = float(self.__data[1][0] * xOther.x + self.__data[1][1] * xOther.y + self.__data[1][2] * xOther.z)
            tempZ = float(self.__data[2][0] * xOther.x + self.__data[2][1] * xOther.y + self.__data[2][2] * xOther.z)
            return Point3D(tempX, tempY, tempZ)
        elif isinstance(xOther, Line3D):
            # 矩阵左乘3D直线
            tempOrigin = self * xOther.origin
            tempDirection = self * xOther.direction
            return Line3D(tempOrigin, tempDirection)
        elif isinstance(xOther, Matrix3D):
            # 矩阵相乘
            return self.__data * xOther.__data
        elif isinstance(xOther, (int, float)):
            return self.__data * xOther
        else:
            return None

    @staticmethod
    def eye():
        return Matrix3D([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    def T(self):
        return list(zip(*self.__data))

    def trace(self):
        # 求矩阵的迹
        # 在线性代数中，一个n×n矩阵A的主对角线（从左上方至右下方的对角线）上各个元素的总和被称为矩阵A的迹（或迹数）
        pass

    def __str__(self):
        return str(self.__data)

    # 相似变换(待实现)
    # 仿射变换(待实现)
    # 射影变换(待实现)


# 四元数
class Quaternion:
    def __init__(self, xs, xv):
        assert isinstance(xs, (int, float))
        assert isinstance(xv, (Point3D,))
        self.__s = xs
        self.__v = deepcopy(xv)

    def __str__(self):
        tempStr = [self.__s, str(self.__v)]
        return str(tempStr)

    def __add__(self, other):
        assert isinstance(other, Quaternion)
        return Quaternion(self.__s + other.__s, self.__v + other.__v)

    def __sub__(self, other):
        assert isinstance(other, Quaternion)
        return Quaternion(self.__s - other.__s, self.__v - other.__v)

    def __mul__(self, other):
        assert isinstance(other, Quaternion)
        tempS = self.__s * other.__s - self.__v.x * other.__v.x - self.__v.y * other.__v.y - self.__v.z * other.__v.z
        tempVx = self.__s * other.__v.x + self.__v.x * other.__s + self.__v.y * other.__v.z - self.__v.z * other.__v.y
        tempVy = self.__s * other.__v.y - self.__v.x * other.__v.z + self.__v.y * other.__s + self.__v.z * other.__v.x
        tempVz = self.__s * other.__v.z + self.__v.x + other.__v.y - self.__v.y * other.__v.x + self.__v.z * other.__s
        return Quaternion(tempS, Point3D(tempVx, tempVy, tempVz))

    def conjugateQuaternion(self):
        # 共轭四元数
        tempS = self.__s
        tempVx = -self.__v.x
        tempVy = -self.__v.y
        tempVz = -self.__v.z
        return Quaternion(tempS, Point3D(tempVx, tempVy, tempVz))

    def norm(self):
        # 模
        return (self.__s ** 2 + self.__v.x ** 2 + self.__v.y ** 2 + self.__v.z ** 2) ** 0.5

    def inverseQuaternion(self):
        # 四元数的逆
        tempNorm = self.norm()
        tempS = self.__s / tempNorm
        tempV = self.__v / tempNorm
        return Quaternion(tempS, tempV)

    def rotatePrint(self):
        # 打印四元数对应的旋转角度与旋转轴
        xTheta = 2 * acos(self.__s)
        xAxis = self.__v / sin(xTheta / 2)
        print('旋转角度为：', xTheta, end=' ')
        print('旋转轴为：', xAxis)

    @property
    def s(self):
        return self.__s

    @property
    def v(self):
        return self.__v

    @s.setter
    def s(self, xS):
        self.__s = xS

    @v.setter
    def v(self, xV):
        self.__v = xV


def numMul(xNum: (int, float), xQuaternion: Quaternion):
    # 数乘
    assert isinstance(xNum, (int, float)) and isinstance(xQuaternion, Quaternion)
    return Quaternion(xQuaternion.s * xNum, xQuaternion * xNum)


def dotMul(xQuaternion: Quaternion, yQuaternion: Quaternion):
    # 点乘
    assert isinstance(xQuaternion, Quaternion) and isinstance(yQuaternion, Quaternion)
    tempS = xQuaternion.s * yQuaternion.s
    tempVx = xQuaternion.v.x * yQuaternion.v.x
    tempVy = xQuaternion.v.y * yQuaternion.v.y
    tempVz = xQuaternion.v.z * yQuaternion.v.z
    return Quaternion(tempS, Point3D(tempVx, tempVy, tempVz))


def Rotate(xPoint, xQuaternion):
    # 用四元数表示旋转，计算结果为纯虚四元数，虚部的三个分量表示旋转后的3D点坐标
    assert isinstance(xPoint, Point3D) and isinstance(xQuaternion, Quaternion)
    xP = Quaternion(0, xPoint)
    tempQuaternion = xQuaternion * xP * xQuaternion.inverseQuaternion()
    if tempQuaternion.s == 0:
        return tempQuaternion.v
    else:
        print('输入的四元数有误')
        return None


def matrixToQuaternion(xMatrix):
    # 由矩阵到四元数的转换
    assert isinstance(xMatrix, Matrix3D)
    tempQ0 = (xMatrix.trace() + 1) ** 0.5 / 2
    tempQ1 = (xMatrix[1][2] - xMatrix[2][1]) / (4 * tempQ0)
    tempQ2 = (xMatrix[2][0] - xMatrix[0][2]) / (4 * tempQ0)
    tempQ3 = (xMatrix[0][1] - xMatrix[1][0]) / (4 * tempQ0)
    return Quaternion(tempQ0, Point3D(tempQ1, tempQ2, tempQ3))


def quaternionToMatrix(xQuaternion):
    # 由四元数到矩阵的转换
    assert isinstance(xQuaternion, Quaternion)
    tempQ0 = xQuaternion.s
    tempQ1 = xQuaternion.v.x
    tempQ2 = xQuaternion.v.y
    tempQ3 = xQuaternion.v.z
    R00 = 1 - 2 * tempQ2 ** 2 - 2 * tempQ3 ** 2
    R01 = 2 * tempQ1 * tempQ2 + 2 * tempQ0 * tempQ3
    R02 = 2 * tempQ1 * tempQ3 - 2 * tempQ0 * tempQ2
    R10 = 2 * tempQ1 * tempQ2 - 2 * tempQ0 * tempQ3
    R11 = 1 - 2 * tempQ1 ** 2 - 2 * tempQ3 ** 2
    R12 = 2 * tempQ2 * tempQ3 + 2 * tempQ0 * tempQ1
    R20 = 2 * tempQ1 * tempQ3 + 2 * tempQ0 * tempQ2
    R21 = 2 * tempQ2 * tempQ3 - 2 * tempQ0 * tempQ1
    R22 = 1 - 2 * tempQ1 ** 2 - 2 * tempQ2 ** 2
    return Matrix3D([[R00, R01, R02], [R10, R11, R12], [R20, R21, R22]])


if __name__ == '__main__':
    tLine3D = Line3D()
    print(tLine3D)
    tPlane = Plane()
    print(tPlane)
