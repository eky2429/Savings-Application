"""
from core.rules import is_valid_rule, prebuilt_rules

def test_prebuilt_rules():
    for value in prebuilt_rules.values():
        assert(is_valid_rule(value) == True)

def test_custom_valid_rule():
    rule = {"A": 40, "B": 30, "C": 30}
    assert(is_valid_rule(rule) == True)

def test_custom_invalid_rule():
    rule = {"A": 40, "B": 40, "C": 10}
    assert(is_valid_rule(rule) != True)

def test_few_bins():
    rules = [{}, {"A": 100}]
    for rule in rules:
        assert(is_valid_rule(rule) == False)

def test_many_bins():
    rule = {"A": 5, "B": 5, "C": 5, "D": 5, "E": 5,
      "A1": 5, "B1": 5, "C1": 5, "D1": 5, "E1": 5,
      "A2": 5, "B2": 5, "C2": 5, "D2": 5, "E2": 5,
      "A3": 5, "B3": 5, "C3": 5, "D3": 5, "E3": 2,
            "A4": 3,}
    assert(is_valid_rule(rule) == False)

def test_small_percentage():
    rule = {"A": 1, "B": 99}
    assert(is_valid_rule(rule) == False)

test_prebuilt_rules()
test_custom_valid_rule()
test_custom_invalid_rule()
test_few_bins()
test_many_bins()
test_small_percentage()
"""