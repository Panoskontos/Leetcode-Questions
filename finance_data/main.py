'''
Use alpha vantage to get stock data and plot it in a graph
'''
# make the imports
import requests
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt



API_KEY = "09KQUJEYIEJ5FKW4"

def get_stock_data(symbol, api_key):
    '''
    Get stock data from alpha vantage
    '''
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&apikey={}'.format(symbol, api_key)
    r = requests.get(url)
    data = r.json()
    return data

def plot_stock_data(df):
    '''
    Plot the stock data
    '''
    # get the data
    data = df['Time Series (5min)']
    # create a dataframe
    df = pd.DataFrame(columns=['time', 'open', 'high', 'low', 'close'])
    # populate the dataframe
    for k,v in data.items():
        date = dt.datetime.strptime(k, '%Y-%m-%d %H:%M:%S')
        data_row = [date.date(), float(v['1. open']), float(v['2. high']),
                    float(v['3. low']), float(v['4. close'])]
        series = pd.Series(data_row, index=df.columns, name=date)
        df = df.append(series)
    # sort by time
    df.sort_values('time', inplace=True)
    # plot the data
    plt.figure(figsize=(16,8))
    plt.title('Stock Price')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.plot(df['time'], df['close'])
    plt.show()



if __name__ == "__main__":
    df = get_stock_data('AAPL', API_KEY)
    # print df 'Time Series (5min)' key and plot the data
    print(df['Time Series (5min)'])
    plot_stock_data(df)
    
        
    
