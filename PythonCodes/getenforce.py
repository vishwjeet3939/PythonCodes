import subprocess as sp
a=sp.getoutput("getenforce")
print("Currently selinux is in {} mode".format(a))
