# #!/bin/
# # import streamlit as st
# import matplotlib.pyplot as plt
# import requests
# from bs4 import BeautifulSoup
#
# # def stock_price():
# stock_url = "https://finance.yahoo.com/quote/FB?p=FB"
#
# page = requests.get(stock_url)
# print(page)
#
# soup = BeautifulSoup(page, "html.parser")
# price = soup.f

import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""" 
# Stock Price App
""")
# Enter the stock code
tickerSymbol = st.text_input(" Enter the ticker symbol of company", "NIO")
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
