import yfinance as yf
import numpy
import matplotlib.pyplot as plt


#===Get Price Data===#
ticker_symbol = 'AAPL'
ticker_data = yf.Ticker(ticker_symbol)
ticker_history = ticker_data.history(period='1d', start='2010-1-1', end='2020-1-25')
prices = numpy.asarray(ticker_history['Close'])
dates = ticker_history.index[1::]

#===Compute Returns===#
returns = []
for p in range(1, len(prices)):
    retrn = (prices[p] - prices[p-1])/prices[p-1]
    returns.append(retrn)
    
    
#===Plot===#
plt.figure(1)
plt.scatter(dates, returns)
plt.ylabel("Returns")
plt.xlabel("Dates")


plt.figure(2)
plt.hist(returns, bins=int(4.0*numpy.sqrt(len(returns))))
plt.ylabel("Counts")
plt.xlabel("Returns")

plt.show()   
