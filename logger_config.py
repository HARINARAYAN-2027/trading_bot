import logging

def setup_logging():
    """
    Configures the logging system to save API requests and responses to a file.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("trading_bot.log"), # Log file for submission
            logging.StreamHandler() # Output to terminal
        ]
    )