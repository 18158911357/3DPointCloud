import time

Flag_Test = False  # 是否进入调试


def getLocalDate():
    """
    获取当前日期并格式化为str类型
    """
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def getLocalTime():
    """
    获取当前时间并格式化为str类型
    """
    return time.strftime('%X', time.localtime(time.time()))


def getLogFileName():
    """
    获取当日的log文件名，文件名为‘log-当前日期’
    """
    return 'log/logs-' + getLocalDate() + '.txt'


def newLogFile():
    """
    新建log文件，文件名为‘log-当前日期’
    """
    xLogFilePath = getLogFileName()
    with open(xLogFilePath, 'w') as f:
        print('##############################  %s  ##############################' % getLocalDate(), file=f)


def writeLogFile(xs):
    """
    将字符串xs写入log文件中，并加入当前时间
    """
    xLogFileName = getLogFileName()
    with open(xLogFileName, 'a') as xLogFile:
        print('%s || ' % getLocalTime() + xs, file=xLogFile)


if __name__ == '__main__':
    if Flag_Test:
        start = time.time()
        newLogFile()
        for i in range(10000):
            writeLogFile("我就是试试，试试就试试!")
        end = time.time()
        print(end - start)
