from platform import system
import sys
import os
import datetime   
from time import sleep
import getpass
url = 'https://m.facebook.com/login.php'
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import getpass
import subprocess 
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from urllib.parse import quote
ugen2=['User Agent: Mozilla/5.0 (Linux; Android 12; vivo 1938 Build/SP1A.210812.003;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36']
ugen=['User Agent: Mozilla/5.0 (Linux; Android 12; vivo 1938 Build/SP1A.210812.003;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36']



def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()


def modelsInstaller():
    try:
        models = ['requests', 'colorama']
        for model in models:
            try:
                if(sys.version_info[0] < 3):
                    os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
                else:
                    os.system('python -m pip install {}'.format(model))
                print(' ')
                print('[+] {} has been installed successfully, Restart the program.'.format(model))
                sys.exit()
                print(' ')
            except:
                print('[-] Install {} manually.'.format(model))
                print(' ')
    except:
        pass


import base64
import json
import time
import sys
import os
import re
import binascii
import time
import json
import random
import threading
import pprint
import smtplib
import telnetlib
import os.path
import hashlib
import string
import glob
import getpass
import sqlite3
import urllib
import argparse
import marshal
import datetime   
from platform import system
from getpass import getpass
import getpass
from datetime import datetime

try:
    import requests
    from colorama import Fore
    from colorama import init
except:
    modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
    if system() == 'Linux':
        os.system('clear')
    else:
        if system() == 'Windows':
            os.system('cls')


cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;37;1m'  # mode 31 = red foreground
RESET = '\033[1;37;1m'  # mode 0  = reset
BLUE = "\033[1;37;1m"
khushi = "MAJNUDAD"
WHITE = "\033[1;37;1m",
YELLOW = "\033[1;37;1m",
CYAN = "\033[1;37;1m"
MAGENTA = "\033[1;37;1m",
GREEN = "\033[1;37;1m"
RESET = "\033[1;37;1m"
BOLD = '\033[1;37;1m'
REVERSE = "\033[1;37;1m"

