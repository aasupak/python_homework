# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 06:43:22 2018

@author: aasup
"""

import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org',80))

cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()   #/n refers to "enter" on keyboard
mysock.send(cmd)

while True:
    data = mysock.recv(512)    #recieve data from site of up to 512 chars
    
    if (len(data)<1):
        break    #if while looping you get no data ends loop
    
    print(data.decode())   #if did get data, decode
    
mysock.close()