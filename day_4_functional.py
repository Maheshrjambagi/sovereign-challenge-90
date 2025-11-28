# day_4_functional.py

def celsius_to_fahrenheit(celsius_temp):
    """
    Converts a temperature in Celsius to Fahrenheit.
    ... (omitted for brevity)
    """
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return fahrenheit_temp


def clean_string(text):
    """
    Cleans a string by removing leading/trailing whitespace and
    converting it entirely to lowercase.

    A pure function: takes an argument and returns a value,
    with no side effects.
    """
    # 1. Remove leading and trailing whitespace
    stripped_text = text.strip()

    # 2. Convert the entire string to lowercase
    cleaned_text = stripped_text.lower()

    # 3. Return the processed string
    return cleaned_text

# --- Example of how to use the function (OUTSIDE the function) ---
# dirty_input = "  PyThOn iS fUN!  "
# clean_output = clean_string(dirty_input)
# print(f"Input: '{dirty_input}'")
# print(f"Output: '{clean_output}'") # Output: 'python is fun!'