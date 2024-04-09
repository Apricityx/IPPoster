# http://pve.zwtsvx.xyz:1126/method.php?method=get_address
from time import sleep
import socket

import requests

url = 'http://pve.zwtsvx.xyz:1126/method.php?method=set_ip&ip='
ifDebug = True


def debug(arg):
    global ifDebug
    if ifDebug:
        print(f"\033[33mDebug:{arg}\033[0m")
    else:
        return


def send_ip(ip):
    res = requests.get(url + ip, timeout=5).text
    return res


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        if IP == "192.168.1.110":
            IP = "10.66.56.64"
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


while 1:
    sleep(1)
    while 1:
        try:
            debug(send_ip(get_ip()))
            debug('发送成功')
            sleep(1)
        except Exception as e:
            debug('网络异常')
            debug(e)
            sleep(10)
            continue
