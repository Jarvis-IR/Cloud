import os
import time
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.0.53",9999))
print'done'


data=s.recvfrom(100)
x=data[0]
data=s.recvfrom(100)
y=data[0]
data=s.recvfrom(100)
z=data[0]
os.system('useradd -s /usr/bin/'+z+"   "+x)
os.system('echo '+y+' | passwd '+x+' --stdin')
print"done";

os.system('ssh -X -l '+x+' 192.168.0.53')
