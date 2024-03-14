import datetime
import data_ingestion
import feature_engineering
import data_preprocessing
import split_data
import model
def main():
    print('Heelo 1st')
    tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'JNJ']
    # Set up End and Start times for data grab (last year)
    end = datetime.datetime.now()
    start = datetime.datetime(end.year - 1, end.month, end.day)
    company_data = data_ingestion.fetch_stock_data(tech_list, start, end)
    company_names = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON", "J&J"]
    print('Heelo 2st')
    df = data_ingestion.add_company_name(company_data, company_names)
    df.to_csv("E:/LyProj1/data/raw/data.csv")
    print('Heelo 3st')
    data = feature_engineering.feature_engineering(df)
    data.to_csv('E:\LyProj1\data\processed\\feature_engineered.csv')
    print('Heelo 4st')
    print(data.columns)
    df = data_preprocessing.data_prepro(data)
    print(df)
    df.to_csv('E:\LyProj1\data\processed\preprocessed_data.csv')
    print('heelo 5th') 
    # X = df[['SMA_20','EMA_30','RSI','OBV']]
    # y = df[['signal_RSI','signal_OBV','signal_SMA','signal_EMA']]
    # X_train_list,X_test_list,y_train_list,y_test_list = split_data.split_data(X,y,n_split = 5)
    # company_name='GOOGLE'
    # indicator='OBV'
    # prediction,accuracy = model.knn_str(df,company_name=company_name,indicator=indicator)
    # print('recommendation for', company_name,'based on',indicator,':','buy' if prediction == 1 else 'sell')

if __name__ == '__main__':
    main()