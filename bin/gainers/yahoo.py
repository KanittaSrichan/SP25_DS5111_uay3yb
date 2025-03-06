# bin/gainers/yahoo.py
from .base import GainerDownload, GainerProcess
import requests

class GainerDownloadYahoo(GainerDownload):
    def __init__(self, url="https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200"):
        super().__init__(url)

    def download(self):
        print(f"Downloading Yahoo gainers from {self.url}")
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Failed to download Yahoo data: {e}")


class GainerProcessYahoo(GainerProcess):
    def normalize(self):
        print("Normalizing Yahoo gainers")

    def save_with_timestamp(self):
        print("Saving Yahoo gainers")
