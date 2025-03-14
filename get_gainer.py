# get_gainer.py

import sys
from bin.gainers.factory import GainerFactory

class ProcessGainer:
    def __init__(self, gainer_downloader, gainer_processor):
        self.downloader = gainer_downloader
        self.processor = gainer_processor

    def process(self, input_csv):
        # Download (read) raw data from CSV file
        df = self.downloader.download(input_csv)
        # Normalize the data
        normalized_df = self.processor.normalize(df)
        # Generate an output filename (e.g., appending _norm to the original filename)
        output_csv = input_csv.replace('.csv', '_norm.csv')
        # Save the normalized data
        self.processor.save_with_timestamp(normalized_df, output_csv)

def main():
    if len(sys.argv) < 2:
        print("Usage: python get_gainer.py <source: yahoo/wsj>")
        sys.exit(1)

    source = sys.argv[1].lower()

    # Determine the default CSV filename based on the source
    if source == "yahoo":
        csv_path = "ygainers.csv"
    elif source == "wsj":
        csv_path = "wsjgainers.csv"
    else:
        print("Source must be either 'yahoo' or 'wsj'")
        sys.exit(1)

    try:
        factory = GainerFactory(source)
        downloader = factory.get_downloader()
        processor = factory.get_processor()

        runner = ProcessGainer(downloader, processor)
        runner.process(csv_path)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
