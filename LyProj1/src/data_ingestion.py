import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_stock_data(tickers, start_date, end_date):
    
    company_data = []
    for stock in tickers:
        data = yf.download(stock, start_date, end_date)
        company_data.append(data)
    return company_data

def add_company_name(company_data, company_names):

    for company, name in zip(company_data, company_names):
        company["company_name"] = name
    merged_df = pd.concat(company_data, axis=0)
    return merged_df













# # The tech stocks we'll use for this analysis
# tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'JNJ']

# # Set up End and Start times for data grab (last year)
# end = datetime.now()
# start = datetime(end.year - 1, end.month, end.day)

# # Fetch stock data for tech stocks
# company_data = fetch_stock_data(tech_list, start, end)

# # Define company names
# company_names = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON", "J&J"]

# # Add company names to the DataFrame
# df = add_company_name(company_data, company_names)
# df.to_csv("E:/LyProj1/data/raw/data.csv")
# print(df.tail(10))