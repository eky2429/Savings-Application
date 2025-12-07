from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QWidget, QMessageBox, QSpinBox
)
from PyQt6.QtCore import Qt


MAX_BINS = 20
MIN_PERCENT = 2
MAX_PERCENT = 100


class SettingsDialog(QDialog):
    #For now, NOTHING is passed in for existing_rule
    def __init__(self, parent=None, existing_rule=None):

        super().__init__(parent)
        self.setWindowTitle("Custom Rule Settings")

        #Stores the bins in the array
        self.bins : list = []  # list of (name_input, percent_input)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # --- Title ---
        title = QLabel("Create Custom Rule")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        main_layout.addWidget(title)

        # --- Rule Name Input ---
        self.rule_name_input = QLineEdit()
        self.rule_name_input.setPlaceholderText("Enter a name for this rule (e.g., My Custom Rule)")
        main_layout.addWidget(self.rule_name_input)

        # --- Scrollable Bin List ---
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        self.bin_layout = QVBoxLayout(container)
        scroll.setWidget(container)
        main_layout.addWidget(scroll, stretch=1)

        # --- Buttons: Add Bin ---
        add_button = QPushButton("Add Bin")
        add_button.clicked.connect(lambda: self.add_bin()) #Prevents the signal from passing a boolean!
        main_layout.addWidget(add_button)

        # --- Save Button ---
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.on_save)

        # --- Cancel Button ---
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)

        #Button row for storing the buttons
        button_row = QHBoxLayout()
        button_row.addWidget(save_button)
        button_row.addWidget(cancel_button)
        main_layout.addLayout(button_row)

        # Prefill if a rule exists
        if existing_rule:
            print("Found existing rule")
            for name, percent in existing_rule.items():
                self.add_bin(name, percent)

    # ---------------------------------------------------
    # Add a new bin row
    # ---------------------------------------------------
    def add_bin(self, name="", percent=MIN_PERCENT):
        if len(self.bins) >= MAX_BINS:
            QMessageBox.warning(self, "Limit Reached", f"Maximum {MAX_BINS} bins allowed.")
            return

        row = QHBoxLayout()

        #Creates name input
        name_input = QLineEdit()
        name_input.setPlaceholderText("Bin name (e.g., Savings)")
        print(name)
        name_input.setText(name)

        # Creates percentage input
        percent_input = QSpinBox()
        percent_input.setRange(MIN_PERCENT, MAX_PERCENT)
        percent_input.setValue(percent)
        percent_input.setSuffix(" %")

        # Creates remove button
        remove_button = QPushButton("X")
        remove_button.setFixedWidth(40)

        # Remove row logic
        def remove_this():
            # Remove widgets
            name_input.deleteLater()
            percent_input.deleteLater()
            remove_button.deleteLater()

            row.deleteLater()
            self.bins.remove((name_input, percent_input))
        remove_button.clicked.connect(remove_this)

        #Adds widgets to row
        row.addWidget(name_input, stretch=2)
        row.addWidget(percent_input, stretch=1)
        row.addWidget(remove_button)

        #Adds row to bin_layout
        self.bin_layout.addLayout(row)
        self.bins.append((name_input, percent_input))

    # ---------------------------------------------------
    # Save (Validate + Return Data)
    # ---------------------------------------------------
    def on_save(self):
        rule = {}
        total_percent = 0

        """ERROR HANDLING!"""
        rule_name = self.rule_name_input.text()
        if not rule_name:
            QMessageBox.warning(self, "Invalid Input", "Rule name cannot be empty.")
            return

        for name_input, percent_input in self.bins:
            name = name_input.text().strip()
            percent = percent_input.value()

            if not name:
                QMessageBox.warning(self, "Invalid Input", "Bin name cannot be empty.")
                return

            if name in rule:
                QMessageBox.warning(self, "Invalid Input", "Duplicate bin names are not allowed.")
                return

            rule[name] = percent
            total_percent += percent

        if total_percent != 100:
            QMessageBox.warning(self, "Invalid Total",
                                f"Total percentage must equal 100%.\nCurrently: {total_percent}%")
            return

        # If everything is valid, store and return
        self.rule_name = rule_name
        self.custom_rule = rule
        self.accept()

    # ---------------------------------------------------
    # Helper: Return result to main window
    # ---------------------------------------------------
    def get_rule(self):
        """
        Returns the custom rule dictionary after dialog closes.
        Example:
        {
            "Needs": 40,
            "Wants": 30,
            "Savings": 30
        }

        If custom_rule does not exist, returns None.
        """
        return getattr(self, "custom_rule", None)

    #Helper that gets the rule name
    def get_rule_name(self):
        return getattr(self, "rule_name", None)