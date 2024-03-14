import pandas as pd
import numpy as np

df = pd.read_csv('E:/LyProj1/data/raw/data.csv')

def calculate_company_ema(df, ma_day):
    """
    Calculate Exponential Moving Average (EMA) for each company in the DataFrame.

    Parameters:
    - df (pd.DataFrame): DataFrame containing stock data for multiple companies.
    - ma_day (list): List of MA days for EMA calculation.

    Returns:
    - df (pd.DataFrame): DataFrame containing the original data with EMA columns appended.
    """
    for ma in ma_day:
        column_name = f'EMA_{ma}'
        df[column_name] = df.groupby('company_name')['Adj Close'].transform(lambda x: x.ewm(span=ma, adjust=False).mean())
    return df

# Example usage:
# Assuming df and MA_day are defined elsewhere in your code
# df = ...

def cal_ema(dff):
    dff['buy_signal'] = np.where(dff['EMA_10'] > dff['EMA_50'],1,0)
    dff['sell_signal'] = np.where(dff['EMA_10'] < dff['EMA_50'],1,0)
    dff['signal_EMA'] = np.where((dff['buy_signal'] == 1) & (dff['sell_signal'] == 0),1,0)
    dff['signal_EMA'] = np.where((dff['sell_signal'] == 1) & (dff['buy_signal'] == 0),0,dff['signal_EMA'])
    
    return dff
MA_day = [10,20,30,40,50]

# Call the calculate_company_ema function
result_df = calculate_company_ema(df, MA_day)
df = cal_ema(result_df)

# Print or use the resulting DataFrame as needed
df.index = df['Date']
df.drop('Date' ,axis = 1 , inplace = True)
print(df.tail(35))
# Print or use the resulting DataFrame as needed
df.to_csv('E:/LyProj1/data/processed/EMA.csv',index=False)
print(df.dtypes)
