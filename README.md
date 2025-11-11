# Cointegration Pair Finder

This Python script identifies **cointegrated stock pairs** among S&P 500 companies — a common statistical arbitrage strategy used in **pairs trading**.  

It automatically downloads S&P 500 tickers from Wikipedia, fetches their historical price data from Yahoo Finance, and performs the **Engle-Granger cointegration test** on all possible stock pairs.

---

## 🚀 Features

- Scrapes **S&P 500 tickers** directly from Wikipedia  
- Downloads **historical price data** using [`yfinance`](https://github.com/ranaroussi/yfinance)  
- Computes **cointegration tests** for all stock combinations  
- Outputs the **top 10 pairs** with the lowest p-values (most likely to be cointegrated)  

---

## 🧠 How It Works

1. **Fetch S&P 500 tickers** from Wikipedia.  
2. **Download adjusted closing prices** for a chosen subset of tickers.  
3. **Run cointegration tests** (`statsmodels.tsa.stattools.coint`) for every pair.  
4. **Sort by p-value** to identify the strongest candidates.  

---

## 📦 Requirements

Install dependencies using:

```bash
pip install requests pandas yfinance statsmodels lxml
