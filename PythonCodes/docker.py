import subprocess as sp

i=1

while i<=10:
	sp.getoutput("docker run -itd ubuntu:14.04")
	i+=1
