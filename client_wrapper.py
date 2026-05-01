import os
import time
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_client():
    """
    Initializes the Binance client with stability settings 
    to prevent Connection Reset errors.
    """
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    
    if not api_key or not api_secret:
        raise ValueError("Error: BINANCE_API_KEY or BINANCE_API_SECRET not found in .env file!")

    # Added requests_params to handle connection stability
    client = Client(
        api_key, 
        api_secret, 
        testnet=True,
        requests_params={'timeout': 20} # Increased timeout to 20 seconds
    )

    # Sync local time with Binance server time
    try:
        server_time = client.get_server_time()
        server_time_ms = server_time['serverTime']
        local_time_ms = int(time.time() * 1000)
        client.timestamp_offset = server_time_ms - local_time_ms
    except Exception as e:
        print(f"Warning: Failed to sync server time: {e}")

    return client

def check_connection():
    """
    Verifies the API connection by fetching the account balance.
    """
    print("Connecting to Binance Futures Testnet...")
    try:
        client = get_client()
        # Fetching balance to verify credentials and connection
        balance = client.futures_account_balance()
        print("✅ Connection Successful! Account verified.")
        
        if balance:
            for item in balance:
                if float(item['balance']) > 0:
                    print(f"💰 Asset: {item['asset']} | Balance: {item['balance']}")
        return True
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return False

if __name__ == "__main__":
    check_connection()