import pandas as pd
import pytest

from bin.gainers.yahoo import GainerProcessYahoo, GainerDownloadYahoo
from bin.gainers.wsj import GainerProcessWSJ, GainerDownloadWSJ
from bin.gainers.factory import GainerFactory

def test_yahoo_normalize():
    # Create a dummy DataFrame similar to expected Yahoo CSV structure
    # nice, some test data that is constant is a good thing
    data = {
        "Symbol": ["QBTS", "RGTI"],
        "Price": ["10.15 +3.24 (+46.89%)", "11.22 +2.47 (+28.23%)"],
        "Change": ["3.24", "2.47"],
        "Change %": ["+46.89%", "+28.23%"]
    }
    df = pd.DataFrame(data)
    processor = GainerProcessYahoo()
    normalized = processor.normalize(df)
    expected_columns = ['symbol', 'price', 'price_change', 'price_percent_change']
    assert list(normalized.columns) == expected_columns
    # Check that the price column was converted to float
    assert all(normalized['price'].apply(lambda x: isinstance(x, float)))
    # Verify symbol and percent change extraction
    assert normalized['symbol'].iloc[0] == "QBTS"
    assert normalized['price_percent_change'].iloc[0] == "46.89"

def test_wsj_normalize():
    # Create a dummy DataFrame similar to expected WSJ HTML table
    data = {
        "Unnamed: 0": ["(ABC)", "(DEF)"],
        "Last": [100.50, 200.75],
        "Chg": [1.5, -2.0],
        "% Chg": ["+1.50%", "-1.00%"]
    }
    df = pd.DataFrame(data)
    processor = GainerProcessWSJ()
    normalized = processor.normalize(df)
    expected_columns = ['symbol', 'price', 'price_change', 'price_percent_change']
    assert list(normalized.columns) == expected_columns
    # Check that the symbol is extracted correctly (removing parentheses)
    assert normalized['symbol'].iloc[0] == "ABC"
    # Check that price equals the 'Last' column value
    assert normalized['price'].iloc[0] == 100.50

def test_factory_yahoo():
    factory = GainerFactory("yahoo")
    downloader = factory.get_downloader()
    processor = factory.get_processor()
    assert isinstance(downloader, GainerDownloadYahoo)
    assert isinstance(processor, GainerProcessYahoo)

def test_factory_wsj():
    factory = GainerFactory("wsj")
    downloader = factory.get_downloader()
    processor = factory.get_processor()
    from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ
    assert isinstance(downloader, GainerDownloadWSJ)
    assert isinstance(processor, GainerProcessWSJ)
