import logging

logging.basicConfig(level=logging.ERROR,  # Set global logging level
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
                    datefmt='%Y-%m-%d %H:%M:%S')  # Timestamp format

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
logging.getLogger().addHandler(console_handler)

logging.info('Hello')
logging.exception("Big Bad Exception")