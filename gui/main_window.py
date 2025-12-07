from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QLabel
from core.calculation import calculate_allocations
from core.rules import prebuilt_rules
from gui.settings_dialog import SettingsDialog
from core.rule_storage import save_custom_rule
from core.utils import normalize_salary, format_salary

select_rule_text = "Select rule..."

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Sets some variables
        self.cur_rule : dict = None  # holds custom OR prebuilt rule
        self.cur_rule_name = None #Holds the name of the current rule
        self.using_custom_rule : bool = False  # flag to track rule source

        #Sets title of window
        self.setWindowTitle("Savings App GUI")

        # Basic GUI setup for Milestone 1
        layout = QVBoxLayout()

        #Update Settings Button
        self.settings_button : QPushButton= QPushButton("Settings")
        self.settings_button.clicked.connect(self.open_settings)
        layout.addWidget(self.settings_button)

        #Settings input
        label : QLabel = QLabel("Current Settings: ", self)
        layout.addWidget(label)
        self.rule_selector : QComboBox = QComboBox()
        self.rule_selector.addItem(select_rule_text)
        self.refresh_dropdown()
        layout.addWidget(self.rule_selector)

        # Connect the QComboBox's currentTextChanged signal to a slot
        self.rule_selector.currentTextChanged.connect(self.on_combo_box_changed) #This function works too!

        #Salary input
        self.salary_input : QLineEdit= QLineEdit()
        self.salary_input.setPlaceholderText("Enter income")
        layout.addWidget(self.salary_input)

        #Calculate button
        self.calc_button : QPushButton = QPushButton("Calculate")
        self.calc_button.clicked.connect(self.on_button_clicked) #This function works!
        layout.addWidget(self.calc_button)

        self.output_label :QLabel = QLabel("Bin results will appear here...")
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.output_label)

        #Creates container that stores al elements
        container : QWidget = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    """Called when button is clicked
    - Verifies salary input is correct
    - Gets the current rule
    - Displays results
    """

    def on_button_clicked(self):
        raw_text = self.salary_input.text()
        salary = normalize_salary(raw_text)

        if salary is None:
            self.output_label.setText("Enter a valid salary (up to 2 decimals).")
            return

        # Auto-correct the text box to a clean version
        self.salary_input.setText(format_salary(salary))

        # Check if it is NOT the first option
        if self.cur_rule_name == select_rule_text:
            self.output_label.setText("Pick a rule.")
            return
        elif self.cur_rule_name in prebuilt_rules.keys():
            self.cur_rule = prebuilt_rules[self.cur_rule_name]
        else:
            from core.rule_storage import custom_rules
            self.cur_rule = custom_rules[self.cur_rule_name]

        # Compute results
        results = calculate_allocations(salary, self.cur_rule)
        display = "\n".join(f"{name}: ${value:.2f}" for name, value in results.items())
        self.output_label.setText(display)

    def on_combo_box_changed(self, text):
        print(text)
        self.cur_rule_name = text

    """Called when settings button is clicked
        - Opens up settings
        - Gets updated rule
        """
    def open_settings(self):
        # Now, we assign the current rule as a value of existing_rule
        dialog = SettingsDialog(self, existing_rule=self.cur_rule)

        if dialog.exec():
            custom_rule = dialog.get_rule()
            rule_name = dialog.get_rule_name()

            # If there is a custom rule, we set the current rule to the custom rule
            if custom_rule:
                self.cur_rule = custom_rule
                self.using_custom_rule = True

                # Save to JSON
                save_custom_rule(rule_name, custom_rule)

                # Refresh dropdown
                self.refresh_dropdown()
                self.output_label.setText(f"Saved and applied custom rule: {rule_name}")

    def refresh_dropdown(self):
        from core.rule_storage import custom_rules

        #Resets rule_selector
        self.rule_selector.clear()
        self.rule_selector.addItem("Select rule...")
        self.rule_selector.addItems(prebuilt_rules.keys())

        # Adds custom_rules
        for name in custom_rules.keys():
            self.rule_selector.addItem(name)