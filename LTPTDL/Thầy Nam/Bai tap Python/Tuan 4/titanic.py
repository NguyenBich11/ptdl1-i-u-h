# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:41:33 2021

@author: H4-HTTT
"""
import pandas as pd
import seaborn as sns
def load_data():
    return pd.read_csv('titanic_disaster.csv', header=0, delimiter=',')

df=load_data()
print(df.head(10))

sns.heatmap(df.isnull(), yticklabels = False, cbar = False,cmap = 'viridis')