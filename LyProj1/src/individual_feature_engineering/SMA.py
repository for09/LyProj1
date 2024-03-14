import pandas as pd 
import numpy as np
df = pd.read_csv('E:/LyProj1/data/raw/data.csv')
def calculate_sma(df, ma_days):
    """
    Calculate Simple Moving Average (SMA) for each company in the DataFrame.
    
    Parameters:
    - df (pd.DataFrame): DataFrame containing stock data for multiple companies.
    - ma_days (list): List of integers representing the MA days.
    
    Returns:
    - df (pd.DataFrame): DataFrame with SMA columns added for each MA day.
    """
    for ma in ma_days:
        for company in df['company_name'].unique():
            column_name = f'SMA_{ma}'
            df.loc[df['company_name'] == company, column_name] = df.loc[df['company_name'] == company, 'Adj Close'].rolling(ma,center=True).mean()
    return df


def signals(df):
    df['buy_signal'] = np.where(df['Adj Close'] > df['SMA_20'],1,0)
    df['sell_signal'] = np.where(df['Adj Close'] < df['SMA_20'],1,0)

    df['signal_SMA'] = np.where((df['buy_signal'] == 1) & (df['sell_signal'] == 0),1,0)
    df['signal_SMA'] = np.where((df['sell_signal'] == 1) & (df['buy_signal'] == 0),0,df['signal_SMA'])
    return df


MA_day = [10,20,30,40,100]

df = calculate_sma(df,MA_day)
df = signals(df)
df.index = df['Date']
df.drop('Date' ,axis = 1 , inplace = True)
print(df.head(25))
df.to_csv('E:/LyProj1/data/processed/SMA.csv')
