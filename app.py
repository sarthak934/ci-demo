"""
app.py
A simple utility module containing basic math operations.
"""

def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


def multiply(a: int, b: int) -> int:
    """Return the product of two numbers."""
    return a * b


if __name__ == "__main__":
    # Sample output for demonstration
    print("Addition (10 + 5):", add(10, 5))
    print("Multiplication (10 * 5):", multiply(10, 5))
