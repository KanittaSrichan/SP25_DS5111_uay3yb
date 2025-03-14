# bin/gainers/wsj.py

import pandas as pd
from .base import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        super().__init__()

    def download(self, csv_path):
        print("Reading WSJ CSV data from:", csv_path)
        try:
            df = pd.read_csv(csv_path)
        except Exception as e:
            raise ValueError(f"Error reading CSV file: {e}")
        return df

class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        super().__init__()

    def normalize(self, df):
        # Ensure the input is a DataFrame
        assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
        df = df.copy()
        # Normalize based on WSJ's format
        df['symbol'] = df['Unnamed: 0'].str.extract(r'\((.*?)\)')
        df['price'] = df['Last']
        df['price_change'] = df['Chg']
        df['price_percent_change'] = df['% Chg']
        normalized_df = df[['symbol', 'price', 'price_change', 'price_percent_change']]
        assert not normalized_df.isnull().values.any(), "Null values found in WSJ normalized data"
        return normalized_df

    def save_with_timestamp(self, df, output_path):
        df.to_csv(output_path, index=False)
        print(f"WSJ data saved to {output_path}")
