# bin/gainers/yahoo.py

import pandas as pd
from .base import GainerDownload, GainerProcess

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        super().__init__()

    def download(self, csv_path):
        print("Reading Yahoo CSV data from:", csv_path)
        try:
            df = pd.read_csv(csv_path)
        except Exception as e:
            raise ValueError(f"Error reading CSV file: {e}")
        return df

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        super().__init__()

    def normalize(self, df):
        # Ensure the input is a DataFrame
        assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
        df = df.copy()
        # Drop rows missing any critical columns
        df = df.dropna(subset=['Symbol', 'Price', 'Change', 'Change %'])
        # Normalize based on Yahoo's format
        df['symbol'] = df['Symbol']
        # Extract the price using split, remove commas, and convert to float
        df['price'] = (
            df['Price']
            .str.strip()
            .str.split()
            .str[0]
            .str.replace(',', '', regex=False)
        )
        try:
            df['price'] = df['price'].astype(float)
        except Exception as e:
            raise ValueError(f"Error converting price to float: {e}")
        df['price_change'] = df['Change']
        df['price_percent_change'] = df['Change %'].str.strip('+%')
        normalized_df = df[['symbol', 'price', 'price_change', 'price_percent_change']]
        # Ensure no null values remain
        assert not normalized_df.isnull().values.any(), "Null values found in Yahoo normalized data"
        return normalized_df

    def save_with_timestamp(self, df, output_path):
        df.to_csv(output_path, index=False)
        print(f"Yahoo data saved to {output_path}")
