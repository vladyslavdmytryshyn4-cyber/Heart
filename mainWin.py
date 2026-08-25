from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
              QPushButton, QLabel, QLineEdit)

from instr import *
       
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        # створюємо та налаштовуємо графічні елементи:
        self.initUI()
        #Встановлює зв'язки між елементами
        self.connects()
        #Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.set_appear()
        # старт:
        self.show()
    def initUI(self):
        ''' створює графічні елементи '''
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        pass

    ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


app = QApplication([])
mw = MainWin()
app.exec_()

