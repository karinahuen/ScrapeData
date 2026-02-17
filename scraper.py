import yfinance as yf
import pandas as pd
from datetime import date

def fetch_exchange_rates():
    print("--------------------------------")
    print("Fetching latest rates...")

    tickers = [
        'GBPUSD=X', 
        'GBPEUR=X', 
        'GBPJPY=X', 
        'GBPAUD=X', 
        'GBPCAD=X', 
        'GBPCHF=X', 
        'GBPCNY=X', 
        'GBPHKD=X' 
    ]

    data = yf.download(tickers, period="1d")

    # Get the latest 'Close' price
    latest = data['Close'].iloc[-1].reset_index()
    latest.columns = ['Ticker', 'Rate']

    def format_name(symbol):
        # Remove the "=X" junk
        clean_symbol = symbol.replace('=X', '') 
        # Insert "/" after the first 3 letters
        return f"{clean_symbol[:3]}/{clean_symbol[3:]}"

    # Apply the formatting to every row
    latest['Currency Pair'] = latest['Ticker'].apply(format_name)
    
    # Add date for reference
    latest['Date'] = date.today()

    filename = "gbp_rates.csv"
    # We save specific columns in a clean order
    clean_data = latest[['Currency Pair', 'Rate', 'Date']]
    clean_data.to_csv(filename, index=False)
    
    print(f"Success! Data saved to {filename}")
    print(clean_data)

if __name__ == "__main__":
    fetch_exchange_rates()