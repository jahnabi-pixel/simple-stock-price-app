import yfinance as yf
import streamlit as st
import pandas as pd

st.title("Interactive Stock Price Viewer")

# Dropdown of popular stocks
stock_options = {
    "Google": "GOOGL",
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Reliance (India)": "RELIANCE.NS",
    "Infosys (India)": "INFY.NS"
}

selected_stock = st.selectbox("Select a Stock", options=list(stock_options.keys()))
tickerSymbol = stock_options[selected_stock]

# Date range inputs
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2023-01-01"))

# Fetch data
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start=start_date, end=end_date)

# Display data
st.subheader(f"Closing Price of {selected_stock}")
st.line_chart(tickerDf.Close)

st.subheader(f"Trading Volume of {selected_stock}")
st.line_chart(tickerDf.Volume)
