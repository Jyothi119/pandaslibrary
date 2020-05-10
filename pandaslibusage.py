import pandas as pd
import re

#loading data
data=pd.read_csv('C:/Users/Daddy/PycharmProjects/pandaslib/train.csv')
print(data.head(10))
print(data.columns)

#reading data
print(data.iloc[1:4])

#for index,row in data.iterrows():
#    print(index,row['browser'])

print(data.loc[data['browser']=='a'])

#sorting data
print(data.sort_values('ID', ascending=False))
print(data.sort_values(['ID','browser'],ascending=[1,0]))

#making changes to data

data['total_time']=data['time_on_partnerpage']+data['time_on_trivago']
print(data.head(2))

data=data.drop(columns=['total_time'])
print(data.head(2))

cols=list(data.columns)
print(cols)
data=data[cols[0:4]+[cols[-1]]+cols[4:19]]
print(data.head(2))

#to save data
print(data.to_csv('modified.csv', index=False))

#to filtering data
data.loc[data['browser'].str.contains('a|b')]

print(data.loc[data['device_type_name'].str.contains('sm[a-z]*')])

#conditional changes
print(data.loc[data['device_type_name']=='smart_fridge', 'device_type_name']=='change')

#Aggregate statistics
#groupby
print(data.groupby(['browser']).sum())
print(data.groupby(['browser']).count())