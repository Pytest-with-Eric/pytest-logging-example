from custom_logger import console_logger, LogLevel

c_logger = console_logger(name="temp_convertor", level=LogLevel.DEBUG)


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert the specified Fahrenheit temperature to Celsius and return it.
    Input: fahrenheit: float
    Output: celsius: float
    """
    c_logger.debug(f"Converting {fahrenheit}°F to Celsius.")
    celsius = round((fahrenheit - 32) * 5 / 9, 2)
    c_logger.info(f"Result: {celsius}°C")
    return celsius


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert the specified Celsius temperature to Fahrenheit and return it.
    Input: celsius: float
    Output: fahrenheit: float
    """
    c_logger.debug(f"Converting {celsius}°C to Fahrenheit.")
    fahrenheit = round((celsius * 9 / 5) + 32, 2)
    c_logger.info(f"Result: {fahrenheit}°F")
    return fahrenheit


if __name__ == "__main__":
    fahrenheit_to_celsius(90)
    celsius_to_fahrenheit(19)
