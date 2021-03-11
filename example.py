import function
from tools import getIP


# 发送IP地址
def sendIP():
    ip = getIP()
    function.bark(ip)


if __name__ == '__main__':
    sendIP()