import unittest
from PyQt6.QtWidgets import QApplication
from window_2 import SecondWindow

app = QApplication([])
def test_window_size(self):
    self.assertEqual(self.window.size().width(), 800)
    self.assertEqual(self.window.size().height(), 800)

def test_implements(self):
    expected_options = ["Floor Space", "Wall", "Chair", "None"]
    checkboxes = self.window.checkboxes
    self.assertEqual(len(checkboxes), len(expected_options))  
    for checkbox, expected_text in zip(checkboxes, expected_options):
        self.assertEqual(checkbox.text(), expected_text)

def test_button(self):
    create_workout_button = self.window.findChild(QPushButton)
    self.assertIsNotNone(create_workout_button)
    self.assertEqual(create_workout_button.text(), "Create my Work Out!")

if __name__ == "__main__":
    unittest.main()
