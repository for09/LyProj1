import pandas as pd
import numpy as np


df = pd.read_csv('E:/LyProj1/data/raw/data.csv')

def calculate_rsi(series , window = 15):
    #calculating price change
    price_diff = series.diff(1)
    price_diff.dropna(inplace = True)

    positive = price_diff.copy()
    negative  = price_diff.copy()

    #calculate gain and losses 
    positive[positive<0] = 0
    negative[negative>0] = 0
    
    #calculate avg gain and loss over specified time window
    avg_gain = positive.rolling(window=window).mean()
    avg_loss = abs(negative.rolling(window=window).mean())

    # To solve devide by 0 error, make the number = 0.00000000001 
    avg_loss = avg_loss.replace(0,1e-10)

    #calculating relative strength (RS)
    rs = avg_gain / avg_loss
    #calculating RSI
    rsi = 100.0 - (100.0 /(1+rs))

    return rsi



def rsi_str(df,ov_sol = 30,ov_bo = 70):
    df['buy_signal'] = np.where(df['RSI'] < ov_sol,1,0)
    df['sell_signal'] = np.where(df['RSI'] > ov_bo,-1,0)
    df['signal'] =np.where((df['buy_signal'] == 1) & (df['sell_signal'] == 0),1,0)
    df['signal'] =np.where((df['sell_signal'] == -1) & (df['buy_signal'] == 0),0,df['signal'])
    return df

df.reset_index(drop = True,inplace =True )
df['RSI'] = df.groupby('company_name')['Adj Close'].apply(calculate_rsi).reset_index(drop = True)
df = rsi_str(df)
df.index = df['Date']

df.drop('Date' ,axis = 1 , inplace = True)
print(df.head(25))
df.to_csv('E:/LyProj1/data/processed/RSI.csv')