from gui.main_window import MainWindow
from core.rules import *

def test_display_allocations():
    salary = 500
    window = MainWindow()
    window.on_combo_box_changed(prebuilt_rules.values()[0])
    window.salary_input.setText(str(salary))
    window.on_button_clicked()

    output_text = window.output_label.text()
    assert output_text == "Needs: 250\nWants: 100\n Savings: 150"
    print(output_text)

def test_change_rule():
    salary = 500
    window = MainWindow()
    window.on_combo_box_changed(prebuilt_rules.values()[1])
    window.salary_input.setText(str(salary))
    window.on_button_clicked()

    output_text = window.output_label.text()
    assert output_text == "Needs: 250\nWants: 50\n Savings: 200"
    print(output_text)

"""MODIFY TEST SO IT ADDS CUSTOM RULE"""
def test_custom_rule():
    salary = 500
    window = MainWindow()
    window.on_combo_box_changed(prebuilt_rules.values()[1])
    window.salary_input.setText(str(salary))
    window.on_button_clicked()

    output_text = window.output_label.text()
    assert output_text == "Needs: 250\nWants: 50\n Savings: 200"

    from core.rule_storage import save_custom_rule, delete_custom_rule
    custom_rule = {"RuleA": {"A": 40, "B": 60}}
    save_custom_rule("RuleA", custom_rule["RuleA"])

    window.refresh_dropdown()
    window.on_combo_box_changed(prebuilt_rules.values()[1])
    window.salary_input.setText(str(salary))
    window.on_button_clicked()

    salary = 1000
    window.salary_input.setText(str(salary))
    window.on_button_clicked()
    output_text = window.output_label.text()
    assert output_text == "A: 200\nB: 300"

    delete_custom_rule("RuleA")