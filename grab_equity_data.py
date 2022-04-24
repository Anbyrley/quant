import yfinance as yf

#===Choose Symbol===#
ticker_symbol = 'AAPL'

#===Get Data===#
ticker_data = yf.Ticker(ticker_symbol)

#===Get Historical Data===#
ticker_history = ticker_data.history(period='1d', start='2010-1-1', end='2020-1-25')
print(ticker_history)

#===Get Company Info===#
ticker_info = ticker_data.info
print(ticker_info)

#===Get Calendar===#
ticker_calendar = ticker_data.calendar
print(ticker_calendar)

#===Get Recommendations===#
ticker_recommendations = ticker_data.recommendations
print(ticker_recommendations)

#===Get Mid Price===#
high_price = ticker_history['High']
low_price = ticker_history['Low']
mid_price = 0.5*(high_price + low_price)
print(mid_price)
