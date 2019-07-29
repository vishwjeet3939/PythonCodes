import os
import cv2
import subprocess as sp
import pyttsx3

#os.system("tput setaf 1")
print("\t\t\tWelcome to my tools")
#os.system("tput setaf 0")
print("\t\t\t-------------------")

print("Where you want to run this tool (local/remote/AWS): ",end='')
location=input()

if location=="remote":
	print("Enter ip of remote location: ",end='')
	remote_ip=input()
if location=="AWS":
	print("Enter ip of AWS os: ",end='')

print("""
press 1 : To check date
press 2 : To cal
press 3 : To create user
press 4 : To create file
press 5 : To click photo
press 6 : To launch docker
press 7 : exit
""")

speaker = pyttsx3.init()
speaker.say("Enter your choice")
speaker.runAndWait()

#print("Enter your choice:",end='')
ch = input()

if location=="local":

	if int(ch)==1:
		print(sp.getoutput("date"))
	elif int(ch)==2:
		print(sp.getoutput("cal"))
	elif int(ch)==3:
		print("Enter name of user:",end='')	
		user_name=input()
		sp.getoutput("useradd {}".format(user_name))
		print("User {} created successfully".format(user_name))
	elif int(ch)==4:
		print("Enter file name:",end='')	
		file_name=input()
		sp.getoutput("touch {}".format(file_name))
		print("file {} created successfully".format(file_name))
	elif int(ch)==5:
		sp.getoutput("python36 /root/Desktop/python_codes/photo.py")	
	elif int(ch)==6:
		sp.getoutput("docker run -it --name docker1 centos:latest")
	elif int(ch)==7:
		exit()
	else:
		print("Not supported")

elif location=="remote":
	
	if int(ch)==1:
		print(sp.getoutput("ssh {} date".format(remote_ip)))
	elif int(ch)==2:
		print(sp.getoutput("ssh {} cal".format(remote_ip)))
	elif int(ch)==3:
		print("Enter name of user:",end='')	
		user_name=input()
		sp.getoutput("ssh {} useradd {}".format(remote_ip,user_name))
		print("User {} created successfully".format(user_name))
	elif int(ch)==4:
		print("Enter file name:",end='')	
		file_name=input()
		sp.getoutput("ssh {} touch {}".format(remote_ip,file_name))
		print("file {} created successfully".format(file_name))
	elif int(ch)==5:						
		sp.getoutput("scp /root/Desktop/python_codes/photo.py {}:/root/Desktop".format(remote_ip))
		sp.getoutput("ssh -X {} python36 /root/Desktop/photo.py".format(remote_ip))
		sp.getoutput("scp {}:/root/Desktop/image.png /root/Desktop/".format(remote_ip))
	elif int(ch)==6:
		exit()
	else:
		print("Not supported")
elif location=="AWS":
	
	if int(ch)==1:
		print(sp.getoutput("ssh -l ec2-user {} -i your_key_name date".format(AWS_ip)))
	elif int(ch)==2:
		print(sp.getoutput("ssh -l ec2-user {} -i your_key_name cal".format(AWS_ip)))
	elif int(ch)==3:
		print("Enter name of user:",end='')	
		user_name=input()
		sp.getoutput("ssh -l ec2-user {} -i your_key_name useradd {}".format(AWS_ip,user_name))
	
		print("User {} created successfully".format(user_name))
	elif int(ch)==4:
		print("Enter file name:",end='')	
		file_name=input()
		sp.getoutput("ssh -l ec2-user {} -i your_key_name touch {}".format(AWS_ip,file_name))
		print("file {} created successfully".format(file_name))
#	elif int(ch)==5:						
#		sp.getoutput("scp /root/Desktop/python_codes/photo.py {}:/root/Desktop".format(AWS_ip))
#		sp.getoutput("ssh {} python36 /root/Desktop/photo.py".format(AWS_ip))
#		sp.getoutput("scp {}:/root/image.png /root/Desktop/images".format(AWS_ip))
	
	else:
		print("Not supported")

else:
	print("not supported")
