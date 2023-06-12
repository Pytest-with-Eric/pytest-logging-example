import logging

# Create a logger object.
logger = logging.getLogger('temp_convertor')

# Set the log level to INFO.
logger.setLevel(logging.INFO)

# Create a console handler.
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

# Create a formatter and add it to the handler.
formatter = logging.Formatter('%(asctime)s - %(name)s%(levelname)s: %(message)s', 
                              datefmt='%m/%d/%Y %I:%M:%S%p')
consoleHandler.setFormatter(formatter)

# Add the handler to the logger.
logger.addHandler(consoleHandler)


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
    print(fahrenheit_to_celsius(90))
    print(celsius_to_fahrenheit(19))