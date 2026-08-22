import pandas as pd
import yfinance as yf
import numpy as np

ticker = 'TSLA'

tkr = yf.Ticker(ticker)
df = tkr.history(period='5d')

print(df.head())
print("========================")

print(df['Close'])

print("========================")

print(pd.concat([df['Close'], df['Close'].shift(2)], axis=1, keys = ['Close', '2DaysShift']))

print("------------------------")
print((df['Close'] - df['Close'].shift(2)) / df['Close'].shift(2))
print("------------------------")
df['2daysRise'] = np.log(df['Close'] / df['Close'].shift(2))
print(df[['Close', '2daysRise']])
print("----------Скользящие окно--------------")
df['2daysAvg'] = df['Close'].shift(1).rolling(2).mean()
print(df[['Close', '2daysAvg']])

print("----------  Вычисление процентного изменения скользящего среднего  --------------")
df['2daysAvgRise'] = np.log(df['Close'] / df['2daysAvg'])
print(df[['Close', '2daysRise', '2daysAvgRise']])

print("----------  Многомерные временные ряды  --------------")
import pandas as pd
import yfinance as yf

stocks = pd.DataFrame()

tickers = ['MSFT', 'TSLA', 'GM', 'AAPL', 'ORCL', 'AMZN']

for ticker in tickers:
    tkr = yf.Ticker(ticker)

    hist = tkr.history(period='5d')
    hist = pd.DataFrame(hist[['Close']].rename(columns={'Close': ticker}))

    if stocks.empty:
        stocks = hist
    else:
        stocks = stocks.join(hist)

print(stocks)

print("----------  Обработка многмерных времных рядов  --------------")

stocks_to_keep = []
for i in stocks.columns:
    if stocks[stocks[i] / stocks[i].shift(1) < 0.97].empty:
        stocks_to_keep.append(i)
print(stocks_to_keep)
print("---")
print(stocks[stocks_to_keep])
print()
print("----------  Анали зависимости между переменными  --------------")

import yfinance as yf
import numpy as np

ticker = 'TSLA'
tkr = yf.Ticker(ticker)
df = tkr.history(period='1mo')

df = df[['Close', 'Volume']].rename(columns={'Close': 'Price'})

print(df)
print("---")
df['priceRise'] = np.log(df['Price'] / df['Price'].shift(1))
print(df)
print("---")
df['volumeRise'] = np.log(df['Volume'] / df['Volume'].shift(1))
print(df)
print("---")

print(df[abs(df['priceRise']) > 0.05])
print("==============================================================")
print(df['volumeRise'].mean().round(4))

print("==============================================================")
print(df[abs(df['priceRise']) > 0.05]['volumeRise'].mean().round(4))

print("==============================================================")

df['volumeSum'] = df['Volume'].shift(1).rolling(2).sum().fillna(0).astype(int)
print(df[abs(df['priceRise']) > 0.05].replace(0, np.nan).dropna())

print("==============================================================")
df['nextVolume'] = df['Volume'].shift(-1).fillna(0).astype(int)
print(df[abs(df['priceRise']) > 0.05].replace(0, np.nan).dropna())









