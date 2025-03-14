import sys
import pandas as pd

def normalize_wsj_data(df):
    assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
    df['symbol'] = df['Unnamed: 0'].str.extract(r'\((.*?)\)')
    df['price'] = df['Last']
    df['price_change'] = df['Chg']
    df['price_percent_change'] = df['% Chg']
    normalized_df = df[['symbol', 'price', 'price_change', 'price_percent_change']]
    assert not normalized_df.isnull().values.any(), "Null values found in WSJ normalized data"
    return normalized_df

def normalize_yahoo_data(df):
    assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
    
    # Rename columns if necessary to match expected names
    if 'Price (Intraday)' in df.columns:
        df = df.rename(columns={'Price (Intraday)': 'Price'})
    if '% Change' in df.columns:
        df = df.rename(columns={'% Change': 'Change %'})
    
    # Check that required columns exist now
    required_columns = ['Symbol', 'Price', 'Change', 'Change %']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Expected column '{col}' not found in the data")
    
    df['symbol'] = df['Symbol']
    # Extract a numeric price from the Price column; adjust regex if needed
    df['price'] = df['Price'].str.extract(r'^(\d+\.\d+)')[0].astype(float)
    df['price_change'] = df['Change']
    # Remove any extra characters from the percentage change
    df['price_percent_change'] = df['Change %'].str.strip('+%')
    
    normalized_df = df[['symbol', 'price', 'price_change', 'price_percent_change']]
    assert not normalized_df.isnull().values.any(), "Null values found in Yahoo normalized data"
    return normalized_df



def determine_source(filename):
    # This can be adjusted based on file naming conventions or file content
    if 'wsj' in filename.lower():
        return 'wsj'
    elif 'ygainers' in filename.lower():
        return 'yahoo'
    else:
        raise ValueError("Unknown file source, please check the filename")

def main():
    if len(sys.argv) < 2:
        print("Usage: python bin/normalize_csv.py <path to raw csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    try:
        source = determine_source(csv_path)
        data = pd.read_csv(csv_path)
        if source == 'wsj':
            normalized_data = normalize_wsj_data(data)
        elif source == 'yahoo':
            normalized_data = normalize_yahoo_data(data)
        else:
            raise ValueError("Source determination failed")

        output_path = csv_path.replace('.csv', '_norm.csv')
        normalized_data.to_csv(output_path, index=False)
        print(f"File saved: {output_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

