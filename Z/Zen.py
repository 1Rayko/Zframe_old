
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
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(0.8)
done = True
os.system ('clear')
print(Fore.GREEN +
""" ____  ____
/_  / / __/______ ___ _  ___
 / /_/ _// __/ _ `/  ' \/ -_)
/___/_/ /_/  \_,_/_/_/_/\__/
                            """)
print(Fore.BLUE +Back.WHITE + 'Author : sudoreboot2020')
print(Fore.RED + 'Set option :')
print(Fore.YELLOW+'-----#deanonymization#-----')
print(Fore.YELLOW+ '1 - Saycheese')
print(Fore.YELLOW+ '2 - Seeker')
print(Fore.YELLOW+ '3 - sayhello ')
print(Fore.YELLOW+ '4 - sherlock ')
print(Fore.YELLOW+'5 - Deanons')
print(Fore.YELLOW+'-----#Utils for VK#-----')
print(Fore.YELLOW+ '6 - VTOOL')
print(Fore.YELLOW+ '7 - VKBRUTE')
print (Fore.YELLOW+"8 - VK DNK ")
print(Fore.YELLOW+'9 - kingfish')
print(Fore.YELLOW+'-----#others#-----')
print(Fore.YELLOW+ '10- smsham ')
print(Fore.YELLOW+ '11 - Recreator Phishing')
print(Fore.RED+ '12 - DDOS')
print(Fore.WHITE + '13 - http tunnels')


os.chdir('utils')
num =int(input(''))

#Приступим к самому соку :


if num == (1) :
    print (Fore.GREEN + 'Starting Saycheese')
    os.system('clear')
    os.chdir('saycheese-master')
    os.system('bash saycheese.sh')
elif num == (2):
    print (Fore.GREEN + 'Starting Seeker')
    os.system('clear')
    os.chdir('seeker-master')
    os.system('python3 seeker.py -t manual')
elif num == (3):
    print (Fore.GREEN + 'Starting sayhello')
    os.system('clear')
    os.chdir('sayhello-master')
    os.system('bash sayhello.sh')
elif num == (4):
    print (Fore.GREEN + 'Starting sherlock')
    os.system('clear')
    os.chdir('sherlock-master')
    os.system('python3 sherl.py')
elif num == (5):
	print(Fore.GREEN+"Starting deanons")
	os.chdir('deanons-master')
	os.system('clear')
	os.system('python3 dean.py')
elif num == (6):
    print(Fore.GREEN + 'Starting VTOOL')
    os.system('clear')
    os.chdir('vtool-master')
    os.system('python3 vtool.py')
elif num == (7) :
    print(Fore.GREEN + 'Starting VKBRUTE')
    os.system('clear')
    os.chdir('vtool-master')
    os.system('python3 brute.py')
elif num == (8):
    print(Fore.YELLOW+'Starting VKtoPasswd')
    os.chdir('VkToPassword-master')
    os.system('clear')
    os.system('python3 vtp.py')
elif num == (9):
	print(Fore.GREEN+'Starting kingfish')
	os.system('clear')
	os.chdir('kingfish-master')
	os.system('python3 fsh.py')
elif num == (10):
    print (Fore.GREEN + 'Starting smsham')
    os.system('clear')
    os.chdir('smsham-master')
    os.system('python3 smsham.py')


elif num == (11) :
    print (Fore.GREEN + 'Starting Recreator Phishing')
    os.system ('clear')
    os.chdir ('Recreator-Phishing-master')
    os.system ('python3 recreator-phishing.py')

elif num == (12):
    print(Fore.GREEN + 'Starting DDOS')
    os.system('clear')
    os.chdir('DDos')
    os.system('chmod 777 *')
    os.system('python3 2.py')

elif num == (13):
    print (Back.WHITE +Fore.BLUE  + '1 - ngrok or 2 - localhost.run')
    num = str(input(''))
    if num == ('1'):
        print (Back.WHITE +Fore.BLUE  + 'Port:')

        port = str(input())
        os.system('./ngrok http '+ port)
    elif num == ('2'):
        print (Back.WHITE +Fore.BLUE  + 'Port:')
        port = str(input())
        os.system('ssh -R 80:localhost:'+port+' ssh.localhost.run')
    else :
        print(Fore.RED +'RETURN')
else :
    print(Fore.RED +'RETURN')

