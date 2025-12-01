from src.tools import clean_column_name, clean_price, calculate_total_revenue


def demo_cleaning() -> None:
    """
    Demo function to show that imports from src.tools work correctly.
    """
    raw_col = "Total Price "
    cleaned_col = clean_column_name(raw_col)

    raw_prices = ["₹1,000.50", "2,500", "3,000.75"]
    quantities = [1, 2, 1]

    cleaned_prices = [clean_price(p) for p in raw_prices]
    total_revenue = calculate_total_revenue(cleaned_prices, quantities)

    print(f"Original column name: {raw_col!r}")
    print(f"Cleaned column name: {cleaned_col!r}")
    print(f"Cleaned prices: {cleaned_prices}")
    print(f"Total revenue: {total_revenue}")
    

if __name__ == "__main__":
    demo_cleaning()
