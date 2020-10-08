'''In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
 scan for a tag that is in a particular position relative to the first name in the list, 
 follow that link and repeat the process a number of times and report the last name you find.'''
import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_html(url): # a function that gets URL's for us
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

url = input('Enter - ') # inputs
count = int(input('Enter count: '))
pos = int(input('Enter position: ')) - 1

urllist = list()

for i in range(count): #loop as many times as user asks
    taglist = list() #list with tags

    for tag in get_html(url)('a'): # Needed to update your variable to new url html
        taglist.append(tag)

    url = taglist[pos].get('href', None) # You grabbed url but never updated your tags variable.

    print('Retrieving: ', url)
    urllist.append(url)

print('Last URL: ', urllist[-1])