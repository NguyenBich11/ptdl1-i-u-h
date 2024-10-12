#cau 3
import pandas as pd
df = pd.read_csv('dulieuxettuyendaihoc.csv',header=0,delimiter=',')
print(df.head(10))
print(df.tail(10))

#cau 4
print(df['T1']) # values(series)
print(df[['T1']]) #datafram(column)
print(df[['T1','L1']]) #print 2 cot

#cac gia tri thieu cua DT
missignDT = df['DT'].isna().sum()
print(missignDT)
#dien vo cac cho thieu la 0
df['DT'].fillna(0, inplace = True)
print(df['DT'])

#cau 5
missignT1 = df['T1'].isna().sum()
print(missignT1)
df['T1'].fillna(df['T1'],inplace = True)

#cau 6
df[['L1','L2','L3']] = df[['L1','L2','L3']].fillna(df[['L1','L2','L3']].mean())
print(df[['L1','L2','L3']])

#cau 7
df['TBM1'] = (df['T1']*2 + df['L1'] + df['H1'] + df['L1'] + df['S1'] + df['V1']*2 + df['X1'] +df['D1'] + df['N1'])/10

print (df[['TBM1']])

df['TBM2'] = (df['T2']*2 + df['L2'] + df['H2'] + df['L2'] + df['S2'] + df['V2']*2 +df['X2'])

print (df[['TBM2']])

df['TBM3'] = (df['T3']*2 + df['L3'] + df['H3'] + df['L3'] + df['S3'] + df['V3']*2 +df['X3'])

print (df[['TBM3']])

#cau 8
df.loc[df['TBM1'] < 5,'XL1'] = 'Y'
print(df[['TBM1','XL1']])
df.loc[(df['TBM1'] >= 5.0) & (df['TBM1'] < 6.5), 'XL1'] = 'TB'
df.loc[(df['TBM1'] >= 6.5) & (df['TBM1'] < 8.0), 'XL1'] = 'K'
df.loc[(df['TBM1'] >= 8.0) & (df['TBM1'] < 9.0), 'XL1'] = 'G'
df.loc[df['TBM1'] >= 9.0,'XL1'] = 'XS'

print(df[['TBM1','XL1']])

#cau 9
#x_new=[[(x_old-min_old):(max_old-min_old)]*(max_new-min_new)]+min_new

df['US_TBM1']=((df['TBM1']-0)/(10.0-0)*(4.0-0))+0
print(df['US_TBM1'])




