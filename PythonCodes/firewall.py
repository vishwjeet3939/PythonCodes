import subprocess as sp
x=sp.getoutput("ansible localhost -m command -a 'systemctl status firewalld' ")
if "inactive" in  x:
	print("not active")
else:
	print("active") 

