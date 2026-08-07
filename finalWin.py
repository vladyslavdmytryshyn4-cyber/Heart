from instr import *
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout)

class FinalWin(QWidget):
    def __init__(self, data=None):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle("Результати тестування")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.left_layout = QVBoxLayout()
        self.left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.label_name = QLabel("Індекс руфь'є: 0.0")
        self.left_layout.addWidget(self.label_name)



app = QApplication([])

