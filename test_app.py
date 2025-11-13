"""
test_app.py
Unit tests for the math functions in app.py.
"""

import pytest
from app import add, multiply

def test_addition_positive_numbers():
    assert add(10, 5) == 15

def test_addition_negative_numbers():
    assert add(-2, -3) == -5

def test_multiplication_positive_numbers():
    assert multiply(4, 5) == 20

def test_multiplication_with_zero():
    assert multiply(10, 0) == 0

def test_add_and_multiply_combined():
    result = multiply(add(2, 3), 4)   # (2+3)*4 = 20
    assert result == 20
