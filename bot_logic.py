from binance.enums import *
import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        # Binance ko quantity aur price hamesha string ya sahi float format mein chahiye
        qty = float(quantity)
        order = None
        
        if order_type.upper() == 'MARKET':
            order = client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type=ORDER_TYPE_MARKET,
                quantity=qty
            )
        elif order_type.upper() == 'LIMIT':
            if not price:
                raise ValueError("LIMIT order ke liye price zaroori hai!")
            
            order = client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=qty,
                price=float(price)
            )
        else:
            raise ValueError(f"Invalid order_type: {order_type}. Use 'MARKET' or 'LIMIT'")
            
        logging.info(f"SUCCESS: {order}")
        return order

    except Exception as e:
        # Ye line tumhe terminal mein exact batayegi ki problem kya hai
        error_msg = f"API Error: {e}"
        logging.error(error_msg)
        print(error_msg)
        return None