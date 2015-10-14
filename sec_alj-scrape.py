# this script is to extract the hyperlinks to the 2015 ALJ Orders 
# from the SEC website (http://www.sec.gov/alj/aljorders.shtml)

# packages
import re
import os
import time
import urllib2
import requests
import pandas as pd
from bs4 import BeautifulSoup

# setting the url for job search on craigslist
url = "http://www.sec.gov/alj/aljorders.shtml"

# alj orders
r = requests.get(url)

# parsing the page source into usable data
soup = BeautifulSoup(r.content)

# get the datafiles
links = []
for link in soup.find_all('a'):
	print(link.get('href'))
	links.append(str(link.get('href')))

# check the number of links found
print len(links)

# drop all non-.pdf links
pdf_links = []
for link in links: 
	if re.search(r'\.pdf',link):
		pdf_links.append(link)
print len(pdf_links)

#use the list with links to download the pdf files
i = 0
for link in pdf_links:
	i+=1
	file_link = "http://www.sec.gov" + link
	print file_link
	rq = urllib2.Request(file_link)
	res = urllib2.urlopen(rq)
	pdf = open("link%d.pdf" %i, 'wb')
	pdf.write(res.read())
	pdf.close()


time.sleep(1)

	
    



