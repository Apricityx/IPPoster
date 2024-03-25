from time import sleep
import socket

import requests

url = 'http://localhost/method.php?method=set_ip&ip='


def send_ip(ip):
    res = requests.get(url + ip, timeout=5).text
    return res


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


while 1:
    sleep(1)
    print(send_ip(get_ip()))
