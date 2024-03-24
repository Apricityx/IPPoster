import os
import socket
import sys
from time import sleep

import requests

ifDebug = True


def debug(arg):
    global ifDebug
    if ifDebug:
        print(f"\033[33mDebug:{arg}\033[0m")


def reconnect():
    debug('连接断开，尝试重连')
    sleep(5)
    main()


def main():
    # 连接到服务器
    try:
        ws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ws.connect(('127.0.0.1', 8083))
        print('已连接')
        while 1:
            # 获取本机内网IP地址
            # res = requests.get('https://myip.ipip.net', timeout=5).text
            # res = res.split('：')[1].split(' ')[0]
            res = os.system('ipconfig')
            # res = str(res)
            # ws.send(res.encode('utf-8'))
            sleep(1)
    except ConnectionError as e:
        debug('与服务器断开连接')
        reconnect()
    except requests.exceptions.ReadTimeout:
        debug('本机网络异常')
        reconnect()


def http():
    x = requests.get('http://check.mctown.tech')
    print(x.status_code)


if __name__ == '__main__':
    main()
