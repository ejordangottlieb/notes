#!/usr/bin/env python

import socket
import threading
from ipaddress import IPv6Network
from time import sleep
import sys

class TcpPlay(object):
    def __init__(self,net,port,connections):
        self.port = port
        self.connections = connections + 1
        self.ip6net = IPv6Network(net)

    def play(self):
        for x in range(1,self.connections):
            ip6addr = '{}'.format(self.ip6net[x])
            threading.Thread(target = self.process_conn,
                             args = (ip6addr,)).start()

    def process_conn(self,ip6addr):
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        s.connect((ip6addr, self.port))
        addrstr = '{}\n'.format(ip6addr)
        s.send(addrstr)
        while True:
            try:
                data = s.recv(1024)
                if data:
                    print(data)
                    break
            except:
                   s.close()
                   return False
        sleep(60)
        s.close()

if __name__ == "__main__":
    connections = int(sys.argv[1])
    x = TcpPlay('2001:db8:0:1::/64', 9999, connections).play()
