import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_974657.html')
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
counttag = 0
sumtag = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    sumtag =  sumtag + int((tag.contents[0]))
    print('Attrs:', tag.attrs)
    counttag = int(counttag) + 1
print('Count ', counttag)
print('Sum ', sumtag)