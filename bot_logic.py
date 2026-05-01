from binance.enums import *
import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        # Binance requires quantity and price to always be in string or proper float format
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
                raise ValueError("Price is required for LIMIT orders!")
            
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
        # This line will show you the exact problem in the terminal
        error_msg = f"API Error: {e}"
        logging.error(error_msg)
        print(error_msg)
        return None