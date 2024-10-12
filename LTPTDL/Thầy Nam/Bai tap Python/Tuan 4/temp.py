import pandas as pd
#cau 3

column_names=["id","name","Age","weight","m0006","m0612","m1215","f0006","f0612","f1215"]

df = pd.read_csv('patient_heart_rate.csv', names = column_names)

print(df.head())

#cau 4
df[['Firstname','Lastname']] = df['name'].str.split(expand=True)
df = df.drop('name',axis=1)
print(df)

#cau 5
weight = df['weight']

for i in range (0,len(weight)):
    x = str(weight[i])
    
    if "los" in x[-3:]:
        x = x[:-3:]
        
        float_x=float(x)
        
        y=int(float_x/2.2)
        
        y=str(y)+"kgs"
        weight[i]=y
    print(df)
    
#cau 6
df.dropna(how="all", inplace = True)
print(df)

#cau 7
df = df.drop_duplicates(subset=['Firstname','Lastname','Age','weight'])
print(df)

#cau 8
df.Firstname.replace({r'[''\x000\x7F]+':''},regex=True,inplace=True)
df.Lastname.replace({r'[^\x00-\x7F]+':''},regex=True,inplace=True)

#cau 9
