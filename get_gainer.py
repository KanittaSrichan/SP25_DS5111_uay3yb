import sys
from bin.gainers.factory import GainerFactory

def main():
    # Make our selection, 'one' choice and a URL for the downloader
    choice = sys.argv[1]
    url = sys.argv[2]  # URL to be passed as the second argument

    # Create the factory instance with the choice and URL
    factory = GainerFactory(choice, url)
    downloader = factory.get_downloader()
    processor = factory.get_processor()

    # Process the gainer
    downloader.download()
    processor.normalize()
    processor.save_with_timestamp()

if __name__ == "__main__":
    main()
