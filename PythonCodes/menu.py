import os
import subprocess as sp
import pyttsx3

os.system("tput setaf 1")
print("\t\t\tWelcome to my tools")
os.system("tput setaf 0")
print("\t\t\t-------------------")

print("""
press 1 : To check data
press 2 : To cal
press 3 : To create user
press 4 : To create file
press 5 : exit
""")

speaker = pyttsx3.init()
speaker.say("Enter your choice")
speaker.runAndWait()

#print("Enter your choice:",end='')
ch = input()

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
	exit()
else:
	print("Not supported")

















