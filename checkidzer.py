import requests
import time
import os
from uuid import uuid4
from user_agent import generate_user_agent

# = = = = = = = = = = = = = = =
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[1;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[1;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
# = = = = = = = = = = = = = = =

c = input("""(1) Download lib & update
(2) pass

[ ⌯ ] Please Choose : """)

def ava():
	log = f'''
  \033[1;92m8888P 888888 88""Yb     888888  dP"Yb   dP"Yb  88     .dP"Y8 
    dP  88__   88__dP       88   dP   Yb dP   Yb 88     `Ybo." 
   dP   88""   88"Yb        88   Yb   dP Yb   dP 88  .o o.`Y8b 
  d8888 888888 88  Yb       88    YbodP   YbodP  88ood8 8bodP' 


{Z}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
{Z}[ {Y}⌯ {Z}]{F} SCRIPT BY    : ZER TOOLS
{Z}[ {Y}⌯ {Z}]{F} Telegram     : ZER TOOLS
{Z}[ {Y}⌯ {Z}]{F} Telegram     : O7181
{Z}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'''
	for logo in log.splitlines():
		time.sleep(0.09)
		print(logo)

if c == '1':
	os.system("pip install requests")
	os.system("pip install instaloader")
	os.system("pip install time")
	os.system('clear')
	pass
else:
	os.system('clear')
	pass

def main():
	os.system('clear');ava()
	file = input(f'{Z}[ {Y}⌯ {Z}]{F} ENTER NAME FILE : '+B)
	for Check in open(f'{file}','r').read().splitlines():
		user = str(Check.split('\n')[0])
		uid = uuid4()
		url = 'https://i.instagram.com/api/v1/accounts/login/'
		headers = {
			'User-Agent' : 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
			'Cookie':'missing',
			'Accept-Encoding':'gzip, deflate',
			'Accept-Language':'en-US',
			'X-IG-Capabilities':'3brTvw==',
			'X-IG-Connection-Type':'WIFI',
			'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
			'Host':'i.instagram.com'
		}
		data = {
			'uuid':uid,
			'password':'@whisper666',
			'username':''+user,
			'device_id':uid,
			'from_reg':'false',
			'_csrftoken':'missing',
			'login_attempt_countn':'0'
		}
		req= requests.post(url, headers=headers, data=data).json()
		if req['message'] == 'The password you entered is incorrect. Please try again.':
			print(f'{Z}[ {Y}+ {Z}]{F} AVAILABLE {Z}: {F}{user}')
		else:
			print(f'{Y}[ {Z}- {Y}]{Z} NOT AVAILABLE {F}: {Z}{user}')

main()
