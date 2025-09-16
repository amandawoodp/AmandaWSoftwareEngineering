from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QCheckBox, QPushButton)
from backend.logic import filter_exercises, exercises
from frontend.window_3 import ThirdWindow

class SecondWindow(QMainWindow):
    """
    Shows second window 
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickFit")
        self.setFixedSize(800, 800)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.setStyleSheet("background-color: #071453;")

        self.time_section = QVBoxLayout()
        self.time_label = QLabel("How much time do you have for your workout?")
        self.time_label.setStyleSheet("color: white; font-size: 20px;")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_section.addWidget(self.time_label)
        self.time_combo_box = QComboBox()
        self.time_combo_box.setStyleSheet("background-color: white; color: black; font-size: 20px;")
        self.time_combo_box.addItems([f"{i} minutes" for i in range(1, 31)])
        self.time_section.addWidget(self.time_combo_box, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addLayout(self.time_section)

        self.implements_section = QVBoxLayout()
        self.implements_label = QLabel("What implements do you have right now?")
        self.implements_label.setStyleSheet("color: white; font-size: 20px;")
        self.implements_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.implements_section.addWidget(self.implements_label)

        self.checkboxes_layout = QHBoxLayout()
        self.options = ["Floor Space", "Wall", "Chair", "None"]
        self.checkboxes = []
        for option in self.options:
            checkbox = QCheckBox(option)
            checkbox.setStyleSheet("color: white; font-size: 16px;")
            self.checkboxes.append(checkbox)
            self.checkboxes_layout.addWidget(checkbox)
        self.implements_section.addLayout(self.checkboxes_layout)
        self.main_layout.addLayout(self.implements_section)

        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch()
        self.create_workout_button = QPushButton("Create my Work Out!")
        self.create_workout_button.setObjectName("createWorkoutButton")

        self.create_workout_button.setStyleSheet(
            "background-color: blue; color: white; font-size: 20px;")
        self.create_workout_button.clicked.connect(self.create_workout)
        self.button_layout.addWidget(
            self.create_workout_button, alignment=Qt.AlignmentFlag.AlignRight)
        self.main_layout.addLayout(self.button_layout)

    def create_workout(self) -> None:
        """
        Generates a workout 
        """
        selected_time = int(self.time_combo_box.currentText().split()[0]) * 60
        selected_implements = [box.text() for box in self.checkboxes if box.isChecked()]

        filtered = filter_exercises(exercises, selected_implements, selected_time)

        self.third_window = ThirdWindow(filtered)
        self.third_window.show()
        self.close()
