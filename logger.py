import logging

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,     # Set the logging level to DEBUG
    format='%(asctime)s [%(levelname)s]: %(message)s'  # Define log message format
)


def get_logger(name: str):
    return logging.getLogger(name)
