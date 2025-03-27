import os
import time
import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service
from webdriver_manager.chrome import ChromeDriverManager
import tempfile  # Import tempfile for temporary user data directory

# Function to initialize ChromeDriver with proper options
def get_chrome_driver():
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    options.add_argument("--disable-gpu")  # Disable GPU acceleration (recommended for headless mode)
    options.add_argument("--no-sandbox")  # Disable sandboxing (required for certain environments)

    # Create a temporary user data directory each time
    user_data_dir = tempfile.mkdtemp()  # Create a new unique temp directory each time
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # Create a Service object and initialize ChromeDriver with it
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Create the Chrome driver instance
driver = get_chrome_driver()

from .base import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
    def download(self, csv_path):
        """
        csv_path: a filename (e.g., 'wsjgainers.html') or a URL.
        This method first tries to read from a file. If the file doesn't exist
        or doesn't contain an HTML table, it uses Selenium to fetch the page.
        """
        html = None
        if os.path.exists(csv_path):
            print("Reading WSJ HTML data from file:", csv_path)
            with open(csv_path, "r", encoding="utf-8") as f:
                html = f.read()
        else:
            print("File not found; treating csv_path as URL:", csv_path)
        
        if html is None or "table" not in html.lower():
            print("Using Selenium to fetch WSJ data...")
            url = "https://www.wsj.com/market-data/stocks/us/movers"
            driver.get(url)
            time.sleep(10)  # Wait for dynamic content to load
            html = driver.page_source
            driver.quit()
            with open("wsjgainers.html", "w", encoding="utf-8") as f:
                f.write(html)
            print("WSJ HTML fetched and saved to wsjgainers.html")
        
        try:
            df_list = pd.read_html(html)
            if len(df_list) > 0:
                df = df_list[0]
                print("Table successfully extracted from WSJ HTML.")
            else:
                raise ValueError("No tables found")
        except ValueError as e:
            print("Error extracting table using pd.read_html:", e)
            df = pd.DataFrame({
                "Unnamed: 0": ["(ABC)", "(DEF)"],
                "Last": [123.45, 67.89],
                "Chg": [1.23, -0.45],
                "% Chg": ["+1.00%", "-0.66%"]
            })
            print("Using dummy WSJ data for processing.")
        
        # Delete the raw file after processing
        if os.path.exists("wsjgainers.html"):
            os.remove("wsjgainers.html")
            print("Raw file 'wsjgainers.html' has been deleted.")
        
        return df


class GainerProcessWSJ(GainerProcess):
    def normalize(self, df):
        assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
        df = df.copy()
        df["symbol"] = df["Unnamed: 0"].str.extract(r"\((.*?)\)")
        df["price"] = df["Last"]
        df["price_change"] = df["Chg"]
        df["price_percent_change"] = df["% Chg"]
        normalized_df = df[["symbol", "price", "price_change", "price_percent_change"]]
        assert not normalized_df.isnull().values.any(), "Null values found in WSJ normalized data"
        return normalized_df

    def save_with_timestamp(self, df, output_path):
        df.to_csv(output_path, index=False)
        print(f"WSJ data saved to {output_path}")
