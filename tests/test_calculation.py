from core.calculation import calculate_allocations

def test_basic_rule():
    result = calculate_allocations(1000, {"Needs": 50, "Wants": 50})
    assert result["Needs"] == 500
    assert result["Wants"] == 500

def test_basic_rule2():
    salary = 1000

    from core.rules import prebuilt_rules
    result = calculate_allocations(salary, prebuilt_rules["50/30/20"])
    assert result["Needs"] == 500
    assert result["Wants"] == 300
    assert result["Savings"] == 200

    total = 0
    for num in result.values():
        total += num
    assert total == salary

def test_balanced_rounding():
    salary = 50

    rule = {"Needs": 51, "Wants": 49}
    out = calculate_allocations(salary, rule)

    assert out["Needs"] == 25.5
    assert out["Wants"] == 24.5

    total = 0
    for num in out.values():
        total += num
    assert total == salary

def test_round_mismatch():
    salary = 100

    rule = {"A": 33, "B": 33, "C": 34}
    out = calculate_allocations(salary, rule)

    assert out["A"] == 33
    assert out["B"] == 33
    assert out["C"] == 34

    total = 0
    for num in out.values():
        total += num
    assert total == salary

def test_fractional_rule():
    salary = 100

    rule = {"A": 33, "B": 33, "C": 34}
    out = calculate_allocations(salary, rule)

    assert out["A"] == 33
    assert out["B"] == 33
    assert out["C"] == 34

    total = 0
    for num in out.values():
        total += num
    assert total == salary

def test_complex_fractional_rule():
    salary = 999.99

    rule = {"A": 25.5, "B": 25.5, "C": 25.5, "D": 23.5}
    out = calculate_allocations(salary, rule)

    for key in rule.keys():
        assert out[key] == rule[key] * salary

    total = 0
    for num in out.values():
        total += num
    assert total == salary

def test_many_bins():
    salary = 500
    rule = {"A": 5, "B": 5, "C": 5, "D": 5, "E": 5,
      "A1": 5, "B1": 5, "C1": 5, "D1": 5, "E1": 5,
      "A2": 5, "B2": 5, "C2": 5, "D2": 5, "E2": 5,
      "A3": 5, "B3": 5, "C3": 5, "D3": 5, "E3": 5}

    out = calculate_allocations(salary, rule)

    for key in rule.keys():
        assert out[key] == rule[key] * salary

    total = 0
    for num in out.values():
        total += num
    assert total == salary

def test_small_salary():
    salary = 0.03
    rule = {"A": 50, "B": 50}

    out = calculate_allocations(salary, rule)

    expected_values = {"A": 0.02, "B": 0.01}
    for key in rule.keys():
        assert out[key] == expected_values[key]

    total = 0
    for num in out.values():
        total += num
    assert total == salary