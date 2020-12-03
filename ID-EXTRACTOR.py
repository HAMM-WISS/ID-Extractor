import amino
import time
import os
green = '\033[0;32m'
white = '\033[0;37m'
red = '\033[0;31m'
time.sleep(0.5)
emaillogin = input(green + "ENTER YOUR EMAIL :  ")
time.sleep(0.5)
passwordlogin = input("ENTER YOUR PASSWORD :  ")
time.sleep(2)
client =amino.Client()
email=emaillogin
password = passwordlogin
Gather=0
if Gather!=1:
	try:
		client.login(email=email, password=password)
	except:
		print(red+"Invalid email or password!"+white)
		os._exit(1)
print("[1]-Chat/User ID")
print("[2]-Community ID")
Choice=input(green+"Choose : "+white)
if choice==1:
	hostlink=input(green + "ENTER THE LINK : ")
	time.sleep(1)
	if len(hostlink)!=0:
		try:
			id =client.get_from_code(hostlink).objectId
		except:
			print(red+"Invalid url"+white)
			os._exit(1)
if choice==2:
	hostlink=input(green + "ENTER YOUR PROFILE LINK : ")
	time.sleep(1)
	if len(hostlink)!=0:
		try:
			uurl =client.get_from_code(hostlink).objectId
			id = uurl.path[1:uurl.path.index("/")]
		except:
			print(red+"Invalid url"+white)
			os._exit(1)
print(red + 'ID= ' + white + id)
os._exit(1)
