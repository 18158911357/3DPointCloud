from ma import *


class B:
    def __init__(self, xValue=A(1)):
        self.value = xValue


if __name__ == '__main__':
    a = A()
    print(a.value)
    b = B()
    print(b.value.value)
