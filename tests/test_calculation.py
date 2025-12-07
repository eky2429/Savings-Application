from core.calculation import calculate_allocations

def test_basic_rule():
    result = calculate_allocations(1000, {"Needs": 50, "Wants": 50})
    assert result["Needs"] == 500
    assert result["Wants"] == 500

def test_balanced_rounding():
    rule = {"Needs": 51, "Wants": 49}
    out = calculate_allocations(50, rule)

    assert round(sum(out.values()), 2) == 50