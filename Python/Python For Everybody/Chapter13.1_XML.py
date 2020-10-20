'''Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_974659.xml (Sum ends with 47)'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')

print('Retrieving', url)
xmlfile = urllib.request.urlopen(url).read()
print('Retrieved: ', str(len(xmlfile)) + ' characters' )


tree = ET.fromstring(xmlfile)
counts = tree.findall('.//count')
print('Counts:', str(len(counts)))
sumcounts = 0
for count in counts:
    sumcounts += int(count.text)
print('Sum:', str(sumcounts))