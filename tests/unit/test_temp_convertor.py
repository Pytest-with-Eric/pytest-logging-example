import logging
import pytest
from temp_convertor.core import fahrenheit_to_celsius, celsius_to_fahrenheit

# Get logger
logger = logging.getLogger('__temp_convertor__')
logger.setLevel(logging.DEBUG)


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(90) == 32.22


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(19) == 66.2

def test_celecius_to_fahrenheit_caplog_ex(caplog):
    caplog.set_level(logging.DEBUG, logger='__temp_convertor__') # Overwrite the default log level using caplog fixture
    assert celsius_to_fahrenheit(300) == 572.0
    for record in caplog.records:  # Print Caplog records
        print(record.levelname, record.message)


