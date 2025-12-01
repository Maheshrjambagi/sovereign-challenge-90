from typing import List


def clean_column_name(raw_name: str) -> str:
    """
    Takes a raw column name (e.g. 'Total Price ') and converts it
    to a clean snake_case name (e.g. 'total_price').
    """
    cleaned = raw_name.strip().lower().replace(" ", "_")
    return cleaned


def clean_price(raw_price: str) -> float:
    """
    Cleans a price string by removing commas and currency symbols,
    then converts it to a float.
    Example: '₹1,234.50' -> 1234.50
    """
    # remove common currency symbols; add more if needed
    for symbol in ["₹", "$", "€"]:
        raw_price = raw_price.replace(symbol, "")

    # remove thousand separators
    raw_price = raw_price.replace(",", "")

    return float(raw_price)


def calculate_total_revenue(prices: List[float], quantities: List[int]) -> float:
    """
    Given parallel lists of prices and quantities, calculates total revenue.
    """
    total = 0.0
    for price, qty in zip(prices, quantities):
        total += price * qty
    return total