# Logo
logo = """
\033[1;37m⌌\033[1;31m━━━━\033[1;32m━━━━\033[1;33m━━━━\033[1;34m━━━━\033[1;35m━━━━\033[1;36m━━━━\033[1;37m━━━━\033[1;30m━━━━\033[1;31m━━━\033[1;32m━━━━\033[1;33m━━━━━\033[1;34m━━━━\033[1;35m━━\033[1;37m⌍
\033[1;38m▏ 
 __      __                               ______  

     
███    ███  █████       ██ ███    ██ ██    ██ 
████  ████ ██   ██      ██ ████   ██ ██    ██ 
██ ████ ██ ███████      ██ ██ ██  ██ ██    ██ 
██  ██  ██ ██   ██ ██   ██ ██  ██ ██ ██    ██ 
██      ██ ██   ██  █████  ██   ████  ██████  
                                              
                                              

\033[1;37m⌎\033[1;31m━━━━\033[1;32m━━━━\033[1;33m━━━━\033[1;34m━━━━\033[1;35m━━━━\033[1;36m━━━━\033[1;37m━━━━\033[1;30m━━━━\033[1;31m━━━\033[1;32m━━━━\033[1;33m━━━━━\033[1;34m━━━━\033[1;35m━━\033[1;37m⌏                                              
                                             
\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[37m[*]  𝐎𝐖𝐍𝐄𝐑  𝐍𝐀𝐌𝐄     : \033[36m   𝐌𝟗𝐉𝟗𝐔 𝐃𝟎𝟗 
\033[37m[*]  𝐆𝐈𝐓𝐇𝐔𝐁     𝐈𝐃        : \033[33m   𝐌𝟗𝐉𝟗𝐔 𝐓𝐑𝟏𝟑𝐊𝟑𝐑 
\033[37m[*]  𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐈𝐃      : \033[32m   𝐌𝟒𝐉𝐍𝟗 𝐉𝟒𝐍𝐔 
\033[37m[*]  𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏            : \033[35m  𝟗𝟐𝟑𝟖𝟓𝟏𝟏𝟖𝟏𝟏
\033[37m[*]  𝐘𝐎𝐔𝐓𝐔𝐁𝐄             : \033[34m   𝐌𝟗𝐉𝟗𝐔 𝐁𝐇𝟗𝟏
\033[37m[*]  𝐓𝐎𝐎𝐋 𝐎𝐖𝐍𝐄𝐑     : \033[36m   𝐌𝟗𝐉𝟗𝐔 𝐃𝟎𝟗 
\033[37m[*]  𝐓𝐎𝐎𝐋 𝐒𝐓𝐀𝐓𝐔𝐒     : \033[33m   𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋 𝐈𝐒 𝐏𝐀𝐈𝐃
\033[37m[*]  𝐓𝐎𝐎𝐋 𝐓𝐘𝐏𝐄         : \033[32m   𝐌𝐔𝐋𝐓𝐈 𝐈𝐃𝐒 𝐂𝐎𝐍𝐕𝐎 𝐓𝐎𝐎𝐋
\033[37m[*]  𝐓𝐎𝐎𝐋 𝐏𝐀𝐑𝐓𝐍𝐄𝐑 : \033[35m   𝐀𝐋𝐎𝐍𝐄 𝐒𝐓𝐀𝐍𝐃 𝐌𝐀𝐉𝐍𝐔 𝐃𝐎𝐍 𝐇𝐄𝐑𝐄 
\033[37m[*] 𝐅𝐎𝐑 𝐇𝐀𝐀𝐓𝐄𝐑𝐒     : \033[34m   𝐇𝐀𝐓𝐄𝐑𝐒 𝐊𝐈 𝐌𝐀 𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 
\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
print(logo)
password = input("\033[1;36m[+] PASSWORD KE LIYE  WSP MSG KAR  UPER 9238511811 NUMBER HAI :: ")
import os
import random
import time
import requests

# Facebook Graph API endpoint
thread_id = input("\033[1;32mEnter thread ID: ")

url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'

# Token file paths
token_file_paths = input("\033[33mEnter token file paths (separated by comma): ").split(',')

# Message file path
message_file_path = input("\033[34mEnter message file path: ")

# Haters name
haters_name = input("\033[35mEnter haters name: ")

# Delay between messages
delay_between_messages = int(input("\033[36mEnter delay between messages: "))

# Read tokens from files
access_tokens = []
token_names = []
for token_file_path in token_file_paths:
    with open(token_file_path.strip(), "r") as token_file:
        for i, token in enumerate(token_file.readlines()):
            access_tokens.append(token.strip())
            token_names.append(f"Token {i+1}")

# Read messages from file
messages = []
with open(message_file_path, "r") as message_file:
    messages = message_file.readlines()

def get_account_name(token):
    try:
        response = requests.get(f'https://graph.facebook.com/v15.0/me?access_token={token}')
        data = response.json()
        return data['name']
    except Exception as e:
        return "Unknown"

def send_message(token, message, thread_id, haters_name):
    try:
        message_url = f"{url}"
        message_params = {
            "access_token": token,
            "message": f"{haters_name} {message}"
        }
        message_response = requests.post(message_url, params=message_params)
        if message_response.status_code == 200:
            current_time = time.strftime("%H:%M:%S")
            print(f"""
 \033[34m 
▁ ▂ ▄ ▅ ▆ ▇〓〓〓〓〓〓〓〓〓〓 ＭＡＪＮＵ ＤＯＮ ＨＥＲＥ 〓〓〓〓〓〓〓〓〓〓▇ ▆ ▅ ▄ ▂ ▁
""")
            account_name = get_account_name(token)           
            print(f"\033[38;5;25m[+] 𝗞𝗛𝗨𝗦 𝗛𝗢𝗝𝗔 𝗕𝗦𝗗𝗞𝗘 𝗠𝗦𝗚 𝗦𝗘𝗡𝗧 𝗛𝗢𝗚𝗬𝗔  => 𝗧𝗔𝗧𝗧𝗔 ID: {thread_id} => 𝗧𝗢𝗞𝗘𝗡: {token_names[access_tokens.index(token)]} => 𝗜𝗗 𝗡𝗔𝗠𝗘: {account_name} => 𝗧𝗔𝗧𝗧𝗔 𝗡𝗔𝗠𝗘: {haters_name} => 𝗠𝗔𝗦𝗦𝗔𝗚𝗘: {message} => 𝗧𝗜𝗠𝗘: {current_time}\033[0m")
        else:
            current_time = time.strftime("%H:%M:%S")
            print(f"""
 \033[31;5;196m 
▁ ▂ ▄ ▅ ▆ ▇〓〓〓〓〓〓〓〓〓〓 ＭＡＪＮＵ ＤＯＮ ＨＥＲＥ 〓〓〓〓〓〓〓〓〓〓▇ ▆ ▅ ▄ ▂ ▁
""")
            print(f"\033[38;5;196m𝗗𝗨𝗞𝗛𝗜 𝗛𝗢𝗝𝗔 𝗕𝗦𝗗𝗞𝗘 𝗠𝗦𝗚 𝗙𝗔𝗜𝗟 𝗛𝗢𝗚𝗬𝗔  => 𝗧𝗔𝗧𝗧𝗔 ID: {thread_id} => 𝗧𝗢𝗞𝗘𝗡: {token_names[access_tokens.index(token)]} => 𝗜𝗗 𝗡𝗔𝗠𝗘: {account_name} => 𝗧𝗔𝗧𝗧𝗔 𝗡𝗔𝗠𝗘: {haters_name} => 𝗠𝗔𝗦𝗦𝗔𝗚𝗘: {message} => 𝗧𝗜𝗠𝗘: {current_time}\033[0m")
    except Exception as e:
        print(str(e))

def process_messages_thread():
    try:
        while True:
            random_token = random.choice(access_tokens)
            random_message = random.choice(messages).strip()
            send_message(random_token, random_message, thread_id, haters_name)
            time.sleep(delay_between_messages)
    except Exception as e:
        print(str(e))

process_messages_thread()