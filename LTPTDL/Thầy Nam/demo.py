# -*- coding: utf-8 -*-
"""
Created on Sat May 15 12:58:32 2021

@author: PC
"""

import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('dulieuxettuyendaihoc.csv')
X = df[['T1', 'H1', 'L1', 'S1', 'V1']]
Y = df.DH1
print(X)
print(Y)

#Bước 3: Mô tả dữ liệu
summary_result = X.describe()
print(summary_result)

# Boxplot
X.boxplot()

# Profile plot
X.plot().legend(loc='center left', bbox_to_anchor=(1,0.5))

#Histogram
X.hist()

#Bước 4
print(X.cov())
print(X.corr())

# Pair plot: Matrix Scatter
sns.pairplot(X, diag_kind='hist', kind='kde')

# Heatmap
sns.heatmap(X.corr(), vmax=1.0, square = False).xaxis.tick_top()