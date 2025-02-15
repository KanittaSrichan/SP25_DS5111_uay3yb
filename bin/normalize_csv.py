import pandas as pd
import sys

def normalize_csv(input_file):
    try:
        df = pd.read_csv(input_file)

        # Normalize column names to lowercase
        df.columns = [col.strip().lower() for col in df.columns]

        # Check for necessary columns and adjust if necessary
        expected_columns = ['symbol', 'price', 'change', 'change %']
        missing_columns = set(expected_columns) - set(df.columns)
        if missing_columns:
            raise ValueError(f"Missing columns: {missing_columns}")

        # Select and rename only the necessary columns
        df = df[['symbol', 'price', 'change', 'change %']]
        df.rename(columns={'change': 'price_change', 'change %': 'price_percent_change'}, inplace=True)

        # Save the normalized file
        output_file = input_file.replace('.csv', '_norm.csv')
        df.to_csv(output_file, index=False)
        print(f"Normalized file saved as: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python normalize_csv.py <path to CSV file>")
        sys.exit(1)
    normalize_csv(sys.argv[1])
