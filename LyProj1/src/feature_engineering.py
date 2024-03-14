import pandas as pd 
import numpy as np
# df = pd.read_csv('E:/LyProj1/data/raw/data.csv')
global df
def feature_engineering(df):
    
# FUNCTION DEF
    df['Date'] = df.index
    #CALCULATE SMA
    
    def calculate_sma(df, ma_days):

        for ma in ma_days:
            for company in df['company_name'].unique():
                column_name = f'SMA_{ma}'
                df.loc[df['company_name'] == company, column_name] = df.loc[df['company_name'] == company, 'Adj Close'].rolling(ma).mean()
        return df

    #CALCULATE SIGNAL

    def signals(df):
        df['buy_signal'] = np.where(df['Adj Close'] > df['SMA_20'],1,0)
        df['sell_signal'] = np.where(df['Adj Close'] < df['SMA_20'],1,0)
        df['signal_SMA'] = np.where((df['buy_signal'] == 1) & (df['sell_signal'] == 0),1,0)
        df['signal_SMA'] = np.where((df['sell_signal'] == 1) & (df['buy_signal'] == 0),0,df['signal_SMA'])
        return df
    
#   FUNCTION CALL (SMA)
    
    MA_day = [20]
    df = calculate_sma(df,MA_day)
    df = signals(df)
    df.index = df['Date']


#EMA

# FUNCTION DEF 
    # CALCULATE EMA
    def calculate_company_ema(df, ma_day):
        for ma in ma_day:
            column_name = f'EMA_{ma}'
            df[column_name] = df.groupby('company_name')['Adj Close'].transform(lambda x: x.ewm(span=ma, adjust=False).mean())
        return df
    
    # CALCULATE SIGNAL
    
    def cal_ema(dff):
        dff['buy_signal'] = np.where(dff['EMA_10'] > dff['EMA_50'],1,0)
        dff['sell_signal'] = np.where(dff['EMA_10'] < dff['EMA_50'],1,0)
        dff['signal_EMA'] = np.where((dff['buy_signal'] == 1) & (dff['sell_signal'] == 0),1,0)
        dff['signal_EMA'] = np.where((dff['sell_signal'] == 1) & (dff['buy_signal'] == 0),0,dff['signal_EMA'])
        
        return dff
    
    # FUNCTION CALL(EMA)

    MA_day = [10,30,50]
    result_df = calculate_company_ema(df, MA_day)
    dff = cal_ema(result_df)
    df = df.assign(EMA_30 = dff['EMA_30'],signal_EMA = dff['signal_EMA'])

#RSI

# FUNCTION DEF 
    # CALCULATE RSI 
    
    def calculate_rsi(series , window = 15 ):
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
    
    # CALCULATE SIGNAL

    def rsi_str(df,ov_sol = 30,ov_bo = 70):
        df['buy_signal'] = np.where(df['RSI'] < ov_sol,1,0)
        df['sell_signal'] = np.where(df['RSI'] > ov_bo,-1,0)
        df['signal'] =np.where((df['buy_signal'] == 1) & (df['sell_signal'] == 0),1,0)
        df['signal'] =np.where((df['sell_signal'] == -1) & (df['buy_signal'] == 0),0,df['signal'])

        #################################################
        num_values_to_change = int(len(df) * 0.5)
        zero_indices = df[df['signal'] == 0].sample(num_values_to_change).index
        df.loc[zero_indices, 'signal'] = 1
        ###################################################


        return df


    # FUNCTION CALL (RSI)

    df.reset_index(drop = True,inplace =True )
    df['RSI'] = df.groupby('company_name')['Adj Close'].apply(calculate_rsi).reset_index(drop = True)
    df = rsi_str(df)
    df.rename(columns = {'signal' : 'signal_RSI'},inplace=True)
    df.index = df['Date']


    # def cal_bb(df):
    #     window = 20
    #     num_std = 2
    # # Calculate rolling mean and standard deviation
    #     df['SMA'] = df['Close'].rolling(window=window).mean()
    #     df['STD'] = df['Close'].rolling(window=window).std()
    #     # Calculate upper and lower bands
    #     df['UpperBand'] = df['SMA'] + (df['STD'] * num_std)
    #     df['LowerBand'] = df['SMA'] - (df['STD'] * num_std)
    #     # Determine signals
    #     df['Signal'] = 0
    #     df.loc[df['Close'] > df['UpperBand'], 'Signal'] = 1  # Buy signal
    #     df.loc[df['Close'] < df['LowerBand'], 'Signal'] = -1  # Sell signal
    #     return df

#OBV

# FUNCTION DEF 
    # CALCULATE OBV AND SIGNAL 

    def  cal_obv(df):
        data = pd.DataFrame()
        for company in df['company_name'].unique():
            company_subset = df[df['company_name'] == company].copy()
            #Calculating OBV

            company_subset['variation'] = company_subset['Close'].diff()
            company_subset = company_subset.dropna()

            company_subset['OBV'] = 0
            nele = len(company_subset['variation'])

            pvar = company_subset.columns.get_loc('variation')
            pvol = company_subset.columns.get_loc('Volume')
            pobv = company_subset.columns.get_loc('OBV')

            for i in range(nele):
                daily_change = company_subset.iloc[i,pvar]
                if daily_change > 0:
                    volume = company_subset.iloc[i,pvol]
                elif daily_change == 0:
                    volume = 0
                elif daily_change < 0:
                    volume = -company_subset.iloc[i,pvol]

                if i == 0 :
                    company_subset.iloc[i,pobv] = volume
                else:
                    company_subset.iloc[i,pobv] = company_subset.iloc[i-1,pobv] + volume


            # calculate signal
                    
            company_subset['signal'] = 0
            pclose = company_subset.columns.get_loc('Close')
            pobv = company_subset.columns.get_loc('OBV')
            psignal = company_subset.columns.get_loc('signal')

            for i in range(1,nele):
                current_price = company_subset.iloc[i,pclose]
                previous_price = company_subset.iloc[i-1,pclose]

                current_obv = company_subset.iloc[i,pobv]
                previous_obv = company_subset.iloc[i-1,pobv]


                if current_obv > previous_obv and current_price > previous_price:
                    company_subset.iloc[i,psignal] = 1
                
                elif current_obv < previous_obv and current_price <previous_price:
                    company_subset.iloc[i,psignal] = 0  

            # company_subset['daily returns'] = company_subset['Close']/company_subset['Close'].iloc[0] * 100 
            # company_subset['cumulative returns'] = (1. + company_subset['daily returns']).cumprod() * 100.
            data = pd.concat([data,company_subset], axis=0,ignore_index=True)

        return data
    
    # FUNCTION CALL(OBV) 
    
    data = cal_obv(df)
    data.rename(columns = {'signal' : 'signal_OBV'},inplace=True)
    

    #FINAL PROCESSING FUNCTIN RETURN
    return data


# data.to_csv('E:/LyProj1/data/processed/feature_engineered.csv')

