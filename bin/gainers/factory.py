# bin/gainers/factory.py
from .wsj import GainerDownloadWSJ, GainerProcessWSJ
from .yahoo import GainerDownloadYahoo, GainerProcessYahoo

class GainerFactory:
    def __init__(self, choice):
        self.choice = choice 

    def get_downloader(self):
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()

    def get_processor(self):
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        elif self.choice == 'wsj':
            return GainerProcessWSJ()
