import requests
import pandas as pd
import yfinance as yf
from statsmodels.tsa.stattools import coint
import itertools
from io import StringIO


url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies' #link to list of stocks, can be changed
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    sp500 = pd.read_html(StringIO(response.text))[0]
    tickers = sp500['Symbol'].tolist()
else:
    raise Exception(f"Failed to fetch S&P 500 tickers, status code: {response.status_code}")

tickers = tickers[:50] #change the integer here to decide how many stocks you wish to check through


data = yf.download(tickers, start="2020-01-01", end="2025-08-31")  #adjust date as you wish


data = data['Close'].dropna(how='any')


results = []
for t1, t2 in itertools.combinations(tickers, 2):
    x = data[t1]
    y = data[t2]
    try:
        score, pvalue, _ = coint(x, y)
        results.append((t1, t2, pvalue))
    except Exception:
        continue


results_df = pd.DataFrame(results, columns=['Ticker1', 'Ticker2', 'pvalue'])
results_df = results_df.sort_values('pvalue')


print("\nTop 10 candidate pairs by lowest cointegration p-value:")
print(results_df.head(10))
