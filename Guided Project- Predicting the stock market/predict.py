import pandas as pd
import datetime as dt
from sklearn.linear_model import LinearRegression


s = pd.read_csv('sphist.csv')
s['Date'] = pd.to_datetime(s['Date'])
s.sort('Date', inplace = True)

s['Av_5day'] = pd.rolling_mean(s['Close'], window = 5).shift(1)
s['Av_1yr'] = pd.rolling_mean(s['Close'], window = 365).shift(1)
s['ratio_dy'] = s['Av_5day']/s['Av_1yr']
s['AvVol_5day'] = pd.rolling_mean(s['Volume'], window = 5).shift(1)
s['AvVol_1yr'] = pd.rolling_mean(s['Volume'], window = 365).shift(1)

s = s[s['Date'] > dt.datetime(year = 1951, month = 1, day = 2)]
s.dropna(axis = 0, inplace = True)

train = s[s['Date'] < dt.datetime(year = 2013, month = 1, day = 1)]

test = s[s['Date'] >= dt.datetime(year = 2013, month = 1, day = 1)]

columns_use = ['Av_5day', 'Av_1yr', 'ratio_dy', 'AvVol_5day', 'AvVol_1yr']
y_train = train['Close']
y_test = test['Close']
lr = LinearRegression()

lr.fit(train[columns_use], y_train)
fitted = lr.predict(train[columns_use])

predictions = lr.predict(test[columns_use])
#using MAE for error measure.
mae = sum(abs(predictions - y_test)) / len(predictions)
print(mae)
