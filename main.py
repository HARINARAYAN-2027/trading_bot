import argparse
from logger_config import setup_logging
from client_wrapper import get_client
from bot_logic import place_order

def main():
    # Initialize logging and client
    setup_logging()
    
    try:
        client = get_client()
    except Exception as e:
        print(f"Initialization Error: {e}")
        return

    # CLI Argument Parsing
    parser = argparse.ArgumentParser(description='Binance Futures Trading Bot CLI')
    parser.add_argument('--symbol', type=str, required=True, help='Trading symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', type=str, required=True, choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('--type', type=str, required=True, choices=['MARKET', 'LIMIT'], help='Order type')
    parser.add_argument('--qty', type=float, required=True, help='Order quantity')
    parser.add_argument('--price', type=float, help='Target price (Required for LIMIT orders)')

    args = parser.parse_args()

    print(f"\n🚀 Executing {args.type} {args.side} order for {args.symbol}...")
    
    # Place the order
    response = place_order(
        client, 
        args.symbol, 
        args.side, 
        args.type, 
        args.qty, 
        args.price
    )

    if response:
        print(f"✅ Order Placed Successfully!")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Execution Status: {response.get('status')}")
    else:
        print("❌ Order Execution Failed. See 'trading_bot.log' for details.")

if __name__ == "__main__":
    main()