import subprocess as sp
a=sp.getoutput("ansible all --list-hosts")
b=a[14:]
c=b.split('\n')
for i in c:
	x = sp.getstatusoutput("ping -c 1 {}".format(i))
	if x[0]==0:
		print("Connection active: {}".format(i))
	else:
		print("Connection dead:   {}".format(i))



