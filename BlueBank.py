+# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 17:42:58 2022

@author: hp
"""
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
 
#transform to dataframe
loandata = pd.DataFrame(data)

#Finding unique values for the purpose column
loandata['purpose'].unique()

#describing the data
loandata.describe()

#describing the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP to get the anaual income
income = np.exp(loandata['log.annual.inc'])
loandata['AnnualIncome']= income

#working with arrays
#1D array
arr = np.array([1,2,3,4])

#0D array
arr = np.array(43)

#2D array
arr = np.array([[1,2,3],[4,5,6]]) 

#fico score
fico = 700
if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)

#for loops
fruits = ['Apple','Banana','Orange']
for x in fruits:
    print(x)

for x in range(0,3):
    y = fruits[x]
    print(y)    
    
    
#applying for loops to loan data
#using first 10
length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'very poor'
    elif category >= 400 and category < 600:
        cat = 'poor'
    elif category >= 601 and category < 660:
        cat = 'fair'
    elif category >= 660 and category < 700:
        cat = 'good'
    elif category >= 700:
        cat = 'excellent'
    else:
        cat = 'unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)    
loandata['fico.category'] = ficocat

length = len(loandata)
ficocat=[]
for x in range(0,length):
    category = 'Red'
    try:
        if category >= 300 and category < 400:
            cat = 'very poor'
        elif category >= 400 and category < 600:
            cat = 'poor'
        elif category >= 601 and category < 660:
            cat = 'fair'
        elif category >= 660 and category < 700:
            cat = 'good'
        elif category >= 700:
            cat = 'excellent'
        else:
            cat = 'unknown'
    except:
        cat = 'error - unknown'
    ficocat.append(cat)
    
    
#df.loc as conditional statements
# df.loc[df[columnname] condition, new columnname] == 'value if the condition mets'
#for interest rates, a new column is wanted. rates >0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type']= 'high'

loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type']= 'low'

loandata.loc[1]

#number of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.pie()
plt.show()


purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.pie()
plt.show()

#scatter plots
ypoint=loandata['AnnualIncome']
xpoint=loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()


#writing loan data into csv
loandata.to_csv('loan_clean.csv',index= True)



























