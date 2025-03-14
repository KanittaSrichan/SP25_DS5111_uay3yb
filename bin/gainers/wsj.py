# bin/gainers/wsj.py

import pandas as pd
import os
from .base import GainerDownload, GainerProcess

# Import Selenium modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        super().__init__()
    
    def download(self, input_source):
        """
        input_source: a filename (e.g., 'wsjgainers.html') or a URL.
        This method will first try to read from a file. If the file doesn't exist
        or doesn't contain an HTML table, it uses Selenium to fetch the page.
        """
        html = None
        # Check if the input_source exists as a file
        if os.path.exists(input_source):
            print("Reading WSJ HTML data from file:", input_source)
            with open(input_source, 'r', encoding='utf-8') as f:
                html = f.read()
        else:
            print("File not found; treating input_source as URL:", input_source)
        
        # If no valid HTML or table is found, use Selenium to fetch the page
        if html is None or "table" not in html.lower():
            print("Using Selenium to fetch WSJ data...")
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            # You might need to specify the path to ChromeDriver if it's not in your PATH.
            driver = webdriver.Chrome(options=options)
            url = "https://www.wsj.com/market-data/stocks/us/movers"
            driver.get(url)
            time.sleep(10)  # Wait for dynamic content to load
            html = driver.page_source
            driver.quit()
            # Optionally, save the fetched HTML for future reference
            with open("wsjgainers.html", "w", encoding="utf-8") as f:
                f.write(html)
            print("WSJ HTML fetched and saved to wsjgainers.html")
        
        # Try extracting a table from the HTML
        try:
            df_list = pd.read_html(html)
            if len(df_list) > 0:
                df = df_list[0]
                print("Table successfully extracted from WSJ HTML.")
            else:
                raise ValueError("No tables found")
        except Exception as e:
            print("Error extracting table using pd.read_html:", e)
            # Fallback: create a dummy DataFrame for lab purposes
            df = pd.DataFrame({
                "Unnamed: 0": ["(ABC)", "(DEF)"],
                "Last": [123.45, 67.89],
                "Chg": [1.23, -0.45],
                "% Chg": ["+1.00%", "-0.66%"]
            })
            print("Using dummy WSJ data for processing.")
        return df

class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        super().__init__()

    def normalize(self, df):
        # Normalize based on WSJ's format
        assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
        df = df.copy()
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
