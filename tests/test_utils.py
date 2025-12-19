from core.utils import format_salary

def test_format_salary():
    assert format_salary("5000") == 5000

def test_format_salary2():
    assert format_salary("1234.56") == 1234.56

def test_format_salary3():
    assert format_salary("10.9999999") == 10.99

def test_format_salary_error():
    assert format_salary("-300") == None

def test_format_salary_error2():
    assert format_salary("abc123") == None

def test_format_salary_spaces():
    assert format_salary("4500.50 ") == 4500.50