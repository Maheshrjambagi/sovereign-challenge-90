from typing import List, Dict, Any
from src.tools import clean_price, calculate_total_revenue


def process_data(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Processes a list of raw transaction dictionaries and returns a summary.

    Each transaction dictionary is expected to have:
      - "price": string representing price (may contain commas/currency symbols)
      - "qty": integer quantity

    This function:
      - cleans the price string and converts it to float
      - calculates total revenue across all transactions
      - returns a summary dictionary with:
          - total_transactions
          - total_revenue
          - average_price
    """
    cleaned_prices: List[float] = []
    quantities: List[int] = []

    for tx in data:
        raw_price = str(tx.get("price", "0"))
        qty = int(tx.get("qty", 0))

        price_value = clean_price(raw_price)
        cleaned_prices.append(price_value)
        quantities.append(qty)

    total_revenue = calculate_total_revenue(cleaned_prices, quantities)

    total_transactions = len(data)
    avg_price = sum(cleaned_prices) / len(cleaned_prices) if cleaned_prices else 0.0

    summary: Dict[str, Any] = {
        "total_transactions": total_transactions,
        "total_revenue": total_revenue,
        "average_price": avg_price,
    }
    return summary


if __name__ == "__main__":
    # Example raw data you can adjust
    raw_transactions = [
        {"price": "₹1,000.50", "qty": 2},
        {"price": "2,500", "qty": 1},
        {"price": "$3,000.75", "qty": 3},
    ]

    result = process_data(raw_transactions)
    print("Data Cleaner Summary:")
    print(result)
