# get_gainer.py

import sys
import datetime
import os
from bin.gainers.factory import GainerFactory

class ProcessGainer:
    def __init__(self, source, gainer_downloader, gainer_processor):
        self.source = source
        self.downloader = gainer_downloader
        self.processor = gainer_processor

    def process(self):
        # Generate a timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

        # Define the folder path for this source
        folder_path = os.path.join("raw_data", self.source)  # raw_data/yahoo or raw_data/wsj
        os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists

        # Filenames without redundant "yahoo_" or "wsj_" prefixes
        raw_csv_filename = os.path.join(folder_path, f"gainers_raw_{timestamp}.csv")
        normalized_csv_filename = os.path.join(folder_path, f"gainers_normalized_{timestamp}.csv")

        print(f" Downloading {self.source} data...")

        # Download (read) raw data
        df = self.downloader.download(raw_csv_filename)

        print(f" Normalizing {self.source} data...")

        # Normalize the data
        normalized_df = self.processor.normalize(df)

        print(f" Saving raw data to {raw_csv_filename}")
        self.processor.save_with_timestamp(df, raw_csv_filename)
        print(f" Saved raw data: {raw_csv_filename}")

        print(f" Saving normalized data to {normalized_csv_filename}")
        self.processor.save_with_timestamp(normalized_df, normalized_csv_filename)
        print(f" Saved normalized data: {normalized_csv_filename}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python get_gainer.py <source: yahoo/wsj>")
        sys.exit(1)

    source = sys.argv[1].lower()

    if source not in ["yahoo", "wsj"]:
        print(" Source must be either 'yahoo' or 'wsj'")
        sys.exit(1)

    try:
        # Initialize Factory for source
        factory = GainerFactory(source)
        downloader = factory.get_downloader()
        processor = factory.get_processor()

        # Process data collection
        runner = ProcessGainer(source, downloader, processor)
        runner.process()

    except Exception as e:
        error_message = f"An error occurred with {source}: {e}"
        print(error_message)

        # Log error to a file for debugging
        with open("error_log.txt", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - {error_message}\n")

        sys.exit(1)

if __name__ == "__main__":
    main()
