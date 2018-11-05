from currency import convert
import pytest

def test_same_conversion():
    assert convert(
        rate = [], value = 1, current = "USD", to = "USD") == 1
    assert convert(
        rate = [], value = 99, current = "USD", to = "USD") == 99

def test_currency_convert_mulitples():
    assert convert(
        rate = [("USD", "EUR", 0.74)], value = 1, current = "USD", to = "EUR") == 0.74
    assert convert(
        rate = [("USD", "EUR", 0.74)], value = 99, current = "USD", to = "EUR") == 73.26

def test_currency_convert_backwards():
    assert round(convert(
        rate = [("USD", "EUR", 0.74)], value = 1, current = "EUR", to = "USD"), 2) == 1.35
    assert round(convert(
        rate = [("USD", "EUR", 0.74)], value = 99, current = "EUR", to = "USD"), 2) == 133.78

def test_many_rates():
    assert convert(
        rate = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)], value = 1, current = "USD", to = "EUR") == 0.74
    assert convert(
        rate = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)], value = 1, current = "EUR", to = "JPY") == 145.949

# def test_the_back_and_forth():