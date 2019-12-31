import time


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
    with open(xLogFilePath, 'a') as f:
        print('##############################  %s  ##############################' % getLocalDate(), file=f)


if __name__ == '__main__':
    newLogFile()
