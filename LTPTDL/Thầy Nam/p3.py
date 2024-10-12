# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 05:58:42 2021

@author: PC

Dựa vào điểm thi năm 2021 - giả sử trường đh iuh cần tuyển những học sinh có
điểm thi sao cho phù ợp vs nhu cầu đào tạo của trường.

Trường IUH thấy rằng ban tuyển sinh ưu tiên DH3 tốt và DH1 vừa vừa
Hãy đưa ra khuyến nghị đề xuất các nhóm học sinh có kết quả phù hợp

Vậy thế nào là tốt? --> khá khá?
"""
import pandas as pd
import numpy as np

#Bước 1: Nạp dữ liệu
df = pd.read_csv('dulieuxettuyendaihoc.csv', header = 0, delimiter = ',')
print(df[['DH1', 'DH2', 'DH3']])

# Giải thuật gom cụm -> Kỹ thuật KMeans
# Tại sao cần gom cụm? Các phần tử cùng 1 cụm (nhóm)
#thì mối liên kết cao
# Dùng Kmeans phải biết số cụm

data = df[['DH1', 'DH2', 'DH3']] #Cần gom cụm 3 cột này

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 4).fit(data)
#biến kmeans lưu dsach các tâm cụm

print(kmeans.cluster_centers_)
print(kmeans.labels_[:]) #vs 1 cụm thì sẽ có 1 nhãn; 4 cụm 4 nhãn 0,1,2,3

df['Nhom'] = kmeans.labels_[:] #tạo cột nhóm r gán học sinh vào cột này

print(df[['DH1', 'DH2', 'DH3', 'Nhom']])

# Trực quan dữ liệu
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
#nhóm 1 học lệch vl, sự chêch lệch ở điểm DH3

#DH3 tốt tốt, DH1 khá khá?
#Xét trung bình, DH3 tốt thì nó sẽ thuộc nhóm 1 và 2
#                DH1 khá thì nó sẽ thuộc nhóm 2 và 3.
