<<<<<<< HEAD
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QApplication
from PyQt6.QtCore import Qt
=======
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
>>>>>>> 96238404d2a7eb886056ce3b23861440f833b794
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

        self.label_name = QLabel("Індекс руфь'є: 0.0")
        layout.addWidget(self.label_name)

app = QApplication([])
app.exec()
