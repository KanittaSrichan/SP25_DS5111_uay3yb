# bin/gainers/wsj.py
from .base import GainerDownload, GainerProcess
import requests

class GainerDownloadWSJ(GainerDownload):
    def __init__(self, url="https://www.wsj.com/market-data/stocks/us/movers"):
        super().__init__(url)

    def download(self):
        print(f"Downloading WSJ gainers from {self.url}")
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Ensures we notice bad responses
            return response.text  # For actual processing, you might return or save this data
        except requests.RequestException as e:
            print(f"Failed to download WSJ data: {e}")


class GainerProcessWSJ(GainerProcess):
    def normalize(self):
        print("Normalizing WSJ gainers")

    def save_with_timestamp(self):
        print("Saving WSJ gainers")
