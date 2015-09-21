#this script parses the html table from www.fincen.gov, which contains all the money service businesses registered with FinCEN.
#language: Python 
#packages

import codecs
import csv


import pandas as pd 
import numpy as np 

from bs4 import BeautifulSoup


#load file
f = open('scrape.html', 'r').read()

output = csv.writer(open("MSB.csv", "w"))   # Open the output file for writing before the loop
f.writerow(["legal name", "dba name", "address", "city", "state", "zipcode", "msb activities", "states msb activities", "all states terr foreign", "foreign location", "no branches", "auth sign date", "received date" ]) 
# Write column headers as the first line

soup = BeautifulSoup(f)
table = soup.table
rows = table.find_all('tr')

for r in rows:

	cols = r.find_all('td')

	#we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
    try:

    	legal_name = cols[0].a.string
    	dba_name = cols[1].string
    	address = cols[2].string
    	city = cols[3].string
    	state = cols[4].string
    	zipcode = cols[5].string
		msb_activities = cols[6].string
		states_msb_activities = cols[7].string
		all_states_terr_foreign = cols[8].string
		foreign_location  = cols[9].string
		no_branches = cols[10].string
		auth_sign_date = cols[11].string
		received_date = cols[12].string

    except:

    	print "bad tr string"
    	continue #This tells the computer to move on to the next item after it encounters an error

    output.writerow([legal_name, dba_name, address, city, state, zipcode, msb_activities, states_msb_activities, all_states_terr_foreign, foreign_location, no_branches, auth_sign_date, received_date])




