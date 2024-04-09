import socket
from time import sleep

import requests

ifDebug = True


def debug(arg):
    global ifDebug
    if ifDebug:
        print(f"\033[33mDebug:{arg}\033[0m")


debug('Server started.')


def main():
    ws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ws.bind(('127.0.0.1', 8083))
    ws.listen()
    conn, addr = ws.accept()
    debug(f"Connected by {addr}")
    # 新建一个线程，若检测到连接断开，则将文件ip中第二行的内容改为0，若检测到新的连接，则将文件ip中第二行的内容改为1
    while 1:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            print('Connection closed')
            break
        print(data)
        f = open('ip', 'r+')
        f.write(data + '\n')
        debug('写入成功')
        f.close()
    ws.close()


if __name__ == '__main__':
    while 1:
        main()
