import argparse
from bin.gainers.factory import GainerFactory

def main(source):
    # Create the factory based on the source provided
    factory = GainerFactory(source)
    
    # Retrieve the appropriate downloader and processor from the factory
    downloader = factory.get_downloader()
    processor = factory.get_processor()

    # Execute the download, normalization, and saving processes
    data = downloader.download()
    normalized_data = processor.normalize(data)
    processor.save_with_timestamp(normalized_data)

if __name__ == "__main__":
    # Setup the argument parser
    parser = argparse.ArgumentParser(description="Process financial gainer data from a specified source.")
    
    # Add a positional argument for the source, with specified options
    parser.add_argument("source", choices=['yahoo', 'wsj'], help="Specify the data source (yahoo or wsj).")
    
    # Parse the command line arguments
    args = parser.parse_args()

    # Run the main function with the chosen source
    main(args.source)
