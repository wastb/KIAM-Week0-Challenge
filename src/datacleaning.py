
import pandas as pd

def process_data(data):
    # Ensure 'Timestamp' column exists before converting to datetime format
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    
    # Remove rows where all values are missing
    data.drop('Comments', axis=1, inplace=True)
    
    # Apply absolute values to all columns (only for numeric values)
    data = data.applymap(lambda x: abs(x) if isinstance(x, (int, float)) else x)
    
    # Return the cleaned DataFrame
    return data



