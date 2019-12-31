import time

Flag_Test = False  # 是否进入调试


def GetLocalDate():
    """
    获取当前日期并格式化为str类型
    """
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def GetLocalTime():
    """
    获取当前时间并格式化为str类型
    """
    return time.strftime('%X', time.localtime(time.time()))


def GetLogFileName():
    """
    获取当日的log文件名，文件名为‘log-当前日期’
    """
    return 'log/logs-' + GetLocalDate() + '.txt'


def NewLogFile():
    """
    新建log文件，文件名为‘log-当前日期’
    """
    xLogFilePath = GetLogFileName()
    with open(xLogFilePath, 'w') as f:
        print('##############################  %s  ##############################' % GetLocalDate(), file=f)


def WriteLogFile(xs):
    """
    将字符串xs写入log文件中，并加入当前时间
    """
    xLogFileName = GetLogFileName()
    with open(xLogFileName, 'a') as xLogFile:
        print('%s || ' % GetLocalTime() + xs, file=xLogFile)


if __name__ == '__main__':
    if Flag_Test:
        start = time.time()
        NewLogFile()
        for i in range(10000):
            WriteLogFile("我就是试试，试试就试试!")
        end = time.time()
        print(end - start)
