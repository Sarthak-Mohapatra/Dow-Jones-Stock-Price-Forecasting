### Stock Price Prediction Dow Jones 30 companies (DJIA) - (2000-01-01 to 2020-18-05)

#### The companies/ stocks that make up the DJIA are as follows:

#### 3M (NYSE: MMM), American Express (NYSE: AXP), Apple (NASDAQ: AAPL), 
#### Boeing (NYSE: BA), Caterpillar (NYSE: CAT), Chevron (NYSE: CVX),         
#### Cisco (NASDAQ: CSCO), Coca-Cola (NYSE: KO), The Walt Disney Company (NYSE:DIS),           
#### DowDuPont (NYSE:DD), ExxonMobil (NYSE:XOM), General Electric (NYSE:GE),           
#### Goldman Sachs (NYSE:GS), The Home Depot (NYSE:HD), IBM (NYSE:IBM),             
#### Intel (NASDAQ:INTC), Johnson & Johnson (NYSE:JNJ), JPMorgan Chase (NYSE:JPM),            
#### McDonald's (NYSE:MCD), Merck (NYSE:MRK), Microsoft (NASDAQ:MSFT),               
#### Nike (NYSE:NKE), Pfizer (NYSE:PFE), Procter & Gamble (NYSE:PG),            
#### Travelers Companies (NYSE:TRV), United Technologies (NYSE:RTX), UnitedHealth (NYSE:UNH),  
#### Verizon (NYSE:VZ), Visa (NYSE:V), Wal-Mart (NYSE:WMT)

#### Web scrapping the above stocks from quandl.

#### Importing required libraries

import pandas as pd
import pandas_datareader as pdr
import datetime

start_date = datetime.datetime(2000, 1, 1)
end_date   = datetime.datetime(2020, 5, 25)

start_date_str = str(start_date.date())
end_date_str   = str(end_date.date())

DJIA_Stocks = ['MMM', 'AXP', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO', 'DIS', 'DD', 'XOM', 'GE', 'GS', 'HD', 'IBM', 
               'INTC', 'JNJ', 'JPM', 'MCD', 'MRK', 'MSFT', 'NKE', 'PFE', 'PG', 'TRV', 'UTX', 'UNH', 'VZ', 'V', 'WMT']


csv_path_to_save = 'D:/Datasets/DJIA_Stocks_Web-Scrapping'

##
## api_key has been masked as *****
##

for ticker in DJIA_Stocks:
    file_name = ticker + '_' + start_date_str + '_to_' + end_date_str + '.csv'
    print(file_name)
    data = pdr.DataReader(ticker, 'quandl', start_date, end_date, api_key = '*******************')
    print(data.shape)
    data.to_csv(csv_path_to_save + file_name)




