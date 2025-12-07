from decimal import Decimal, ROUND_DOWN

def normalize_salary(text: str) -> float | None:
    """
    Converts user salary input to a float with 2 decimals (rounded down).
    Returns None if invalid.
    """
    try:
        value = Decimal(text)
        clean = value.quantize(Decimal("0.01"), rounding=ROUND_DOWN)
        return float(clean)
    except:
        return None


def format_salary(value: float) -> str:
    """Return salary as a string with exactly 2 decimal places."""
    return f"{value:.2f}"