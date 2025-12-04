from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Sets title of window
        self.setWindowTitle("Savings App GUI")

        # Basic GUI setup for Milestone 1
        layout = QVBoxLayout()

        #Salary input
        self.salary_input = QLineEdit()
        self.salary_input.setPlaceholderText("Enter salary")
        layout.addWidget(self.salary_input)

        #Calculate button
        self.calc_button = QPushButton("Calculate")
        self.calc_button.clicked.connect(self.on_button_clicked) #This function works!
        layout.addWidget(self.calc_button)

        #Text
        self.output = QLabel("Bin results will appear here...")
        self.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.output)

        #Creates container that stores al elements
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_button_clicked(self):
        salary = self.salary_input.text()
        self.output.setText(f"You entered: {salary}")