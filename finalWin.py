from instr import *
from testWin import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout)

class FinalWin(QWidget):
    def __init__(self, index=None, name =None, age=None, result=None):
        super().__init__()
        self.name = name
        self.age = age
        self.index = index
        self.result = result
        self.set_appear()
        self.initUI()
        self.show()


    def get_ruffier_level(self, age, index):
        if age >= 15:
            if index >= 15:
                return "Низький"
            elif index >= 11:
                return "Задовільний"
            elif index >= 6:
                return "Середній"
            elif index >= 0.5:
                return "Вище середнього"
            else:
                return "Високий"

        elif age >= 13:
            if index >= 16.5:
                return "Низький"
            elif index >= 12.5:
                return "Задовільний"
            elif index >= 7.5:
                return "Середній"
            elif index >= 2:
                return "Вище середнього"
            else:
                return "Високий"

        elif age >= 11:
            if index >= 18:
                return "Низький"
            elif index >= 14:
                return "Задовільний"
            elif index >= 9:
                return "Середній"
            elif index >= 3.5:
                return "Вище середнього"
            else:
                return "Високий"

        elif age >= 9:
            if index >= 19.5:
                return "Низький"
            elif index >= 15.5:
                return "Задовільний"
            elif index >= 10.5:
                return "Середній"
            elif index >= 5:
                return "Вище середнього"
            else:
                return "Високий"

        elif age >= 7:
            if index >= 21:
                return "Низький"
            elif index >= 17:
                return "Задовільний"
            elif index >= 12:
                return "Середній"
            elif index >= 6.5:
                return "Вище середнього"
            else:
                return "Високий"

        else:
            return "Невизначено (вік поза діапазоном таблиці)"

        



          
    def set_appear(self):
        self.setWindowTitle("Результати тестування")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.left_layout = QVBoxLayout()
        self.left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.left_layout.addSpacing(80)

        self.label_name = QLabel("Індекс руфь'є:" + str(self.index))
        self.label_name.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.left_layout.addWidget(self.label_name)
        self.left_layout.addSpacing(300)


        self.label_name = QLabel("Працездатність серця:" +self.get_ruffier_level(int(self.age), self.index))
        self.label_name.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.left_layout.addWidget(self.label_name)

        self.label_name = QLabel("Четвертий тест Мартіне Кушелевського: " + str(self.result), alignment=Qt.AlignmentFlag.AlignCenter)
        self.label_name.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.left_layout.addWidget(self.label_name)

        self.setLayout(self.left_layout)


