from core.rule_storage import *

def test_custom_rule():
    custom_rule = {"RuleA" : {"A": 40, "B": 60} }
    save_custom_rule("RuleA", custom_rule["RuleA"])

    my_dict : dict = load_custom_rules()
    assert my_dict.get("RuleA") == custom_rule["RuleA"]

    delete_custom_rule("RuleA")
    my_dict = load_custom_rules()
    assert not(my_dict.get("RuleA") == custom_rule["RuleA"])

def test_corrupt_json():
    no_rules_file = os.path.join("data", "no_rules.json")
    ensure_file_exists(no_rules_file)
    os.remove(no_rules_file)

test_custom_rule()
test_corrupt_json()