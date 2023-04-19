#!/usr/bin/env python3
import os
os.system('pkg install python')
os.system('pip install requests')
os.system ("pip install urllib.request")
os.system('pip install pyfiglet')
import os
import pyfiglet
import requests
os.system('clear')
rs = requests.session()
R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"
nu = 0
n = 0
br = pyfiglet.figlet_format("CodeAx1")
print(B+br)
print('''
[Link Grabber From Website]
Coded By : CodeAX1
________________________________________
''')
from html.parser import HTMLParser
import urllib.request

class pyParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if(tag=="a"):
            for a in attrs:
                if(a[0] == "href"):
                    link = a[1]
                    if(link.find('http') >=0):
                        print(link)
                        newParse = pyParser()
                        newParse.feed(link)
url = input(Y+"Enter The Url with http:")
try:
    request = urllib.request.urlopen(url)
    parser = pyParser()
    parser.feed(request.read().decode('utf-8'))
except:
    print("Error Occured paste your url with http")
