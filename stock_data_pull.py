import requests
import pandas as pd
from datetime import datetime

# Configuration
API_KEY = "fvWNKeW1OjDQvLOzza0cGabR0_RvGtQ8"
BASE_URL = "https://api.massive-data.io/v1/stocks/batch" # Assumed endpoint for batch pulls
SYMBOLS = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META"] # Default symbols, can be modified

def pull_stock_data():
    """
    Pulls the most recent stock data for a batch of symbols using the Massive API.
    Uses a batch request to minimize API calls for the free tier.
    """
    print(f"Fetching most recent stock data as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
    
    params = {
        "symbols": ",".join(SYMBOLS),
        "apikey": API_KEY
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Processing based on typical API response structures
        # If the API returns a list of stocks a flat list or a dictionary mapped by symbol
        df = pd.DataFrame(data)
        
        # Save to CSV
        filename = f"stock_data_{datetime.now().strftime('%Y%m%d')}.csv"
        df.to_csv(filename, index=False)
        print(f"Successfully pulled data for {len(SYMBOLS)} symbols. Saved to {filename}")
        return df
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    pull_stock_data()
