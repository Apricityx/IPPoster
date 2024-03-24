import socket
from time import sleep

import requests

ifDebug = True
print('Server started.')


def debug(arg):
    global ifDebug
    if ifDebug:
        print(f"\033[33mDebug:{arg}\033[0m")


def main():
    ws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ws.bind(('127.0.0.1', 8083))
    ws.listen()
    conn, addr = ws.accept()
    print(f"Connected by {addr}")
    while 1:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            print('Connection closed')
            break
        print(data)
        f = open('ip.txt', 'r+')
        f.write(data + '\n')
        f.close()
    ws.close()


if __name__ == '__main__':
    while 1:
        main()
