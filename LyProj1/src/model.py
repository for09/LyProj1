# import numpy as np
# import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier
# import split_data



# def knn_str(df,company_name,indicator):
#     company_data = df[df['company_name'] == company_name].copy()
#     X = company_data[[indicator]]
#     y= company_data[['signal_' + indicator]]
#     X_train_list,X_test_list,y_train_list,y_test_list = split_data(X,y)
    
#     knn = KNeighborsClassifier(n_neighbors=5)
#     all_prediction = []
  
#     for X_train,X_test,y_train,y_test in zip(X_train_list,X_test_list,y_train_list,y_test_list):
#         knn.fit(X_train,y_train)
#         prediction = knn.predict(X_test)
#         binary_prediction  = np.where(prediction >0.5 , 1,0)
#         all_prediction.extend(binary_prediction)
#     avg_pred = np.mean(binary_prediction,axis = 0)
    
#     final_pred = 1 if np.mean(avg_pred) >= 0.5 else 0

#     return final_pred

