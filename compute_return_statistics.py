import yfinance as yf
import numpy
import matplotlib.pyplot as plt

#===Get Tickers===#
ticker_symbols = ['CACI', 'RTX', 'LMT', 'LLL']

#===Compute Mean===#
mean_vector = numpy.zeros(len(ticker_symbols), dtype=float)
all_returns = []
for t, ticker_symbol in enumerate(ticker_symbols):

    #===Get Price Data===#
    ticker_data = yf.Ticker(ticker_symbol)
    ticker_history = ticker_data.history(period='1d', start='2010-1-1', end='2020-1-25')
    prices = numpy.asarray(ticker_history['Close'])
    dates = ticker_history.index[1::]

    #===Compute Returns===#
    returns = []
    for p in range(1, len(prices)):
        retrn = (prices[p] - prices[p-1])/prices[p-1]
        returns.append(retrn)
    num_returns = len(returns)
    all_returns.append(returns)
        
    #===Compute Mean===#
    mean = numpy.mean(returns)
    mean_vector[t] = mean       
mean_vector = numpy.asmatrix(mean_vector).T        

#===Compute Covariance===#
for n in range(num_returns):
    return_vector = numpy.asmatrix([all_returns[k][n] for k in range(len(ticker_symbols))]).T
    if (n==0):
        cov = (return_vector-mean_vector)*(return_vector-mean_vector).T
    else:
        cov += (return_vector-mean_vector)*(return_vector-mean_vector).T
cov /= (float(num_returns)-1.0) 

#===Print===#
print("Mean Returns: \n", mean_vector)           
print("Return Covariance: \n", cov)           

