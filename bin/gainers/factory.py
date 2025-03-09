from bin.gainers.base import GainerDownloadYahoo, GainerDownloadWSJ, GainerProcessYahoo, GainerProcessWSJ

class GainerFactory:
    def __init__(self, choice, url):
        """
        Initialize the factory with a gainer choice ('yahoo' or 'wsj') and a URL.
        The URL is used by the downloader for data retrieval.
        """
        assert choice in ['yahoo', 'wsj'], f"Unrecognized gainer type {choice}"
        self.choice = choice
        self.url = url  # Accept the URL as part of the initialization

    def get_downloader(self):
        """
        Returns the appropriate downloader based on the chosen source.
        """
        if self.choice == 'yahoo':
            return GainerDownloadYahoo(self.url)  # Pass URL to the Yahoo downloader
        elif self.choice == 'wsj':
            return GainerDownloadWSJ(self.url)  # Pass URL to the WSJ downloader

    def get_processor(self):
        """
        Returns the appropriate processor based on the chosen source.
        """
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        elif self.choice == 'wsj':
            return GainerProcessWSJ()
