"""
Day 5: Type Hinting & Docstrings - The Contract
Making code readable for humans and safe for machines.
"""

def calculate_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle.
    
    Args:
        length (float): Length of the rectangle in units.
        width (float): Width of the rectangle in units.
    
    Returns:
        float: Area of the rectangle (length * width).
    
    Example:
        >>> calculate_area(5.0, 3.0)
        15.0
    """
    return length * width


def clean_text(raw_text: str) -> str:
    """
    Cleans raw text by removing extra whitespace and converting to lowercase.
    
    Args:
        raw_text (str): The original messy text string.
    
    Returns:
        str: Cleaned text with normalized whitespace and lowercase.
    
    Example:
        >>> clean_text("  Hello World!  ")
        "hello world!"
    """
    return raw_text.strip().lower()


def format_currency(amount: float, currency: str = "USD") -> str:
    """
    Formats a float amount into currency string with 2 decimal places.
    
    Args:
        amount (float): The numeric amount to format.
        currency (str): Currency code (default: "USD").
    
    Returns:
        str: Formatted currency string like "$1,234.56".
    
    Example:
        >>> format_currency(1234.567)
        "$1,234.57"
    """
    formatted_amount = f"{amount:,.2f}"
    return f"{currency}{formatted_amount}"


if __name__ == "__main__":
    # Test all functions
    print("=== Day 5 Type Safety Tests ===")
    
    # Test 1: calculate_area
    area = calculate_area(10.5, 4.2)
    print(f"Area: {area}")  # Expected: 44.1
    
    # Test 2: clean_text
    cleaned = clean_text("  Mixed CASE Text  ")
    print(f"Cleaned: '{cleaned}'")  # Expected: 'mixed case text'
    
    # Test 3: format_currency
    money = format_currency(1234.5678)
    print(f"Money: {money}")  # Expected: "$1,234.57"
    
    print("All tests passed! Type safety implemented.")
