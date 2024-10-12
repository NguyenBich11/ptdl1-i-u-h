# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:34:38 2021

@author: PC
"""
#DH3

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn import datasets, linear_model, metrics
from sklearn.model_selection import train_test_split

#Bước 1: Nạp dữ liệu
df = pd.read_csv('dulieuxettuyendaihoc.csv', header = 0, delimiter = ',')
print(df.head())


#Bước 2: Xử lý missing, noise and error
print(df['DH3'].isna().sum()) #==> Kết quả 0


#Bước 3: Phân tích định lượng biến DH3
# Describe data DH3
print('---------------------------')
print('Mô tả dữ liệu: ')
print(df['DH3'].describe())


#Bước 4: Vẽ Biểu Đồ
print('---------------------------')
print('Biểu đồ: ')
# Plot data
fig = plt.figure() # Khai báo đồ họa

# Histogram
ax = fig.add_subplot(2,1,1) # First row sub-plot 
df[['DH3']].hist(bins=10, ax = ax)

# Box chart
ax = fig.add_subplot(2,1,2) # Second row sub-plot
df.boxplot(column=['DH3'], vert=False, ax = ax)
plt.show()


# Bước 5 Phân tích tương quan biến
print('---------------------------')
print('Hệ số tương quan giản dầm: ')

# Trả về 1 dataframe có các correlation của các biến trong df
Df_corr = df.corr()
#print(Df_corr)

# Tìm ra cột có tương quan cao nhất so với DH3 và xếp giảm dần
DH3_corr = Df_corr['DH3'].sort_values(ascending=False)
print(DH3_corr) #H2 tương quan cao nhất, không tính cột DT

# max(corr_cf) < 0.5 --> Tiến hành gom cụm ở bước 6 

corr_cf = df['DH3'].corr(df['H2'])
print(corr_cf)



#Bước 6: Phân cụm K-Means --> số cụm là 3 thì cục bộ cụm có tương quan tốt nhất
print('---------------------------')
print('Tâm cụm: ')
kmeans = KMeans(n_clusters=3).fit(df[['H2','DH3']])
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['H2'], df['DH3'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()

# Bước 7: Phân tích hồi quy Linear Regression
#Input: H2
#Output: DH3
# Model: DH3 = slope * H2 + interception


# splitting X and y into training and testing sets: train 80% and test 20%
X_train, X_test, y_train, y_test = train_test_split(df[['H2']], df[['DH3']], test_size=0.2,random_state=1)
print(X_train)

# create linear regression object
reg = linear_model.LinearRegression()
 
# train the model using the training sets
reg.fit(X_train, y_train)
 
print('Intercept', reg.intercept_)
print('Coefficients: ', reg.coef_)


# Bước 8: Đánh giá mô hình

# variance score: 1 means perfect prediction đánh giá độ chính xác của mô hình trên tập test
print('Variance score tập test: {}'.format(reg.score(X_test, y_test)))
# variance score: 1 means perfect prediction đánh giá độ chính xác của mô hình trên tập train
print('Variance score tập train: {}'.format(reg.score(X_train, y_train)))


# plot for residual error
 
## setting plot style
plt.style.use('fivethirtyeight')
 
## plotting residual errors in training data
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, color = "green", s = 10, label = 'Train data')
 
## plotting residual errors in test data
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test, color = "blue", s = 10, label = 'Test data')
 
## plotting line for zero residual error
plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 2)
 
## plotting legend
plt.legend(loc = 'upper right')
 
## plot title
plt.title("Residual errors")
 
## method call for showing the plot
plt.show()


#Nhận Xét: Biến H2 có độ tương quan với DH3 lên đến 0.388977 nhưng khi đưa vào mô hình dự đoán thì 
#nhận được score_test là 0.3018018 và score_train là 0.10921 mô hình vẫn chưa khả quan


'''

# variance score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(X_test, y_test)))

# plot for residual error
 
## setting plot style
plt.style.use('fivethirtyeight')
 
## plotting train data 
plt.scatter(X_train, y_train, color = "green", s = 10, label = 'Actual Train Data')
 
## plotting model on train data 
plt.scatter(X_train, reg.predict(X_train), color = "red", s = 10, label = 'Predictive Train Data')
 
## plotting train data 
plt.scatter(X_test, y_test, color = "blue", s = 10, label = 'Actual Test Data')
 
## plotting model on test data 
plt.scatter(X_test, reg.predict(X_test), color = "orange", s = 10, label = 'Predictive Test Data')

## plotting line 
plt.hlines(y = 0, xmin = 0, xmax = 25, linewidth = 2)
 
## plotting legend
plt.legend(loc = 'upper right')
 
## plot title
plt.title("Visualize")
 
## method call for showing the plot
plt.show()

'''


