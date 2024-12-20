import logging
import os
from logging.handlers import RotatingFileHandler

# 1. Basic logging configuration
logging.basicConfig(level=logging.DEBUG,  # Set global logging level
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
                    datefmt='%Y-%m-%d %H:%M:%S')  # Timestamp format

# 2. Different log levels demonstration
logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING message")
logging.error("This is an ERROR message")
logging.critical("This is a CRITICAL message")

# 3. Logging to both file and console
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("example.log")

# Add handlers to the root logger
logging.getLogger().addHandler(console_handler)
logging.getLogger().addHandler(file_handler)

# Log messages to both console and file
logging.info("This is an INFO message logged to both console and file.")

# 4. Custom log format for different handlers
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# 5. Custom logger names
logger = logging.getLogger('custom_logger')
logger.setLevel(logging.DEBUG)
logger.debug("This is a DEBUG message from the custom logger")

# 6. Logging in different modules (simulating with functions)
def simulate_logging_in_function():
    logger.debug("This message is from within a function.")

simulate_logging_in_function()

# 7. Using a logging handler (FileHandler and StreamHandler)
# FileHandler example
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.info("Info logged in the 'app.log' file.")

# 8. Log rotation (using RotatingFileHandler)
log_rotation_handler = RotatingFileHandler("rotating.log", maxBytes=2000, backupCount=3)
log_rotation_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(log_rotation_handler)

# Simulating log rotation by logging multiple messages
for i in range(50):
    logger.info(f"Log rotation message number {i}")

# 9. Logging exceptions and tracebacks
try:
    1 / 0  # Division by zero will raise an exception
except ZeroDivisionError as e:
    logger.exception("An exception occurred!")

# Demonstrating logging an exception (logging traceback)
try:
    open("non_existent_file.txt", "r")  # File not found
except FileNotFoundError as e:
    logger.error("An error occurred", exc_info=True)

# Clean up by removing handlers
logging.getLogger().removeHandler(console_handler)
logging.getLogger().removeHandler(file_handler)
