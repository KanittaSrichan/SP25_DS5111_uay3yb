from .base import GainerDownload, GainerProcess

class GainerDownloadYahoo(GainerDownload):
    def __init__(self, url):
        super().__init__(url)

    def download(self):
        print("Downloading Yahoo gainers")

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        pass

    def normalize(self):
        print("Normalizing Yahoo gainers")

    def save_with_timestamp(self):
        print("Saving Yahoo gainers")
