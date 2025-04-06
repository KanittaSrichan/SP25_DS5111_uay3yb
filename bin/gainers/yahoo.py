import subprocess
import pandas as pd
from .base import GainerDownload, GainerProcess

class GainerDownloadYahoo(GainerDownload):
    def download(self, csv_path):
        # Use the command from the Makefile to fetch Yahoo HTML data.
        base_cmd = (
            "google-chrome-stable --headless --disable-gpu --dump-dom "
            "--no-sandbox --timeout=5000 "
        )
        url = "'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200'"
        cmd = base_cmd + url
        print("Running command:", cmd)
        try:
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, check=True
            )
        except subprocess.CalledProcessError as e:
            raise ValueError("Error running chrome command: " + str(e)) from e

        html = result.stdout
        # Save the fetched HTML to a file for debugging purposes.
        with open("ygainers.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Yahoo HTML saved to ygainers.html")

        # Extract the table using pandas.
        try:
            df_list = pd.read_html(html)
            if len(df_list) > 0:
                df = df_list[0]
                print("Table successfully extracted from Yahoo HTML.")
            else:
                raise ValueError("No tables found in Yahoo HTML.")
        except Exception as e:
            raise ValueError("Error extracting table using pd.read_html: " + str(e)) from e

        return df

class GainerProcessYahoo(GainerProcess):
    def normalize(self, df):
        # Ensure the input is a DataFrame and drop rows missing critical columns.
        assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
        df = df.copy()
        df = df.dropna(subset=["Symbol", "Price", "Change", "Change %"])
        df["symbol"] = df["Symbol"]
        # Extract the numeric price: take the first token from the Price string and remove commas.
        df["price"] = (
            df["Price"].str.strip()
              .str.split()
              .str[0]
              .str.replace(",", "", regex=False)
        )
        try:
            df["price"] = df["price"].astype(float)
        except Exception as e:
            raise ValueError(f"Error converting price to float: {e}") from e
        df["price_change"] = df["Change"]
        df["price_percent_change"] = df["Change %"].str.strip("+%")
        normalized_df = df[["symbol", "price", "price_change", "price_percent_change"]]
        assert not normalized_df.isnull().values.any(), "Null values found in Yahoo normalized data"
        return normalized_df

    def save_with_timestamp(self, df, output_path):
        df.to_csv(output_path, index=False)
        print(f"Yahoo data saved to {output_path}")
