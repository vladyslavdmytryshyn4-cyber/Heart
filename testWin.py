from instr import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout)
from finalWin import FinalWin

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def send_data(self):
        txt_name = self.line_name.text()
        txt_age = self.line_age.text()
        txt_test1 = self.line_test1.text()
        txt_test2 = self.line_test2.text()
        txt_test3 = self.line_test3.text()
        txt_test4 = self.line_test4.text()
        txt_test4_1 = self.line_test4_1.text()


    def initUI(self):
        self.timer = QTimer()
        self.time_left = 0

        self.left_layout = QVBoxLayout()
        self.left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # П.І.Б.
        self.label_name = QLabel(txt_name)
        self.line_name = QLineEdit(txt_hintname)
        self.left_layout.addWidget(self.label_name)
        self.left_layout.addWidget(self.line_name)
        self.left_layout.addSpacing(15)

        self.label_age = QLabel(txt_age)
        self.line_age = QLineEdit(txt_hintage)
        self.left_layout.addWidget(self.label_age)
        self.left_layout.addWidget(self.line_age)
        self.left_layout.addSpacing(15)

        # Тест 1
        self.label_test1 = QLabel(txt_test1)
        self.label_test1.setWordWrap(True)
        self.btn_test1 = QPushButton(txt_start_test1)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.left_layout.addWidget(self.label_test1)
        self.left_layout.addWidget(self.btn_test1)
        self.left_layout.addWidget(self.line_test1)
        self.left_layout.addSpacing(15)

        # Тест 2
        self.label_test2 = QLabel(txt_test2)
        self.label_test2.setWordWrap(True)
        self.btn_test2 = QPushButton(txt_start_test2)
        self.left_layout.addWidget(self.label_test2)
        self.left_layout.addWidget(self.btn_test2)
        self.left_layout.addSpacing(15)

        # Тест 3
        self.label_test3 = QLabel(txt_test3)
        self.label_test3.setWordWrap(True)
        self.btn_test3 = QPushButton(txt_start_test3)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        self.left_layout.addWidget(self.label_test3)
        self.left_layout.addWidget(self.btn_test3)
        self.left_layout.addWidget(self.line_test2)
        self.left_layout.addWidget(self.line_test3)
        self.left_layout.addSpacing(15)

        # Тест 4
        self.label_test4 = QLabel(txt_test4)
        self.label_test4.setWordWrap(True)
        self.btn_test4 = QPushButton(txt_start_test4)
        self.line_test4 = QLineEdit(txt_hinttest4)
        self.label_test4_1 = QLabel(txt_test4_1)
        self.line_test4_1 = QLineEdit(txt_hinttest4_1)
        self.btn_test4_1 = QPushButton(txt_start_test4_1)
        self.left_layout.addWidget(self.label_test4)
        self.left_layout.addWidget(self.btn_test4)
        self.left_layout.addWidget(self.line_test4)
        self.left_layout.addWidget(self.label_test4_1)
        self.left_layout.addWidget(self.btn_test4_1)
        self.left_layout.addWidget(self.line_test4_1)
        self.left_layout.addSpacing(15)


        self.btn_send = QPushButton(txt_sendresults)
        self.left_layout.addWidget(self.btn_send, alignment=Qt.AlignmentFlag.AlignCenter)

        self.btn_next = QPushButton("Далі")
        self.left_layout.addWidget(self.btn_next, alignment=Qt.AlignmentFlag.AlignCenter)

        self.right_layout = QVBoxLayout()
        self.right_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.timer_label = QLabel("00:00:15")
        self.timer_label.setStyleSheet("font-size: 48px; font-weight: bold;")
        self.right_layout.addWidget(self.timer_label)

        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(self.left_layout, stretch=3)
        self.main_layout.addLayout(self.right_layout, stretch=1)

        self.setLayout(self.main_layout)

    def connects(self):
        self.btn_test1.clicked.connect(self.start_test1)
        self.btn_test2.clicked.connect(self.start_test2)
        self.btn_test3.clicked.connect(self.start_test3)
        self.btn_test4.clicked.connect(self.start_test4)
        self.btn_test4_1.clicked.connect(self.start_test4_1)
        self.btn_send.clicked.connect(self.send_results)
        self.btn_next.clicked.connect(self.next_click)
        self.timer.timeout.connect(self.timer_event)

    def Experiment():
        return {
            "age": self.line_age.text(),
            "test1": self.line_test1.text(),
            "test2": self.line_test2.text(),
            "test3": self.line_test3.text(),
            "test4": self.line_test4.text(),
            "test4_1": self.line_test4_1.text()
        }

    def next_click(self):
        data = self.send_data()
        self.hide()
        self.exp = self.Experiment(self.line_age, self.line_test1, self.line_test2, self.line_test3, self.line_test4, self.line_test4_1)
        self.tw = FinalWin(self.exp)

    def result(self):
        self.index = (4 * (int(self.exp.test1()) + int(self.exp.test2()) + int(self.exp.test3())) - 200) / 10


    def start_test1(self):
        self.time_left = 15
        self.update_timer_label()
        self.timer.start(1000)
        self.btn_test1.setEnabled(False)

    def start_test2(self):
        self.time_left = 45
        self.update_timer_label()
        self.timer.start(1000)
        self.btn_test2.setEnabled(False)

    def start_test3(self):
        self.time_left = 60
        self.update_timer_label()
        self.timer.start(1000)
        self.btn_test3.setEnabled(False)

    def start_test4(self):
        self.time_left = 20
        self.update_timer_label()
        self.timer.start(1000)
        self.btn_test4.setEnabled(False)

    def start_test4_1(self):
        self.time_left = 180  # 3 хвилини
        self.update_timer_label()
        self.timer.start(1000)
        self.btn_test4_1.setEnabled(False)

    def timer_event(self):
        self.time_left -= 1
        self.update_timer_label()
        if self.time_left <= 0:
            self.timer.stop()

    def update_timer_label(self):
        hours = self.time_left // 3600
        minutes = (self.time_left % 3600) // 60
        seconds = self.time_left % 60
        self.timer_label.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    def send_results(self):
        name = self.line_name.text()
        age = self.line_age.text()
        test1 = self.line_test1.text()
        test2 = self.line_test2.text()
        test3 = self.line_test3.text()
        test4 = self.line_test4.text()
        test4_1 = self.line_test4_1.text()

app = QApplication([])
win = TestWin()
app.exec()