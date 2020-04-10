import os
import colorama
from colorama import Fore , Back , Style
os.system('clear')
print(Fore.GREEN +
""" ____  ____                  
/_  / / __/______ ___ _  ___ 
 / /_/ _// __/ _ `/  ' \/ -_)
/___/_/ /_/  \_,_/_/_/_/\__/ 
                            """)
print(Fore.GREEN+'Enter Lang :')
print(Fore.RED+'['+Fore.YELLOW+'1'+Fore.RED+'] - RUS/РУС')
print(Fore.RED+'['+Fore.YELLOW+'2'+Fore.RED+'] - ENG/АНГ')
os.chdir('Z')
lag = input()
if lag == ('1'):
    os.system('clear')
    os.system('python3 Zru.py')
elif lag == ('2'):
    os.system('clear')
    os.system('python3 Zen.py')
else :
    print(Fore.RED+'RETURN')
