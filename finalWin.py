from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from instr import *

class FinalWin(QWidget):
    def __init__(self, data=None):
        super().__init__()
        self.data = data if data is not None else {}
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle("Результати тестування")
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(15)

