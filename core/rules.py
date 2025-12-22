# core/rules.py

prebuilt_rules = {
    "50/30/20": {"Needs": 50, "Wants": 30, "Savings": 20},
    "50/10/40": {"Needs": 50, "Wants": 10, "Savings": 40},
}

"""
def is_valid_rule(rule: dict) -> bool:
    #Ensure percentages sum to 100 and values are ints.

    #Checks if rule is a dictionary; if not, then we return false
    if not isinstance(rule, dict):
        return False
    total = sum(rule.values())
    #Othewise we determine sum of values and check if all values in rules are an integer
    return total == 100 and all(isinstance(v, int) for v in rule.values())

def get_rule(name: str):
    return prebuilt_rules.get(name)
"""