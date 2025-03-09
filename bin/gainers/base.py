from abc import ABC, abstractmethod
import requests
import pandas as pd
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Base Downloader Class
class GainerDownload(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def download(self):
        pass


# Yahoo Downloader Class
class GainerDownloadYahoo(GainerDownload):
    def __init__(self, url):
        super().__init__(url)

    def download(self):
        print(f"Downloading Yahoo gainers from {self.url}")
        response = requests.get(self.url)
        if response.status_code == 200:
            print("Successfully downloaded Yahoo gainers data")
            tables = pd.read_html(response.text)
            if tables:
                self.data = tables[0]  # Assume the first table is the one we need
                print("Successfully parsed Yahoo gainers data")
        else:
            print(f"Failed to download data. HTTP status code: {response.status_code}")


# WSJ Downloader Class (Using Selenium for Dynamic Content)
class GainerDownloadWSJ(GainerDownload):
    def __init__(self, url):
        super().__init__(url)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def download(self):
        print(f"Downloading WSJ gainers from {self.url}")
        self.driver.get(self.url)
        time.sleep(5)  # Wait for JS to load content
        page_source = self.driver.page_source
        tables = pd.read_html(page_source)
        if tables:
            self.data = tables[0]  # Assume the first table is the one we need
            print("Successfully parsed WSJ gainers data")
        else:
            print("No tables found in the HTML")
        self.driver.quit()


# Base Processor Class
class GainerProcess(ABC):
    def __init__(self):
        self.normalized_data = None

    @abstractmethod
    def normalize(self):
        pass

    @abstractmethod
    def save_with_timestamp(self):
        pass


# Yahoo Processor Class
class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        super().__init__()

    def normalize(self):
        print("Normalizing Yahoo gainers")
        self.normalized_data = {"symbol": "AAPL", "price": 150}  # Example data
        print("Yahoo gainers normalized")

    def save_with_timestamp(self):
        print("Saving Yahoo gainers")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ygainers_{timestamp}.csv"
        pd.DataFrame([self.normalized_data]).to_csv(filename, index=False)
        print(f"Data saved to {filename}")


# WSJ Processor Class
class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        super().__init__()

    def normalize(self):
        print("Normalizing WSJ gainers")
        self.normalized_data = {"symbol": "GOOG", "price": 2800}  # Example data
        print("WSJ gainers normalized")

    def save_with_timestamp(self):
        print("Saving WSJ gainers")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"wsjgainers_{timestamp}.csv"
        pd.DataFrame([self.normalized_data]).to_csv(filename, index=False)
        print(f"Data saved to {filename}")
