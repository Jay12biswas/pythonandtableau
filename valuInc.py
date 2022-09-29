# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 10:57:03 2022

@author: hp
"""

import pandas as pd
#file_name = pd.read_csv('file.csv') <--- format of read_csv
data = pd.read_csv('transaction.csv') 
data = pd.read_csv('transaction.csv',sep=';' )
 
data2 = pd.read_csv('value_inc_seasons.csv',sep=(';'))

#summary of the data
data.info()

#working with calculations
CostPerItem = 11.73 
SallingPricePerItem = 21.11
NumberofItemsPurchased = 6

#mathematical operation on tableau
ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SallingPricePerItem - CostPerItem
ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem 

#CostPerTransaction = CostPertItem * NumberOfItemPurchased
#Variable = dataframe['Column_name']

CostPerItem = data['CostPerItem']
NumberOfItemPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding a new column to a dataframe
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#SalesPerTransaction

data['SalesPerTransaction'] = data['SellingPricePerItem']*data['NumberOfItemsPurchased']

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

data['Markup'] = ( data['ProfitPerTransaction'] ) / data['CostPerTransaction']

#Rounding Marking

roundmarkup = round(data['Markup'],2)

#Combining Data Fields
myname = 'Jayesh' + 'Biswas'
print(myname)

#my_data = data['Day']+'-'+data['Month']+'-'+data['Year']

#checking columns datatypes
print(data['Day'].dtype)

#Change Column Type

day = data['Day'].astype(str)
year = data['Year'].astype(str)

my_date = day +'-'+data['Month']+'-'+year

data.iloc[0] #To view the rows with index = 0
data.iloc[0:3] #First 3 rows data
data.iloc[:5] #Last 5 rows data
data.head(5) #Bring up the first 5 rows
data.iloc[:,2] #Bring up the 2nd column data for all the rows 
data.iloc[2:,3]
data.iloc[2:5,4]
data.iloc[2,5]

split_col = data['ClientKeywords'].str.split(',',expand=True)
data['ClientAge']=split_col[0]
data['Clienttype']=split_col[1]
data['ClientContract']=split_col[2]
data['ClientAge']=data['ClientAge'].str.replace('[','')
data['ClientContract']=data['ClientContract'].str.replace(']','')

#How to merge files
#Merging in a new dataset
Seasons = pd.read_csv('value_inc_seasons.csv')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'Key')

data = pd.merge(data, Seasons, on = 'Month')
Seasons_data = data['Month']
Seasons_data = data['Season']

data['Month']

data['Day'] = data['Day'].astype(str)
data['Year']=data['Year'].astype(str)

data['Date']= data['Day'] + '-'+data['Month']+ '-' +data['Year']

#Drop Column
#df = df.drop('Column name', axis = 1)

#export into CSV
data.to_csv('ValueInc_cleaned.csv', index = False)





























