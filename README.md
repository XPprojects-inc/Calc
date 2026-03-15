# Calc — Universal Calculator

A universal calculator written in Python, supporting basic arithmetic and advanced mathematical operations.

## Features

| Operation | Method |
|---|---|
| Addition | `add(a, b)` |
| Subtraction | `subtract(a, b)` |
| Multiplication | `multiply(a, b)` |
| Division | `divide(a, b)` |
| Modulo | `modulo(a, b)` |
| Power | `power(base, exponent)` |
| Square Root | `sqrt(a)` |
| Logarithm | `log(a, base=e)` |
| Sine (degrees) | `sin(angle_degrees)` |
| Cosine (degrees) | `cos(angle_degrees)` |
| Tangent (degrees) | `tan(angle_degrees)` |
| Factorial | `factorial(n)` |
| Absolute Value | `absolute(a)` |

## Usage

### Interactive mode

```bash
python calculator.py
```

### As a library

```python
from calculator import Calculator

calc = Calculator()
print(calc.add(2, 3))        # 5
print(calc.divide(10, 4))    # 2.5
print(calc.sqrt(16))         # 4.0
print(calc.log(100, 10))     # 2.0
print(calc.sin(90))          # 1.0
print(calc.factorial(5))     # 120
```

## Running Tests

```bash
python -m pytest test_calculator.py -v
```
