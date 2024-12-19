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
