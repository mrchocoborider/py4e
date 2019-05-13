# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#html = urllib.request.urlopen(url, context=ctx).read()
html = urllib.request.urlopen(req)
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('p')
#for tag in tags:
#    print(tag.get('href', None))
print(len(tags))
