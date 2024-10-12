# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:39:07 2021

@author: Asus
"""

import pandas as pd


#Bài toán: Xây dựng mô hình hồi quy tuyến tính dự báo điểm thi DH1 
#dựa trên các điểm Lý trong 6 học kỳ của của cấp trung học phổ thông 
#Input: L1, L2, L3, L4, L5L6 (Biến độc lập)
#Output: L6 (Biến phụ thuộc)
#Mô hình (Model): f(L1, L2, L3, L4, L5)
df = pd.read_csv('dulieuxettuyendaihoc.csv',header=0,delimiter=',');
print(df.head(5))

X = df[['L1','L2','L3','L4','L5']]
y = df.L6
print(X.head(10))
print(y.head(10))

import statsmodels.api as sm
X_train=sm.tools.add_constant(X)

model = sm.OLS(y,X_train).fit()
predictions = model.predict(X_train)
print(model.summary())

'''
#1. Mức độ giải thích L6 dựa trên L1,L2,L3,L4,L5
#Trả lời : --> ?

#2. Mô hình này có ý nghĩa (thống kê)
#trong thực tiễn hay không và tại sao ?
#Trả lời : Có --> Vì <0.05

#3. Ý nghĩa thống kê của cấc tham số trong mô hình hồi quy
#những biến số có nghĩa : L5 (Dựa vào cột P>|t|, biến nào <0.05 thì có ý nghĩa)
#những biến số không có nghĩa (ít) : L1, L2, L3, L4
#mô hình : 
L6 = 2.5213 + 0.1230*L1 +  0.1625*L2 + 0.0425*L3 + 0.0756 *L4 + 0.3140 *L5

#4. Kiểm định hiện tượng tự tương quan
#Dựa vào Durbin-Watson : 
<1 : tương quan nghịch (Không tin cậy)
1<x<3 : không tương quan (Tin)
>3 : tương quan thuận (Không tin cậy)
Trả lời : Kết quả của mô hình có thể tin cậy được, 1 <  2.248 < 3 : Không tương quan : Tin cậy được

#5. Hiện tượng đa cộng tuyến (VIF)
VIF > 10 : Đa cộng tuyến
VIF < 10 : Không đa cộng tuyến
#L1,L2,L3,L4,L5
#L1,L2 có tương quan tuyến tính => biểu diễn L1 theo L2
# => loại bỏ L1 hoặc L2
'''
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor

#Biểu diễn tương quan L6 theo L1,L2,L3,L4,L5
yy, XX = dmatrices('L6~L1+L2+L3+L4+L5' ,data = pd.concat([y,X],axis=1),return_type='dataframe')

vif =pd.DataFrame()

vif['ten bien']=XX.columns
vif['VIF']=[variance_inflation_factor(XX.values,i) for i in range(XX.shape[1])]
print(vif)

#Trả lời: Không có hiện tượng đa cộng tuyến trên các biến số L1,L2,L3,L4,L5 vì VIF < 10

#6. Kiểm định các biến ố có giá trị tin cậy, không có siai sót về đo lường
#Trả lời: Dữ liệu là dữ liệu thứ cấp --> tin cậy

#7. Kiểm tra phần dư (Residual ) có là phân phối chuẩn không
from scipy import stats
import seaborn as sns

sns.distplot(model.resid, fit=stats.norm)

# => Phân phối chuẩn (đường viền sát với các cột)

#sm.qqplot(model.resid, line='s')


#8. Phương sai của phần dữ không thay đổi theo từng biến số

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.plot_regress_exog(model, 'L2', fig=fig)

#Trả lời : L1 => phương sai của phần dư không thay đổi => tin cậy
#Kiểm tra tiếp L2,L3,L4,L5

#9. Đánh giá mô hình
import matplotlib.pyplot as plt
import numpy as np
Y_max=y.max()
Y_min=y.min()

ax = sns.scatterplot(model.fittedvalues,y)
ax.set(ylim=(Y_min,Y_max))
ax.set(xlim=(Y_min,Y_max))

ax.set_xlabel('L6 - Predicted value')
ax.set_ylabel('L6 - Actual value')

X_ref = Y_ref = np.linspace(Y_min,Y_max,100)
plt.plot(X_ref,Y_ref,color='red',linewidth=1)
plt.show()

from statsmodels.tools.eval_measures import rmse
print(rmse(y,model.fittedvalues))

#Những điểm màu xanh nằm sát với đường viền đỏ => ổn
#warnings.warn = 0.7705295665575391 <1 : Ổn

#10. Đánh giá mức độ đóng góp của các biến L1,L2,L3,L4,L5 vào mô hình
#Chuẩn hóa OLS --> Stanardization các Input và Output
#Khử Interception (Constant)
#Sử dụng Standarization : chuẩn hóa : z-score
#hông dùng normalization

#Normalization input vs output trước
X_norm=pd.DataFrame(stats.zscore(X),columns = X.columns)
X_norm=sm.add_constant(X_norm)

y_norm=pd.Series(stats.zscore(y),name = y.name)

mod_std=sm.OLS(y_norm,X_norm)
mod_std_result=mod_std.fit()
print(mod_std_result.summary())

#Tornado chart
coff = mod_std_result.params
coff = coff.iloc[(coff.abs() * -1.0).argsort()]

sns.barplot(coff.values, coff.index , orient='h')

#Trả lời: biến số nào có tác động mạnh vào mô hình
#Dựa vào cột P>|t| có L5 = 0.001 < 0.05 nên L5 có ý nghĩa, và tác động đến mô hình nhiều nhất
#Chưa chuẩn hóa : gọi L5 là có ý nghĩa
#Đã chuẩn hóa : gọi L5 là tác động lên
#Sắp xếp theo thứ tự tăng dần tác động của các biến, dựa vào độ dài (ghi chú)
#--> L3 -> L4 -> L1 -> L2 -> L5 (Dựa theo biểu đồ Tornado, căn cứ vào độ dài của thanh)



#11. Đặt ra: Tôi nên loại bỏ những tham số nào để cho mô hình đạt được tối ưu về hiệu suất trong dự báo biến DH1
#Nên giữ biến nào, bỏ biến nào ?
#L6 = 2.5213 + 0.1230*L1 +  0.1625*L2 + 0.0425*L3 + 0.0756 *L4 + 0.3140 *L5
from sklearn.linear_model import LinearRegression
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs

mod = LinearRegression()
mod.fit(X,y)

coef = pd.concat([pd.Series(X.columns),pd.Series(mod.coef_)],axis =1)
coef.columns=['variable','cofficient']
print(coef)

sfs = SFS(
    mod,
    k_features='best',
    forward=False,
    floating = False,
    scoring='r2',
    cv = 30)

sfs = sfs.fit(X,y)

plot_sfs(sfs.get_metric_dict(), kind = 'std_err')
plt.grid()
plt.show()

print(sfs.subsets_[3].get('feature_names'))
#1 giá trị : L5
#2 giá trị : L5 vs L4
#Dựa vào std error, thấp nhất thì giữ lại