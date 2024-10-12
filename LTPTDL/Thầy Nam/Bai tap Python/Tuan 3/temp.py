# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('dulieuxettuyendaihoc.csv', header = 0, delimiter = ',')
print(df.head(11))
print(df.tail(10))

print(df['T1']) #
print(df[['T1']])
print(df[['T1', 'L1']])

#cau 4
missingDT = df['DT'].isna().sum()  # tim tong du lieu thieu
print(missingDT)
df['DT'].fillna(0, inplace = True)
print(df['DT'])

#cau5 
missingT1 = df['T1'].isna().sum()
print(missingT1)
df['T1'].fillna(df['T1'].mean(), inplace = True)
print(df['T1'])

#cau 6


df[['L1','L2','L3']]=df[['L1','L2','L3']].fillna(df[['L1','L2','L3']].mean())
print(df[['L1','L2','L3']])

#cau7

df['TBM1'] = (df['T1']*2 + df['L1'] + df['H1'] + df['S1'] + df['V1']*2 +df['X1'] + df['D1'] + df['N1'])/10
print(df['TBM1'])

df['TBM2'] = (df['T2']*2 + df['L2'] + df['H2'] + df['S2'] + df['V2']*2 +df['X2'] + df['D2'] + df['N2'])/10
print(df['TBM2'])

df['TBM3'] = (df['T6']*2 + df['L6'] + df['H6'] + df['S6'] + df['V6']*2 +df['X6'] + df['D6'] + df['N6'])/10
print(df['TBM3'])

# cau 8

# sv tu hoc loc, iloc, ix
df.loc[df['TBM1']<5, 'XL1'] = 'Y'
df.loc[(df['TBM1']>=5.0) & (df['TBM1']<6.5), 'XL1'] = 'TB'
df.loc[(df['TBM1']>=6.5) & (df['TBM1']<8.0), 'XL1'] = 'K'
df.loc[(df['TBM1']>=8.0) & (df['TBM1']<9.0), 'XL1'] = 'G'
df.loc[(df['TBM1']>=9.0) & (df['TBM1']<=10.0), 'XL1'] = 'XS'
print(df[['TBM1','XL1']])

df.loc[df['TBM2']<5, 'XL2'] = 'Y'
df.loc[(df['TBM2']>=5.0) & (df['TBM2']<6.5), 'XL2'] = 'TB'
df.loc[(df['TBM2']>=6.5) & (df['TBM2']<8.0), 'XL2'] = 'K'
df.loc[(df['TBM2']>=8.0) & (df['TBM2']<9.0), 'XL2'] = 'G'
df.loc[(df['TBM2']>=9.0) & (df['TBM2']<=10.0), 'XL2'] = 'XS'
print(df[['TBM2','XL2']])

df.loc[df['TBM3']<5, 'XL3'] = 'Y'
df.loc[(df['TBM3']>=5.0) & (df['TBM3']<6.5), 'XL3'] = 'TB'
df.loc[(df['TBM3']>=6.5) & (df['TBM3']<8.0), 'XL3'] = 'K'
df.loc[(df['TBM3']>=8.0) & (df['TBM3']<9.0), 'XL3'] = 'G'
df.loc[(df['TBM3']>=9.0) & (df['TBM3']<=10.0), 'XL3'] = 'XS'
print(df[['TBM3','XL3']])

#cau 9
#x_new = [(x_old - min_old)/(max_old-min_old)*(max_new-min_new)] + min_new

df['US_TBM1']=((df['TBM1']-0)/(10.0-0)*(4.0-0))+0
print(df['US_TBM1'])

df['US_TBM2']=((df['TBM2']-0)/(10.0-0)*(4.0-0))+0
print(df['US_TBM2'])

df['US_TBM3']=((df['TBM3']-0)/(10.0-0)*(4.0-0))+0
print(df['US_TBM3'])

























#tuan 3 meo import dc

#sap xep

print(df[['DH1', 'KT']].sort_values(by=['DH1', 'KT'], ascending=[True, False]))



#frequency

freq_KV = df['KV'].value_counts()
print('Frequency', freq_KV)

#cummulative frequency

freq_cum_KV = freq_KV.cumsum()
print('Cummulative freq:', freq_cum_KV)

#percentage

percent_KV = (freq_KV / freq_KV.sum())*100
print('Percentage: ', percent_KV)


#Cummulative Percentage
percent_cum_KV = percent_KV.cumsum()
print('Cummulative Percentage:\n', percent_cum_KV)

#chart for data precentation: bar - pie - bar(line)
#bar: frequency

#fig,(ax1, ax2, ax3) = plt.subplots(1,3)
#fig.suptitle('Bieu do trinh bay du lieu')

#ax1. bar(freq_KV.index, freq_KV[:])

#explodes = (0.1, 0, 0)
#ax2.pie(percent_KV[:], explode = explodes, labels = percent_KV.index)

#ex3.bar(percent_cum_KV.index, percent_cum_KV[:])

# ve bieu do tong hop theo nhom du lieu

#gr_df_kt_kv = df.loc[df['GT']=='F'].groupby(['KV','KT']).size() # loc gioi tinh = nu
#print(gr_df_kt_kv)

#gr_df_kt_kv.unstack().plot(kind='bar', rot=50)

#mo ta du lieu

print(df['T1'].describe()) #std = do lech chuan

print(df.groupby('KV')['T1'].describe().unstack(1))

#ve boxplot
df[['T1']].boxplot()
#hitogram
df['T1'].plot.hist(density= True)

print(df['T1'].skew())

print(df['T1'].kurtosis())

df.hist(column='T1', by='KV', bins =20)

df.groupby('KV').plot.scatter(x='T1', y='DH1')