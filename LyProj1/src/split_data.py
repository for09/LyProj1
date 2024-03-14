from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
df = pd.read_csv('E:\LyProj1\data\processed\preprocessed_data.csv')









# def split_data(X,y,n_split=5):
    
#     tscv = TimeSeriesSplit(n_splits = n_split)

#     X_train_list=[]
#     X_test_list=[]
#     y_train_list=[]
#     y_test_list =[]

#     for train_index , test_index in tscv.split(X):
#         X_train, X_test = X.iloc[train_index], X.iloc[test_index]
#         y_train, y_test = y.iloc[train_index], y.iloc[test_index]
#         X_train.reset_index(drop = True,inplace = True)
#         X_test.reset_index(drop = True,inplace = True)
#         y_train.reset_index(drop = True,inplace = True)
#         y_test.reset_index(drop = True,inplace = True)
#         X_train_list.append(X_train)
#         X_test_list.append(X_test)
#         y_train_list.append(y_train)
#         y_test_list.append(y_test)

#     print(X_train_list)
#     print(y_train_list)
#     print(X_test_list)
#     print(y_test_list)
#     return X_train_list,X_test_list,y_train_list,y_test_list
# X = df[['Date','SMA_20','EMA_30','RSI','OBV']]
# y = df[['Date','signal_RSI','signal_OBV','signal_SMA','signal_EMA']]
# X_train_list,X_test_list,y_train_list,y_test_list =split_data(X,y,n_split = 5)