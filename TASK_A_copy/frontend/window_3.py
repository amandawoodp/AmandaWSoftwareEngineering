from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QScrollArea
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os
from backend.logic import filter_exercises, exercises

class ThirdWindow(QMainWindow):
    def __init__(self, selected_exercises):
        super().__init__()
        self.setWindowTitle("QuickFit - Your Workout")
        self.setFixedSize(800, 800)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet("background-color: #071453;")
        
        self.layout = QVBoxLayout(self.central_widget)
        
        self.title_label = QLabel("Here are your exercises!")
        self.title_label.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("border: none;")
        self.layout.addWidget(self.scroll_area)
        
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        photos_dir = os.path.join(base_dir, "assets/photos")
        
        for exercise in selected_exercises:
            photo_path = os.path.join(photos_dir, f"{exercise.number}.jpg")  
            if os.path.exists(photo_path):
                exercise_label = QLabel(f"{exercise.name} (Time: {exercise.time}s)")
                exercise_label.setStyleSheet("color: white; font-size: 20px;")
                exercise_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.scroll_layout.addWidget(exercise_label, alignment=Qt.AlignmentFlag.AlignCenter)

                pixmap = QPixmap(photo_path)
                photo_label = QLabel(self)
                photo_label.setPixmap(pixmap)
                photo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                photo_label.setScaledContents(True)
                photo_label.setFixedSize(500, 500)  
                self.scroll_layout.addWidget(photo_label, alignment=Qt.AlignmentFlag.AlignCenter)
            else:
                missing_label = QLabel(f"Photo not found for {exercise.name}")
                missing_label.setStyleSheet("color: red; font-size: 16px;")
                missing_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.scroll_layout.addWidget(missing_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.scroll_area.setWidget(self.scroll_content)

        self.back_button = QPushButton("Back to Main Menu")
        self.back_button.setStyleSheet("background-color: blue; color: white; font-size: 20px;")
        self.back_button.clicked.connect(self.back_to_main)
        self.layout.addWidget(self.back_button, alignment=Qt.AlignmentFlag.AlignCenter)

    def back_to_main(self):
        self.close()
        from frontend.main import MainWindow
        self.main_window = MainWindow()
        self.main_window.show()
