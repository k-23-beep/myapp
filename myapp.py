import yfinance as yf
import streamlit as st
import pandas as import pd

st.write("""
# Simple Stock Price App

Shown are the stock closing pricr and the volume of google

""")

tickersymbol = 'GOOGL'


tickerData = yf.Ticker(tickersymbol)

tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
