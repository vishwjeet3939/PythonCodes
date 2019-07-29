import subprocess as sp
x = sp.getoutput("ansible all -m setup | grep ansible_user_uid")
y=x[-3]
if y == '0':
	print("Administrative power active")
else:
	print("No admin power available")
