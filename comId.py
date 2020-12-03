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
client=amino.Client()
print(red+"*You can input invitation link or community link it doesn't matter!:)*"+white)
curl=input(green+"ENTER COMMUNITY URL :  "+white)
courl=client.get_from_code(curl)
userId=courl.objectId
comId=courl.path[1:courl.path.index("/")]

print(green+"ID="+white+comId)