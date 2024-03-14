import pandas as pd

df = pd.read_csv('E:/LyProj1/data/raw/data.csv')

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



df = cal_obv(df)
df['signal'] = df['signal'].fillna(1,inplace=True)
df.index = df['Date']
df.rename(columns={'signal' : 'signal_OBV'},inplace=True)
df.drop('Date' ,axis = 1 , inplace = True)
print(df[df.isna().any(axis = 1)].index)

print(df.head(25))
df.to_csv('E:/LyProj1/data/processed/OBV.csv')