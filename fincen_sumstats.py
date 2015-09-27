'''
KEY FORM 107

401  	Issuer of traveler's checks
402  	Seller of traveler's checks
403  	Redeemer of traveler's checks
404  	Issuer of money orders
405  	Seller of money orders
406  	Redeemer of money orders
407  	Currency dealer or exchanger
408  	Check casher
409  	Money transmitter
410  	Traveler's Checks sales and/or redemption
411  	Money Orders sales and/or redemption
412  	U.S. Postal Service
413  	Seller of prepaid access
414  	Provider of prepaid access
415  	Dealer in foreign exchange
499  	Other

'''

#packages
import pandas as pd 
import numpy as np 
import scipy

import re

import thread

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#graphics
def plot_chart(dictionary):
	x = np.array(list(dictionary.keys()))
	y = np.array(list(dictionary.values()))

	sns.axes_style('white')
	sns.set_style('white')

	COLORS = 'Greens_d'

	(f, ax) = plt.subplots(1)

	b = sns.barplot(
		x,
		y,
		ci = None,
		palette = COLORS,
		hline = 0,
		ax = ax,
		x_order = x)
	
	#labels
	_TITLE = "Registrants by MSB Activities"
	ax.set_title(_TITLE)
	_XLABEL = "MSB Activities"
	ax.set_xlabel(_XLABEL)
	_YLABEL = "No of Registrants"
	ax.set_ylabel(_YLABEL)
	b.set_xticklabels(x, rotation = 90)
	#create margin at bottom for better layout
	plt.subplots_adjust(bottom=0.35)

	plt.show()
	




#load file
df = pd.read_csv('./fincen.csv')
print '\n\n\nFIRST FEW OBSERVATIONS OF THE DATASET...'
print df.head()

# what are the type of crimes that occur in SF?
print "MATRIX SHAPE:" 
print df.shape
print '\n\n\nHEADERS...'
print df.columns.values
#print '\n\n\nCRIME CATEGORY FREQUENCY COUNT...'
#print df['Category'].value_counts()

df['Issuer_Checks'] = df['msb activities'].str.contains("401")
df['Seller_Checks'] = df['msb activities'].str.contains("402")
df['Redeemer_Checks'] = df['msb activities'].str.contains("403")
df['Issuer_Orders'] = df['msb activities'].str.contains("404")
df['Seller_Orders'] = df['msb activities'].str.contains("405")
df['Redeemer_Orders'] = df['msb activities'].str.contains("406")
df['Currency_DealExch'] = df['msb activities'].str.contains("407")
df['Check_Casher'] = df['msb activities'].str.contains("408")
df['Money_Transmit'] = df['msb activities'].str.contains("409")
df['SaleRedeem_Checks'] = df['msb activities'].str.contains("410")
df['SaleRedeem_Order'] = df['msb activities'].str.contains("411")
df['US_Postal_Service'] = df['msb activities'].str.contains("412")
df['Seller_PrePaid'] = df['msb activities'].str.contains("413")
df['Provider_PrePaid'] = df['msb activities'].str.contains("414")
df['ForEx_Dealer'] = df['msb activities'].str.contains("415")
df['Other_Activities'] = df['msb activities'].str.contains("499")

print '\n\n\n MSB ACTIVITIES:'
print np.sum(df['Issuer_Checks'])
print np.sum(df['Seller_Checks'])
print np.sum(df['Redeemer_Checks'])
print np.sum(df['Issuer_Orders'])
print np.sum(df['Seller_Orders'])
print np.sum(df['Redeemer_Orders'])
print np.sum(df['Currency_DealExch'])
print np.sum(df['Check_Casher'])
print np.sum(df['Money_Transmit'])
print np.sum(df['SaleRedeem_Checks'])
print np.sum(df['SaleRedeem_Order'])
print np.sum(df['US_Postal_Service'])
print np.sum(df['Seller_PrePaid'])
print np.sum(df['Provider_PrePaid'])
print np.sum(df['ForEx_Dealer'])
print np.sum(df['Other_Activities'])

#Create Summation Object
print "Creating summation object"

'''To get the row number 11: df.columns.get_loc('Issuer_Checks')
To get the last column number: len(df.columns)
To print the column: print df.ix[:,11] 
To print the row: df.ix[11,:] 
'''

MSB_ACT_SUM = {}
for c in df.ix[:,11:27]:
	print df.ix[:,c]
	a = np.sum(df.ix[:,c])
	MSB_ACT_SUM[c] = a



#call the method 
plot_chart(MSB_ACT_SUM)

