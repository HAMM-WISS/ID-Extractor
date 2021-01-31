import amino
import time
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
client.login(email=email, password=password)
hostlink=input(green + "ENTER THE LINK : ")
time.sleep(1)
id =client.get_from_code(hostlink).objectId
print(red + 'ID= ' + white + id)