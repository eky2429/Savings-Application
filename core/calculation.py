#core.calculation

def calculate_allocations(salary: float, rule: dict) -> dict:
    """
    Calculates how much money goes into each bin using balanced rounding.
    Ensures that the final rounded amounts add up exactly to the salary.
    """

    # Step 1: raw calculations (not rounded)
    raw = {name: salary * (percent / 100) for name, percent in rule.items()}

    # Step 2: preliminary rounded values
    rounded = {name: round(value, 2) for name, value in raw.items()}

    # Step 3: check if rounding changed the total
    total_rounded = sum(rounded.values())
    diff = round(salary - total_rounded, 2)

    if diff == 0:
        return rounded  # Perfect match

    # Step 4: fix the difference by adjusting the largest fractional part
    # Find the bin with the largest decimal remainder
    remainders = {
        name: (raw[name] - int(raw[name]))  # fractional part only
        for name in rule.keys()
    }

    # Find the bin most “deserving” of the adjustment
    target_bin = max(remainders, key=remainders.get)

    # Apply the correction
    rounded[target_bin] += diff
    rounded[target_bin] = round(rounded[target_bin], 2)

    return rounded