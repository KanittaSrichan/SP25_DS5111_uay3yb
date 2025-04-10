# bin/gainers/base.py

from abc import ABC, abstractmethod
# are these files getting put through pylint?  That would have asked for comments on the class etc... let me know if it is and I'm misremembering
# Abstract class for downloading raw data
class GainerDownload(ABC):
    def __init__(self):
        self.url = None

    @abstractmethod
    def download(self, csv_path):
        """
        Reads the raw CSV file and returns a pandas DataFrame.
        """
        raise NotImplementedError

# Abstract class for processing (normalizing & saving) the data
class GainerProcess(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def normalize(self, df):
        """
        Normalizes the input DataFrame and returns a new DataFrame.
        """
        raise NotImplementedError

    @abstractmethod
    def save_with_timestamp(self, df, output_path):
        """
        Saves the normalized DataFrame to the given output path.
        """
        raise NotImplementedError
