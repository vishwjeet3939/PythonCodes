import subprocess as sp
x = sp.getoutput("firewall-cmd --list-all | grep ports:")
z=x.find("forward")
y=x[8:z]
print("Permitted ports: {0}".format(y))
