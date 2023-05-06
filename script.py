pip install tqdm

import argparse
import os
import pyfiglet
import requests
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from typing import List
from tqdm import tqdm

# Define command line arguments
parser = argparse.ArgumentParser(description='Link grabber from website')
parser.add_argument('url', type=str, help='URL to extract links from')
parser.add_argument('--depth', type=int, default=1, help='Maximum depth to follow links')
args = parser.parse_args()

# Set up colored terminal output
R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"

# Display banner
br = pyfiglet.figlet_format("CodeAx1")
print(B+br)
print('''
[Link Grabber From Website]
Coded By : CodeAX1 
Modifyed By : jeturgavli
________________________________________
''')

# HTML parsing function
class pyParser(HTMLParser):
    def __init__(self, depth: int):
        super().__init__()
        self.depth = depth
        self.links: List[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            for a in attrs:
                if a[0] == "href":
                    link = a[1]
                    if link.startswith('http') and link not in self.links:
                        self.links.append(link)
                        if self.depth > 0:
                            newParser = pyParser(self.depth - 1)
                            newParser.feed(requests.get(link).text)
    
    def get_links(self) -> List[str]:
        return self.links

# Start parsing from the specified URL
try:
    response = requests.get(args.url)
    parser = pyParser(args.depth)
    parser.feed(response.text)
    links = parser.get_links()
    print(f"{len(links)} links found:\n")
    for link in tqdm(links):
        print(link)
except requests.exceptions.RequestException as e:
    print(f"{R}Error occurred: {e}")
