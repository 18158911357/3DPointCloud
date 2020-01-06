"""
Focal 1200 型号参数
"""
from numpy import *
from CommonStruct import pyLine3D
from CommonStruct import pyPoint3D
import Algorithm


class Focal_1200:
    def __init__(self):
        """
        Focal_1200内部参数初始化

        1. 激光线宽度
            Optical profile length = 11.26 mm
        2. 点间隔
            Pixel size X = 0.0055 mm
        3. Y向最小间隔
            Pixel size Y = 0.025 mm
        4. Z向精度
            Z-resolution = 0.00055 mm
        5. 工作距离
            Stand-off distance = 16.16 mm
        6. 景深
            景深（DOF），是指在摄影机镜头或其他成像器前沿能够取得清晰图像的成像所测定的被摄物体前后距离范围。
            Z-range = 2.8
        7.
            Max slope of object = ±20 deg
        """
        self.pixel_size_x = 0.0055
        self.pixel_num_x = 2048
        self.pixel_size_y = 0.025
        self.z_resolution = 0.00055
        self.stand_off_distance = 16.16
        self.z_range = 2.8
        self.max_slope = 20
        #####################################################
        self.location = pyPoint3D()  # 传感器的安装位置(平移向量)
        # 约定：传感器的默认激光为在x方向上的分布
        # 传感器的默认安装方式(传感器坐标系与世界坐标系一致)
        self.Mounting_method = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.Fix_Posture = pyPoint3D()  # 传感器的安装姿态(旋转向量)
        # region 激光初始化
        self.LaserLine = [pyLine3D(i * self.pixel_size_x, 0, 0) for i in range(self.pixel_num_x)]
        for i in range(len(self.LaserLine)):
            self.LaserLine[i].direction = pyPoint3D(0, 0, -1)
            print(i, self.LaserLine[i])
        # endregion

    def Fix(self, Fix_Location, Mounting_method, Fix_Posture):
        """
        传感器的安装函数，由于传感器的安装姿态和安装方式，因此需要更新激光的起始点与方向

        :param Fix_Location:
        :param Mounting_method:
        :param Fix_Posture:
        :return:
        """
        self.location = Fix_Location
        self.Mounting_method = Mounting_method
        self.Fix_Posture = Fix_Posture
        Matrix_Posture = Algorithm.Rodrigues(self.Fix_Posture)
        # 更新激光的起始点与方向
        for line in self.LaserLine:
            line = line.lineRotate(self.Mounting_method)
            line = line.lineRotate(Matrix_Posture)
            line.origin += self.location


if __name__ == '__main__':
    focal = Focal_1200()
    print(len(focal.LaserLine))
    for iii4 in focal.LaserLine:
        print(iii4)
    li = pyPoint3D(1, 1, 1)
    mi = Algorithm.RotateMatrix('z', pi / 2)
    pii = pyPoint3D(0, 0, 0)
    focal.Fix(li, mi, pii)
    for iii in focal.LaserLine:
        print(iii)
