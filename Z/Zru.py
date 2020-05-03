#сорян что с этой колорамой такой пздц начал делать
import requests 
import datetime
import sys
import time
import argparse
import os 
import colorama 
import csv  
import json 
import vk
import random
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
import itertools
import threading
import time
import base64
import urllib.request
from bs4 import BeautifulSoup
import socket


os.system('clear')
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rзагрузка ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    

t = threading.Thread(target=animate)
t.start()

#long process heres
time.sleep(0.8)
done = True
os.system ('clear')
print(Fore.GREEN +
""" ____  ____                  
/_  / / __/______ ___ _  ___ 
 / /_/ _// __/ _ `/  ' \/ -_)
/___/_/ /_/  \_,_/_/_/_/\__/ 
                            """)

print(Fore.BLUE +Back.WHITE + 'Автор : sudoreboot2020')
print(Fore.RED + 'Выберите опцию :')
print(Fore.YELLOW+"""-----#Деанон#-----
[1] - Saycheese
[2] - Seeker
[3] - sayhello 
[4] - sherlock 
[5] - Deanons
-----#Работа с ВК#-----
[6] - VTOOL
[7] - VKBRUTE
[8] - VK To Password 
[9] - kingfish
[10] - kingfish2.0
-----#прочее#-----
[11] - smsham 
[12] - spymer
[13] - Recreator Phishing
[14] - DDOS
[15] - http тунели""")


os.chdir('utils')


#Приступим к самому соку :
while True:
    num =str(input("\033[35m\033[5m[*]"))
    if num == ('1') :
        print (Fore.GREEN + 'Запуск Saycheese')
        os.system('clear')
        os.chdir('saycheese-master')
        os.system('bash saycheese.sh')
    elif num == ('2'):
        print (Fore.GREEN + 'Запуск Seeker')
        os.system('clear')
        os.chdir('seeker-master')
 	os.system('chmod 777 template/nearyou/php/info.txt')
	os.system('chmod 777 template/nearyou/php/result.txt')
	os.system('python3 seeker.py -t manual')
    elif num == ('3'):
        print (Fore.GREEN + 'Запуск sayhello')
        os.system('clear')
        os.chdir('sayhello-master')
        os.system('bash sayhello.sh')
    elif num == ('4'):
        print (Fore.GREEN + 'Запуск sherlock')
        os.system('clear')
        os.chdir('sherlock-master')
        os.system('python3 sherl.py')
    elif num == ('5'):
	    print(Fore.GREEN+"Запуск deanons")
	    os.chdir('deanons-master')
	    os.system('clear')
	    os.system('python3 dean.py')
    elif num == ('6'):
        print(Fore.GREEN + 'Запуск VTOOL')
        os.system('clear')
        os.chdir('vtool-master')
        os.system('python3 vtool.py')
    elif num == ('7') :
        print(Fore.GREEN + 'Запуск VKBRUTE')
        os.system('clear')
        os.chdir('vtool-master')
        os.system('python3 brute.py')
    elif num == ('8'):
        print(Fore.YELLOW+'Запуск VKtoPasswd')
        os.chdir('VkToPassword-master')
        os.system('clear')
        os.system('python3 vtp.py')
    elif num == ('9'):
	    print(Fore.GREEN+'Запуск kingfish')
	    os.system('clear')
	    os.chdir('kingfish-master')
	    os.system('python3 fsh.py')
    elif num == ('10'):
	    print(Fore.GREEN+'Запуск kingfish2.0')
	    os.system('clear')
	    os.chdir('kingfish2-master')
	    os.system('python3 fsh.py')
    elif num == ('11'):
        print (Fore.GREEN + 'Запуск smsham')
        os.system('clear')
        os.chdir('smsham-master')
        os.system('python3 smsham.py')
    elif num == ('12'):
        print(Fore.GREEN+'Запуск spymmer')
        os.system('clear')
        os.chdir('spymer-master')
        os.system('python3 spammer.py')
    elif num == ('13') :
        print (Fore.GREEN + 'Запуск Recreator Phishing')
        os.system ('clear')
        os.chdir ('Recreator-Phishing-master')
        os.system ('python3 recreator-phishing.py')
    elif num == ('14'):
        print(Fore.GREEN + 'Запуск DDOS')
        os.system('clear')
        os.chdir('DDos')
        os.system('chmod 777 *')
        print (Fore.LIGHTBLUE_EX+"""Какой порт?[1]-80 или [2]-443""")
        pod = int(input(''))
        if pod == (1) or pod == (80):
            os.system('python3 80port.py')
        elif pod == (2) or pod == (443):
            os.system('python3 443port.py')
        else:
            print(Fore.RED+'ОШИБКА')

      
    elif num == ('15'):
        print (Back.WHITE +Fore.BLUE  + '1 - ngrok или 2 - localhost.run')
        while True:
            num = str(input("\033[35m\033[5m[*]"))
            if num == ('1'):
                print(Fore.LIGHTBLUE_EX+'КАКАЯ ОС?')
                print(Fore.LIGHTRED_EX+"[1]-android"+"\n"+"[2]-Linux")
                osy = int(input("\033[35m\033[5m[*]"))
                print (Fore.LIGHTBLUE_EX  + 'Порт:')
                port = str(input("\033[35m\033[5m[*]"))
                if osy == (1):
                    os.system('./ngroka http '+port)
                elif osy == (2):
                    os.system('./ngrok http '+port)
            elif num == ('2'):
                os.system('ssh -R 80:localhost:'+port+' ssh.localhost.run')
            else :
                print(Fore.RED +'ОШИБКА')
    else :
      print(Fore.RED +'ОШИБКА')

