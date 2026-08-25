from instr import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout)

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
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

        self.left_layout.addSpacing(80)

        self.label_name = QLabel("Індекс руфь'є: 0.0")
        self.left_layout.addWidget(self.label_name)
        self.left_layout.addSpacing(300)


        self.label_name = QLabel("Працездатність серця:" )
        self.left_layout.addWidget(self.label_name)

        self.setLayout(self.left_layout)




