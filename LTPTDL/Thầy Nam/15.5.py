# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 08:18:26 2021

@author: PC

Xây dựng mô hình dự báo hồi quy để dự báo điểm thi DH1, dựa trên T1, H1, L1, S1, V1
Input: T1, H1, L1, S1, V1
Output: DH1
Model: DH1 = f(T1, L1, H1, S1, V1)
--> Linear Regression -> Hồi quy tuyến tính đa biến

"""

#Bước 1: Các thư viện cần thiết
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler

#Bước 2: Nạp dữ liệu chương trình
df = pd.read_csv('dulieuxettuyendaihoc.csv', header=0, delimiter=',')
print(df.head(10))

X = df[['T1', 'H1', 'L1', 'S1', 'V1']] #biến độc lập
y = df.DH1 #biến phụ thuộc

print(X)
print(y)

#Bước 3: Mô tả dữ liệu
summary_result = X.describe()
print(summary_result)

# Boxplot
X.boxplot()

# Profile plot
X.plot().legend(loc='center left', bbox_to_anchor=(1,0.5))

#Histogram
X.hist()

#Bước 4: Tương quan corralation arrange variable
print(X.cov()) #Hiệp phương sai
print(X.corr()) #Hệ số tương quan, chạy từ -1 tới 1

#Pair plot: Matrix scatter
#sns.pairplot(X, diag_kind='hist', kind='kde')

# Heatmap
sns.heatmap(X.corr(), vmax=1.0, square=False).xaxis.tick_top()
# Màu càng sáng là tương quan càng cao ( gần tiến tới 1.0)

#Bước 5: Chuẩn hóa dữ liệu --> Chuẩn hóa trên tập X

# 5.1: Standardisation (dời trục): Std của các biến nó lệch nhau nhiều qua
#và đơn vị của các biến khác nhau
# Dùng nhìu trong --> Phân loại tuyến tính, Linear regression, logistic regrestion
# Mean, std không lệch nhiều với lại do dữ liệu điểm thuộc thang điểm 10 sẵn r
#nên ko cần chuẩn hóa

##standardX = StandardScaler().fit_transform(X) #Biến đổi
##standardX = pd.DataFrame(standardX, index = X.index, columns = X.columns)

# Khi biến đổi dữ liệu có thể mất hết thông tin như chỉ số theo dòng, cột...
# Biến đổi thành dataframe sài cho dẽ

#--> StandardX như là input thay thế cho X

##print(standardX.describe())

# Đừng để ý mean, std nó về 1 hết kìa --> chuẩn hóa xong òi á

#5.2: Normalization: Biến đổi dữ liệu về đoạn nào đó (thường là khoảng [0, 1])
# X--> Linear combination (tổ hợp tuyến tính) --> strong scale parameter : not Gaussian distribution, k-nearst neighbor(KNM), artificial neural network
# strong scale là gia tăng giá trị tham số tính toán lên giá trị lớn --> không tối ưu
# Trong bài toán này thì k cần

#Bước 6: Xây dựng mô hình
# Lúc này thì Input thay đổi
# Gọi stand(X) = standard(x)
# Input: standard(X) --> standardX
# Output: DH1
# Model: DH1 = f(standardX)

#Nhưng do bài này ko cần chuẩn hóa nên INPUT OUTPUT DỮ NGUYÊN
#Input: T1, H1, L1, S1, V1
#Output: DH1
#Model: DH1 = f(T1, H1, L1, S1, V1)

from sklearn import datasets, linear_model, metrics
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=1)
print(X_train) #80 dòng tương ứng vs 80% của dữ liệu

reg = linear_model.LinearRegression()

reg.fit(X_train, y_train)

print('Intercept: ', reg.intercept_)
print('Coefficients: ')

coeff_df = pd.DataFrame(reg.coef_, X_train.columns, columns = ['Coefficient'])
print(coeff_df)

# Phương trình hồi quy tuyến tính của DH1
# DH1 = (T1, H1 ... V1)*slope + intercept
# DH1 = 0.069427*T1 - 0.101604*H1 - 0.102349*L1 + 0.242123*S1 - 0.166291*V1 + 3.98342

#Ví dụ: Một học sinh sắp thi đại học mà người ta biết đc điểm học kì 1 lớp 10 của các môn T, L, H, S, V
#lần lượt là: T=8, L=5, H=7, S=9, V=4. hãy dự báo điểm DH1 của học sinh này

DH1_pre = 0.069427*8 - 0.101604*7 - 0.102349*5 + 0.242123*9 - 0.166291*4 + 3.98342
print(DH1_pre)
# KQ điểm DH1 dự báo cảu học sinh này là 4.8298060000000005

# Bước 7: Đánh giá mô hình
print('Variance score tập test: {}'.format(reg.score(X_test, y_test)))
# Thấp quá, mô hình không ổn

print('Variance score tập train: {}'.format(reg.score(X_train, y_train)))
# Cũng rất thấp, mô hình không tốt

#Đánh giá bằng độ đo khác thì tự viết lại

# Bước 8: Phân tích hồi quy đa biến
import statsmodels.api as sm
X_train = sm.tools.add_constant(X_train)

model = sm.OLS(y_train, X_train).fit() #Đối với mô hình này thì output đặt trước, ngược vs sklearn
predictions = model.predict(X_train)
print(model.summary())

# Từ bảng ta có các chỉ số:

# Phương pháp Least Squares

# Quan sát trên tập train: 80

# Df Model: 5 biến độc lập

# Dùng Adj. R-squared thay vì R-squared, chỉ số này dùng để giải thích số phần trăm sự đa dạng (phong phú) của biến DH1 dựa vào 5 biến độc lập
#--> Vậy 5 biến độc lập trên chỉ giải thích đc 3.3% cho biến DH1 --> Mô hình xây dựng lên không thực tế do thông tin quá ít

# Prob (P-value, sig) < 0.05 mới có ý nghĩa --> Vậy mô hình này không có nghĩa rồi

# Durbin-Watson: [1,3] --> Dữ liệu thu thập tốt, tin cậy đc --> không có hiện tượng tự tương quan --> >3 tương quan dương, <1 tương quan nghịch
#Vậy dữ liệu này dường như không phải tự tạo ra (logic á). Nếu mà tự tạo ra thì thường 
#sẽ đi theo tuyến tính, theo chuỗi, tương quan cao.

# const tương ứng với interception

# p-value < 0.05 thì biến tham gia mới có ý nghĩa --> Tất cả đều lớn hơn 0.05 --> K có nghĩa

#[0.025      0.975] là khoảng tin cậy

#Skew: Độ lệch

#Kurtosis: Độ nhọn

#Từ bảng trên ta thấy có mình const tham gia vào phương trình
# --> DH1 = const <=> DH1 = interception



