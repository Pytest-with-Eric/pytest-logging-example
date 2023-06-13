import logging
from temp_convertor.core import fahrenheit_to_celsius, celsius_to_fahrenheit

# Create a named logger
logger = logging.getLogger('__temp_convertor__')
logger.setLevel(logging.DEBUG)


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(90) == 32.22


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(19) == 66.2


