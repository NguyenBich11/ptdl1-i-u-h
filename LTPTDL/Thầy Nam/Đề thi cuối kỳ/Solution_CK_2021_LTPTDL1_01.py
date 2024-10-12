# -*- coding: utf-8 -*-

#Created on Tue May 25 23:10:02 2021

# Import library
import pandas as pd
import seaborn as sns

# Read data
df = pd.read_csv("dulieuxettuyendaihoc.csv", header=0, delimiter=',')
print(df.head(5))

# Tạo cột trung bình
df['TB10_1'] = df.loc[: , "T1":"N1"].mean(axis=1)
df['TB10_2'] = df.loc[: , "T2":"N2"].mean(axis=1)
df['TB11_1'] = df.loc[: , "T3":"N3"].mean(axis=1)
df['TB11_2'] = df.loc[: , "T4":"N4"].mean(axis=1)
df['TB12_1'] = df.loc[: , "T5":"N5"].mean(axis=1)
df['TB12_2'] = df.loc[: , "T6":"N6"].mean(axis=1)
df['TB_DH'] = df.loc[: , "DH1":"DH3"].mean(axis=1)

# Finally, feature matrix for machine learning 
feature_df = df[['TB10_1', 'TB10_2', 'TB11_1', 'TB11_2','TB12_1', 'TB12_2', 'DH1']]

print(feature_df)

# Setting model: Input and Output
X = feature_df[['TB10_1', 'TB10_2', 'TB11_1', 'TB11_2','TB12_1', 'TB12_2']]
y = feature_df[['DH1']]

from sklearn.model_selection import train_test_split
# Split test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

print(X_train)

# Import library
import statsmodels.api as sm

# Build model
X_train = sm.tools.add_constant(X_train)
model = sm.OLS(y_train,X_train).fit() #y_train: output, X_train: input


# Trả lời cho các mục phân tích: #1, #2, #3, #4
print(model.summary())

# Trả lời cho các mục phân tích: #5
# VIF: Variance Inflation Factor (VIF) Explained
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor
yy, XX = dmatrices('DH1 ~ TB10_1+TB10_2+TB11_1+TB11_2+TB12_1+TB12_2', data=pd.concat([y_train, X_train], axis=1), return_type='dataframe')

vif = pd.DataFrame()
vif['variable'] = XX.columns
vif['VIF'] = [variance_inflation_factor(XX.values, i) for i in range(XX.shape[1])]
print(vif)

# Trả lời cho các mục phân tích: #6: các điểm số được thu thập nguồn chuẩn , dẫn đến điểm trung bình học kì là chính xác

# Trả lời cho các mục phân tích: #7
from scipy import stats
import seaborn as sns
print(model.resid.describe())
sm.qqplot(model.resid, line='s')

# Trả lời cho các mục phân tích: #8 (thử nghiệm trên từng biến số TB10_1, TB10_2, TB11_1, TB11_2, TB12_1, TB12_2)
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.plot_regress_exog(model, 'TB10_1', fig=fig)


# Đánh giá mô hình trên giá trị RMSE
from statsmodels.tools.eval_measures import rmse
import numpy as np

# Training dataset
predictions_train = model.predict(X_train)
rmse_train = rmse(y_train, predictions_train)
print("RMSE on train dataset: ",np.mean(rmse_train))

# Training dataset
X_test = sm.tools.add_constant(X_test)
predictions_test = model.predict(X_test)
rmse_test = rmse(y_test, predictions_test)
print("RMSE on test dataset: ",np.mean(rmse_test))
