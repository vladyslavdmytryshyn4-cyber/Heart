from instr import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.label = QLabel("Введіть П.І.Б.:")
        self.line_edit = QLineEdit()
        self.label = QLabel("Повних років:")
        self.line_edit = QLineEdit()
        self.label = QLabel()


        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)



app = QApplication([])
win = TestWin()
win.show()
app.exec()
