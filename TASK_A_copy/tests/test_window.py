import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PyQt6.QtWidgets import QApplication, QPushButton
from frontend.window_2 import SecondWindow


class TestSecondWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configurar QApplication una vez para todas las pruebas."""
        cls.app = QApplication([])

    def setUp(self):
        """Configurar la instancia de la ventana para las pruebas."""
        self.window = SecondWindow()

    def test_window_size(self):
        """Prueba que la ventana tenga el tamaño correcto."""
        self.assertEqual(self.window.size().width(), 800)
        self.assertEqual(self.window.size().height(), 800)

    def test_implements(self):
        """Prueba que los checkboxes tengan las opciones correctas."""
        expected_options = ["Floor Space", "Wall", "Chair", "None"]
        checkboxes = self.window.checkboxes
        self.assertEqual(len(checkboxes), len(expected_options))
        for checkbox, expected_text in zip(checkboxes, expected_options):
            self.assertEqual(checkbox.text(), expected_text)

    def test_button(self):
        """Prueba que el botón 'Create my Work Out!' esté presente y tenga el texto correcto."""
        create_workout_button = self.window.findChild(QPushButton, "createWorkoutButton")
        self.assertIsNotNone(create_workout_button)
        self.assertEqual(create_workout_button.text(), "Create my Work Out!")

if __name__ == "__main__":
    unittest.main()
