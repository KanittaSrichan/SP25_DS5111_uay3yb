import pandas as pd
import os

# File paths
wsj_path = '/home/ubuntu/SP25_DS5111_uay3yb/wsjgainers_norm.csv'
yahoo_path = '/home/ubuntu/SP25_DS5111_uay3yb/ygainers_norm.csv'

# Check if files exist and load data
data_frames = []
if os.path.exists(wsj_path):
    wsj_data = pd.read_csv(wsj_path)
    data_frames.append(wsj_data)
    print("WSJ data loaded successfully.")
else:
    print("WSJ data file not found.")

if os.path.exists(yahoo_path):
    yahoo_data = pd.read_csv(yahoo_path)
    data_frames.append(yahoo_data)
    print("Yahoo data loaded successfully.")
else:
    print("Yahoo data file not found.")

# Merge the dataframes if any are loaded
if data_frames:
    merged_data = pd.concat(data_frames, ignore_index=True)
    print(merged_data.head())
    # Optionally, save the merged data to a new CSV
    merged_data.to_csv('/home/ubuntu/SP25_DS5111_uay3yb/merged_gainers.csv', index=False)
    print("Merged data saved successfully.")
else:
    print("No data files available to process.")
