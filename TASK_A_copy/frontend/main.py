import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer
from frontend import window_2
from frontend.window_3 import ThirdWindow

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class MainWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.logo_path = os.path.join(base_dir, "assets/photos/complete_logo.png")
        self.typography_logo_path = os.path.join(base_dir, "assets/photos/typography_logo.png")

        self.setWindowTitle("QuickFit")
        self.setFixedSize(800, 800)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.setStyleSheet("background-color: #071453;")  

        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap(self.logo_path) 
        self.logo_label.setPixmap(self.logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.logo_label)
        
        self.timer = QTimer(self) 
        self.timer.timeout.connect(self.show_welcome_screen)
        self.timer.setSingleShot(True)
        self.timer.start(2000) 

    def show_welcome_screen(self):
        self.logo_label.deleteLater()
        self.typography_logo = QLabel(self)
        self.typography_logo_pixmap = QPixmap(self.typography_logo_path)
        self.typography_logo.setPixmap(self.typography_logo_pixmap)
        self.typography_logo.setFixedSize(150, 50)
        self.typography_logo.setScaledContents(True)
        self.layout.addWidget(self.typography_logo, alignment=Qt.AlignmentFlag.AlignTop 
                              | Qt.AlignmentFlag.AlignLeft)

        self.title_label = QLabel("Welcome to QuickFit")
        self.title_label.setStyleSheet("color: white; font-size: 36px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.subtitle_label = QLabel("Your personal assistant when it comes to working out anywhere.")
        self.subtitle_label.setStyleSheet("color: white; font-size: 20px;")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.subtitle_label)

        self.workout_button = QPushButton("Let's Work Out!")
        self.workout_button.setStyleSheet("background-color: blue; color: white; font-size: 30px;")
        self.workout_button.clicked.connect(self.open_second_window)
        self.layout.addWidget(self.workout_button, alignment=Qt.AlignmentFlag.AlignRight)

    def open_second_window(self):
        self.close()  
        self.second_window = window_2.SecondWindow()  
        self.second_window.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
