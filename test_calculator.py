"""Unit tests for the universal calculator."""

import math
import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# --- Basic arithmetic ---

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
    assert calc.add(1.5, 2.5) == pytest.approx(4.0)


def test_subtract(calc):
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-3, -3) == 0


def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 5) == -10
    assert calc.multiply(0, 100) == 0
    assert calc.multiply(1.5, 2) == pytest.approx(3.0)


def test_divide(calc):
    assert calc.divide(10, 2) == pytest.approx(5.0)
    assert calc.divide(7, 2) == pytest.approx(3.5)
    assert calc.divide(-9, 3) == pytest.approx(-3.0)


def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)


def test_modulo(calc):
    assert calc.modulo(10, 3) == 1
    assert calc.modulo(9, 3) == 0


def test_modulo_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot modulo by zero"):
        calc.modulo(5, 0)


# --- Power & roots ---

def test_power(calc):
    assert calc.power(2, 10) == 1024
    assert calc.power(5, 0) == 1
    assert calc.power(2, -1) == pytest.approx(0.5)


def test_sqrt(calc):
    assert calc.sqrt(9) == pytest.approx(3.0)
    assert calc.sqrt(0) == pytest.approx(0.0)
    assert calc.sqrt(2) == pytest.approx(math.sqrt(2))


def test_sqrt_negative(calc):
    with pytest.raises(ValueError, match="negative"):
        calc.sqrt(-1)


# --- Logarithm ---

def test_log_natural(calc):
    assert calc.log(math.e) == pytest.approx(1.0)
    assert calc.log(1) == pytest.approx(0.0)


def test_log_base10(calc):
    assert calc.log(100, 10) == pytest.approx(2.0)
    assert calc.log(1000, 10) == pytest.approx(3.0)


def test_log_invalid(calc):
    with pytest.raises(ValueError):
        calc.log(0)
    with pytest.raises(ValueError):
        calc.log(-5)
    with pytest.raises(ValueError):
        calc.log(10, 1)
    with pytest.raises(ValueError):
        calc.log(10, -2)


# --- Trigonometry ---

def test_sin(calc):
    assert calc.sin(0) == pytest.approx(0.0)
    assert calc.sin(90) == pytest.approx(1.0)
    assert calc.sin(180) == pytest.approx(0.0, abs=1e-10)


def test_cos(calc):
    assert calc.cos(0) == pytest.approx(1.0)
    assert calc.cos(90) == pytest.approx(0.0, abs=1e-10)
    assert calc.cos(180) == pytest.approx(-1.0)


def test_tan(calc):
    assert calc.tan(0) == pytest.approx(0.0)
    assert calc.tan(45) == pytest.approx(1.0)


def test_tan_undefined(calc):
    with pytest.raises(ValueError, match="undefined"):
        calc.tan(90)
    with pytest.raises(ValueError, match="undefined"):
        calc.tan(270)


# --- Factorial ---

def test_factorial(calc):
    assert calc.factorial(0) == 1
    assert calc.factorial(1) == 1
    assert calc.factorial(5) == 120
    assert calc.factorial(10) == 3628800


def test_factorial_invalid(calc):
    with pytest.raises(ValueError):
        calc.factorial(-1)
    with pytest.raises(ValueError):
        calc.factorial(3.5)


# --- Absolute value ---

def test_absolute(calc):
    assert calc.absolute(-7) == 7
    assert calc.absolute(7) == 7
    assert calc.absolute(0) == 0
    assert calc.absolute(-3.14) == pytest.approx(3.14)
