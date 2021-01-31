import amino
import time
import os
green = '\033[0;32m'
white = '\033[0;37m'
red = '\033[0;31m'

os.system("clear")
print(green+"  __   __     _____     __      __    __      __")

print("/|::|/|::|  //:::::\  /|::\    /::| /|::\    /::|")

print("||::|||::| //::/\\\::\ ||:::\  /:::| ||:::\  /:::|")

print("||::|||::| ||::|||::| ||::::\/::::| ||::::\/::::|")

print("||:::::::| ||:::::::| ||::|\::/|::| ||::|\::/|::|")

print("||::|||::| ||::|||::| ||::|/_/||::| ||::|/_/||::|")

print("||::|||::| ||::|||::| ||::|   ||::| ||::|   ||::|")

print("||::|||::| ||::|||::| ||::|   ||::| ||::|   ||::|")

print("|/__/|/__/ |/__/|/__/ |/__/   |/__/ |/__/   |/__/"+white)

time.sleep(1)

print(red+" _ _ _ ____    ____ ____ ____ ")
print(" | | | |___    |__| |__/ |___ ")
print(" |_|_| |___    |  | |  \ |___ "+white)
                              
time.sleep(1)
print("        ____  ____  ____  ____  ____  ____  ____ ")
print("       ||"+red+"M "+white+"||||"+red+"A"+white+" ||||"+red+"K "+white+"||||"+red+"Y"+white+" ||||"+red+"R "+white+"||||"+red+"O"+white+" ||||"+red+"N "+white+"||")
print("       ||__||||__||||__||||__||||__||||__||||__||")
print("       |/__\||/__\||/__\||/__\||/__\||/__\||/__\|")
time.sleep(1)
print("------------------------------------------------")
client =amino.Client()
client.login_sid(SID=input(green + "ENTER SID : "))
hostlink=input(green + "ENTER THE URL : ")
time.sleep(1)
id =client.get_from_code(hostlink)
comId=id.path[1:id.path.index("/")]
userId=id.objectId
print(red + 'ID= ' + white + comId + ": " + userId)