import logging

# Set up Logging
# Create a named logger
logger = logging.getLogger('__temp_convertor__')
logger.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Set the formatter for the console handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                              datefmt='%m/%d/%Y %I:%M:%S%p')
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)

# Create a file handler
file_handler = logging.FileHandler('./logs/temp_convertor_src_run.log')
file_handler.setLevel(logging.INFO)

# Set the formatter for the file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S%p')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


############################ Source code ############################ 
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert the specified Fahrenheit temperature to Celsius and return it.
    Input: fahrenheit: float
    Output: celsius: float
    """
    logger.debug(f"Converting {fahrenheit}°F to Celsius.")
    celsius = round((fahrenheit - 32) * 5 / 9, 2)
    logger.info(f"Result: {celsius}°C")
    return celsius

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert the specified Celsius temperature to Fahrenheit and return it.
        Input: celsius: float
        Output: fahrenheit: float
    """
    logger.debug(f"Converting {celsius}°C to Fahrenheit.")
    fahrenheit = round((celsius * 9 / 5) + 32, 2)
    logger.info(f"Result: {fahrenheit}°F")
    return fahrenheit

if __name__ == "__main__":
    fahrenheit_to_celsius(90)
    celsius_to_fahrenheit(19)