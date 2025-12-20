from core.rule_storage import *

def test_custom_rule():
    custom_rule = {"RuleA" : {"A": 40, "B": 60} }
    save_custom_rule("RuleA", custom_rule["RuleA"])

    my_dict : dict = load_custom_rules()
    assert custom_rule in my_dict

    delete_custom_rule("RuleA")
    my_dict = load_custom_rules()
    assert not(custom_rule in my_dict)

def test_corrupt_json():
    no_rules_file = os.path.join("data", "no_rules.json")
    ensure_file_exists()
    os.remove(no_rules_file)