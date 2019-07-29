import os
import subprocess as sp
import getpass
import signal

def lw(x,y):
	print("\n Bye")
	exit()
signal.signal(2,lw) 
 


pswd1="abc"

pswd=getpass.getpass("enter pswd: ")
if pswd1==pswd:
	print("hi")
else:
	print("wrong pswd")

