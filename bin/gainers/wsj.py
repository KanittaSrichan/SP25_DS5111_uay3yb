from .base import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
    def __init__(self, url):
        super().__init__(url)

    def download(self):
        print("Downloading WSJ gainers")

class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        pass

    def normalize(self):
        print("Normalizing WSJ gainers")

    def save_with_timestamp(self):
        print("Saving WSJ gainers")
