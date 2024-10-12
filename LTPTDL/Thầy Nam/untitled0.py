# -*- coding: utf-8 -*-
"""
Created on Sat May 29 15:46:22 2021

@author: PC
Theo quy định của BGD
KQ điểm sàn (DH1 + DH2 +DH3)
KQ >= 15 Đạt sàn
KQ < 15  Không đạt sàn
Nếu như biết T5, T6: continous data (số thực, liên tục) 
             GT, KV, DT, KT: Categorical data (dữ liệu phân loại)

=> Học sinh có đạt sàn hay không dựa theo dữ liệu lịch sừ

=> Xây dựng mô hình Decision Tree => Decision System
=> Phân loại dữ liệu, input ở nhóm dữ liệu nào

KQ = f(T5, T6, GT, KV, DT, KT)
"""

import pandas as pd
import numpy as np

#Bước 1: Nạp dữ liệu
df = pd.read_csv('dulieuxettuyendaihoc.csv', header = 0, delimiter = ',')
print(df.head(5))

df['DT'].fillna('K', inplace = True) # làm đầy bằng giá trị K
df.DT = df.DT.astype(str) #ép kiểu thành string


df.loc[(df['DH1']+df['DH2']+df['DH3'])<15.0, 'KQ'] = 'Không đạt'
df.loc[(df['DH1']+df['DH2']+df['DH3'])>=15.0, 'KQ'] = 'Đạt'

print(df[['KQ']])

print(df[['T5', 'T6', 'GT', 'KV', 'DT', 'KT', 'KQ']])

#Encoding dữ liệu
#String -> số
#One-hot-encoding

#Mutal

print(np.unique(df['GT']))
map_gt = {'F':0, 'M':1}
df['GT'] = df['GT'].map(map_gt)

print(np.unique(df['KV']))
map_kv = {'1':0, '2':1, '2NT':2}
df['KV'] = df['KV'].map(map_kv)

print(np.unique(df['DT']))
map_dt = {'1.0':0, '6.0':1, 'K':2}
df['DT'] = df['DT'].map(map_dt)

print(np.unique(df['KT']))
map_kt = {'A':0, 'A1':1, 'B':2, 'C':3, 'D1':4}
df['KT'] = df['KT'].map(map_kt)

print(np.unique(df['KQ']))
map_kq = {'Không đạt':0, 'Đạt':1}
df['KQ'] = df['KQ'].map(map_kq)

print(df[['T5', 'T6', 'GT', 'KV', 'DT', 'KT', 'KQ']])

# --> Phân loại
#Input
X = df[['T5', 'T6', 'GT', 'KV', 'DT', 'KT']]
#Output
y = df.KQ

#Chia ra làm 2 tập Train, Test => Sinh viên tự chia

from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier()

dtree = dtree.fit(X,y)

#Xuất kết quả của cây mô hình ra file: mytree_p2.png
from sklearn import tree

data_tree = tree.export_graphviz(dtree, out_file=None, feature_names = X.columns)

import pydotplus
graph = pydotplus.graph_from_dot_data(data_tree)
graph.write_png('mytree_p2.png')

# Input: T5=9.0, T6=7.0, GT=F, DT=6.0, KV=1, KT=D1
# Câu hỏi: đạt sàn ko?
# Encoder => (9.0, 7.0, 0, 1, 0, 4) --> Feature Vector
print(dtree.predict([[9.0, 7.0, 0, 1, 0, 4]]))


# Input: Học sinh An: T5=5.0, T6=7.0, GT=F, DT=6.0, KV=1, KT=C
# Encoder => (5.0, 7.0, 0, 1, 0, 3)
print(dtree.predict([[5.0, 7.0, 0, 1, 0, 3]])) #đạt

# Input: Học sinh Bình: T5=8.0, T6=5.0, GT=F, DT=K, KV=2NT, KT=A
# Encoder => (8.0, 5.0, 0, 2, 2, 3)
print(dtree.predict([[8.0, 5.0, 0, 2, 2, 3]])) #không đạt

#Validation (thẩm định)
#Decision Tree: Confusion, Accuracy

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

y_pred = dtree.predict(X)
print('Confusion matrix: ', confusion_matrix(y, y_pred))

#Sinh viên tự tìm hiểu cách đọc Confusion Matrix
# --> để đánh giá chất lượng của cây tin cậy

print('Accuracy: ', accuracy_score(y, y_pred)*100)


data = df[['DH1', 'DH2', 'DH3']]

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 4).fit(data)

print(kmeans.cluster_centers_)
print(kmeans.labels_[:])

df['Nhom'] = kmeans.labels_[:]

print(df[['DH1', 'DH2', 'DH3', 'Nhom']])

# Truc quan dữ liệu
data_analysis = df[['DH1', 'DH2', 'DH3', 'Nhom']]
print(data_analysis)

gr_count = data_analysis.groupby(['Nhom']).size()
gr_count.plot.bar()

gr_min = data_analysis.groupby(['Nhom'])['DH1', 'DH2', 'DH3'].min()
gr_min.plot(kind='bar')

gr_mean = data_analysis.groupby(['Nhom'])['DH1', 'DH2', 'DH3'].mean()
gr_mean.plot(kind='bar')

gr_max = data_analysis.groupby(['Nhom'])['DH1', 'DH2', 'DH3'].max()
gr_max.plot(kind='bar')

gr_max = data_analysis.groupby(['Nhom'])['DH1', 'DH2', 'DH3'].std()
gr_max.plot(kind='bar')

