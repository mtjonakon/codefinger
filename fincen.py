#packages

import codecs

import pandas as pd 
import numpy as np 

from bs4 import BeautifulSoup


#load file
f = open('new_scrape.html', 'r').read()

#set up file structure
alegal_name = []
adba_name = []
aaddress = []
acity = []
astate = []
azipcode = []
amsb_activities = []
astates_msb_activities = []
aall_states_terr_foreign = []
aforeign_location = []
ano_branches = []

#find the soup
soup = BeautifulSoup(f)
table = soup.table
rows = table.find_all('tr')

for r in rows:
	#retrieve
	#cols = r.find_all('td') #this is wrong but without the indent i get an out of range error
	try:

		cols = r.contents
		print cols
		legal_name = cols[1].a.string
		dba_name = cols[3].string
		address = cols[5].string
		city = cols[7].string
		state = cols[9].string
		zipcode = cols[11].string
		msb_activities = cols[13].string
		states_msb_activities = cols[15].string
		foreign_location = cols[17].string
		no_branches = cols[19].string
		
		alegal_name.append(legal_name)
		adba_name.append(dba_name)
		aaddress.append(address)
		acity.append(city)
		astate.append(state)
		azipcode.append(zipcode)
		amsb_activities.append(msb_activities)
		astates_msb_activities.append(states_msb_activities)
		aforeign_location.append(foreign_location)
		ano_branches.append(no_branches)

	except:

		print "bad tr string"
		continue


# OUTPUT 1: FINCEN.CSV - convert to pandas and export
df2 = pd.Series(alegal_name)
df3 = pd.Series(adba_name)
df4 = pd.Series(address)
df5 = pd.Series(acity)
df6 = pd.Series(astate)
df7 = pd.Series(azipcode)
df8 = pd.Series(amsb_activities)
df9 = pd.Series(astates_msb_activities)
df10 = pd.Series(aforeign_location)
df11 = pd.Series(ano_branches)

data = pd.concat([df2, df3, df4, df5, df6, df7, df8, df9, df10, df11], join='outer',axis=1) 
data.columns = ['legal name', 'dba name', 'address', 'city', 'state', 'zipcode', 'msb activities', 'states msb activities', 'foreign location', 'no branches']
data.to_csv("fincen.csv", encoding = 'utf-8')

	
