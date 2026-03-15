"""Universal Calculator - supports basic and advanced mathematical operations."""

import math


class Calculator:
    """A universal calculator supporting arithmetic, power, root, log, and trig operations."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of a divided by b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def modulo(self, a, b):
        """Return the remainder of a divided by b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot modulo by zero.")
        return a % b

    def power(self, base, exponent):
        """Return base raised to the power of exponent."""
        return base ** exponent

    def sqrt(self, a):
        """Return the square root of a. Raises ValueError if a is negative."""
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)

    def log(self, a, base=math.e):
        """Return the logarithm of a with the given base (default: natural log).
        Raises ValueError if a is not positive."""
        if a <= 0:
            raise ValueError("Logarithm is undefined for non-positive numbers.")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1.")
        return math.log(a, base)

    def sin(self, angle_degrees):
        """Return the sine of an angle given in degrees."""
        return math.sin(math.radians(angle_degrees))

    def cos(self, angle_degrees):
        """Return the cosine of an angle given in degrees."""
        return math.cos(math.radians(angle_degrees))

    def tan(self, angle_degrees):
        """Return the tangent of an angle given in degrees.
        Raises ValueError for angles where tangent is undefined (90 + 180*n degrees)."""
        if (angle_degrees - 90) % 180 == 0:
            raise ValueError("Tangent is undefined at this angle.")
        return math.tan(math.radians(angle_degrees))

    def factorial(self, n):
        """Return the factorial of n. Raises ValueError if n is negative or not an integer."""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        return math.factorial(n)

    def absolute(self, a):
        """Return the absolute value of a."""
        return abs(a)


def main():
    """Run an interactive universal calculator in the terminal."""
    calc = Calculator()
    operations = {
        "1": ("Add", lambda: calc.add(get_number("Enter first number: "), get_number("Enter second number: "))),
        "2": ("Subtract", lambda: calc.subtract(get_number("Enter first number: "), get_number("Enter second number: "))),
        "3": ("Multiply", lambda: calc.multiply(get_number("Enter first number: "), get_number("Enter second number: "))),
        "4": ("Divide", lambda: calc.divide(get_number("Enter first number: "), get_number("Enter second number: "))),
        "5": ("Modulo", lambda: calc.modulo(get_number("Enter first number: "), get_number("Enter second number: "))),
        "6": ("Power", lambda: calc.power(get_number("Enter base: "), get_number("Enter exponent: "))),
        "7": ("Square Root", lambda: calc.sqrt(get_number("Enter number: "))),
        "8": ("Logarithm", lambda: calc.log(
            get_number("Enter number: "),
            get_number("Enter base (press Enter for natural log): ", allow_empty=True) or math.e,
        )),
        "9": ("Sine (degrees)", lambda: calc.sin(get_number("Enter angle in degrees: "))),
        "10": ("Cosine (degrees)", lambda: calc.cos(get_number("Enter angle in degrees: "))),
        "11": ("Tangent (degrees)", lambda: calc.tan(get_number("Enter angle in degrees: "))),
        "12": ("Factorial", lambda: calc.factorial(int(get_number("Enter a non-negative integer: ")))),
        "13": ("Absolute Value", lambda: calc.absolute(get_number("Enter number: "))),
    }

    print("=== Universal Calculator ===")
    while True:
        print("\nOperations:")
        for key, (name, _) in operations.items():
            print(f"  {key:>2}. {name}")
        print("   0. Quit")

        choice = input("\nSelect operation: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue

        name, operation = operations[choice]
        try:
            result = operation()
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


def get_number(prompt, allow_empty=False):
    """Prompt the user for a numeric value."""
    while True:
        raw = input(prompt).strip()
        if allow_empty and raw == "":
            return None
        try:
            return float(raw)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
