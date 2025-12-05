from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QLabel
from core.rules import prebuilt_rules
from gui.settings_dialog import SettingsDialog
from core.rule_storage import save_custom_rule, load_custom_rules

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Sets some variables
        self.current_rule = None  # holds custom OR prebuilt rule
        self.using_custom_rule = False  # flag to track rule source

        #Sets title of window
        self.setWindowTitle("Savings App GUI")

        # Basic GUI setup for Milestone 1
        layout = QVBoxLayout()

        #Update Settings Button
        self.settings_button = QPushButton("Settings")
        self.settings_button.clicked.connect(self.open_settings)
        layout.addWidget(self.settings_button)

        #Settings input
        label = QLabel("Current Settings: ", self)
        layout.addWidget(label)
        self.rule_selector = QComboBox()
        self.rule_selector.addItem("Select rule...")
        self.refresh_dropdown()
        layout.addWidget(self.rule_selector)

        # Connect the QComboBox's currentTextChanged signal to a slot
        self.rule_selector.currentTextChanged.connect(self.on_combo_box_changed) #This function works too!

        #Salary input
        self.salary_input = QLineEdit()
        self.salary_input.setPlaceholderText("Enter salary")
        layout.addWidget(self.salary_input)

        #Calculate button
        self.calc_button = QPushButton("Calculate")
        self.calc_button.clicked.connect(self.on_button_clicked) #This function works!
        layout.addWidget(self.calc_button)

        #Text
        self.output_label = QLabel("Bin results will appear here...")
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.output_label)

        #Creates container that stores al elements
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    """Called when button is clicked
    - Verifies salary input is correct
    - Gets the current rule
    - Displays results
    """
    def on_button_clicked(self):
        text = self.salary_input.text()

        #Check if salary_input is a float
        try:
            salary = float(text)
        except ValueError:
            self.output_label.setText("Enter a valid salary.")
            return

        # Use custom rule if active
        if self.using_custom_rule and self.current_rule:
            rule = self.current_rule
        else:
            # Use a prebuilt rule
            rule_name = self.rule_selector.currentText()
            from core.rules import prebuilt_rules
            rule = prebuilt_rules.get(rule_name)

        if not rule:
            self.output_label.setText("No valid rule selected.")
            return

        # Compute results
        results = {
            name: salary * (percent / 100)
            for name, percent in rule.items()
        }

        display = "\n".join(f"{name}: ${value:.2f}" for name, value in results.items())
        self.output_label.setText(display)

    def on_combo_box_changed(self, text):
        print(text)

    """Called when settings button is clicked
        - Opens up settings
        - Gets updated rule
        """
    def open_settings(self):
        # Now, we assign the current rule as a value of existing_rule
        dialog = SettingsDialog(self, existing_rule=self.current_rule)

        if dialog.exec():
            custom_rule = dialog.get_rule()
            rule_name = dialog.get_rule_name()

            # If there is a custom rule, we set the current rule to the custom rule
            if custom_rule:
                self.current_rule = custom_rule
                self.using_custom_rule = True

                # Save to JSON
                save_custom_rule(rule_name, custom_rule)

                # Refresh dropdown
                self.refresh_dropdown()
                self.output_label.setText(f"Saved and applied custom rule: {rule_name}")

    def refresh_dropdown(self):
        from core.rule_storage import load_custom_rules

        custom_rules = load_custom_rules()

        #Resets rule_selector
        self.rule_selector.clear()
        self.rule_selector.addItem("Select rule...")
        self.rule_selector.addItems(prebuilt_rules.keys())

        # Adds custom_rules
        for name in custom_rules.keys():
            self.rule_selector.addItem(name)