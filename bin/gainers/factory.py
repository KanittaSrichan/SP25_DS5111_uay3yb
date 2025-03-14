# bin/gainers/factory.py

from .yahoo import GainerDownloadYahoo, GainerProcessYahoo
from .wsj import GainerDownloadWSJ, GainerProcessWSJ

class GainerFactory:
    def __init__(self, choice):
        valid_choices = ['yahoo', 'wsj', 'test']
        if choice not in valid_choices:
            raise ValueError(f"Unrecognized gainer type: {choice}")
        self.choice = choice

    def get_downloader(self):
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()
        else:
            raise ValueError("No downloader available for the provided type.")

    def get_processor(self):
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        elif self.choice == 'wsj':
            return GainerProcessWSJ()
        else:
            raise ValueError("No processor available for the provided type.")
