def transform_data(raw_data):
    # Extract 'data' field from JSON response
    records = raw_data.get('data', [])
    
    # Convert to DataFrame
    df = pd.DataFrame(records)
    
    # Select relevant columns
    df = df[['date', 'open', 'high', 'low', 'close', 'volume']]
    
    # Convert date to datetime format
    df['date'] = pd.to_datetime(df['date'])
    
    # Calculate daily price change
    df['price_change'] = df['close'] - df['open']

    return df

import json
import pandas as pd

# Specify the path to your JSON file
file_path = '/workspaces/AdvancedDataPipelineAutomation/marketstack_data.json'

# Read the JSON file into a variable
with open(file_path, 'r') as file:
    data = json.load(file)

# Print the contents of the variable
print(data)


# Test transformation
transformed_data = transform_data(data)
print(transformed_data.head())

import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# API Configuration
API_URL = "http://api.marketstack.com/v1/eod"
ACCESS_KEY = "91ae6b6717bce0ae3c9c98e05b1da3cc"
SYMBOL = "AAPL"

# Function to Fetch Data from API
def fetch_data():
    params = {
        'access_key': ACCESS_KEY,
        'symbols': SYMBOL,
        'limit': 100  # Fetch last 100 records
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data: {response.status_code}")
        return None

# Function to Transform Data
def transform_data(raw_data):
    records = raw_data.get('data', [])
    df = pd.DataFrame(records)
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values(by='date', inplace=True)
    return df

# Fetch and Transform Data
raw_data = fetch_data()
if raw_data:
    stock_data = transform_data(raw_data)

# Streamlit App Layout
st.title("Stock Market Dashboard")
st.sidebar.header("Options")

# Sidebar Filters
symbol = st.sidebar.text_input("Stock Symbol", value="AAPL")
if symbol != SYMBOL:
    SYMBOL = symbol
    raw_data = fetch_data()
    if raw_data:
        stock_data = transform_data(raw_data)

# Display Data Table
st.header("Stock Data Table")
st.write(stock_data)

# Plot Closing Prices Over Time
st.header("Closing Price Over Time")
plt.figure(figsize=(10, 5))
plt.plot(stock_data['date'], stock_data['close'], label='Close Price', color='blue')
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.title(f"{SYMBOL} Closing Prices")
plt.legend()
st.pyplot(plt)

# Add Additional Visualizations (e.g., Volume Trends)
st.header("Trading Volume Over Time")
plt.figure(figsize=(10, 5))
plt.bar(stock_data['date'], stock_data['volume'], color='orange')
plt.xlabel("Date")
plt.ylabel("Volume")
plt.title(f"{SYMBOL} Trading Volume")
st.pyplot(plt)
