# Listing 57. basic/dialogs_input_2.py

import sys
import random

from PySide6.QtWidgets import (
    QApplication,
    QInputDialog,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Тест на геншинфага")

        layout = QVBoxLayout()

        button1 = QPushButton("Калькулятор проданных родителей")
        button1.clicked.connect(self.get_an_int)
        layout.addWidget(button1)

        button2 = QPushButton("Калькулятор проданных почек")
        button2.clicked.connect(self.get_a_float)
        layout.addWidget(button2)

        button3 = QPushButton("Тест на вашу личность")
        button3.clicked.connect(self.get_a_str_from_a_list)
        layout.addWidget(button3)

        button4 = QPushButton("Ваш гендер")
        button4.clicked.connect(self.get_a_str)
        layout.addWidget(button4)

        button5 = QPushButton("Напишите свой фанфик")
        button5.clicked.connect(self.get_text)
        layout.addWidget(button5)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_an_int(self):
        my_int_value, ok = QInputDialog.getInt(
            self, "Сколько у вас легендарных персонажей?", "Введите число"
        )
        print("Вы продали", my_int_value*(random.randint(1,5)), "родителей")

    def get_a_float(self):
        my_int_value, ok = QInputDialog.getInt(
            self, "Сколько у вас легендарного оружия?", "Введите число"
        )
        print("Вы продали", my_int_value*(random.randint(1,4)), "почек")

    def get_a_str_from_a_list(self):
        title = "Ваш любимый персонаж"
        label = "Выберите вашего любимого персонажа"
        items = ["Кли", "Венти", "Скарамучча", "Сяо"]
        initial_selection = 2  # orange, indexed from 0
        my_selected_str, ok = QInputDialog.getItem(
            self,
            title,
            label,
            items,
            current=initial_selection,
            editable=False,
        )
        if my_selected_str == "Венти":
            print("Вы гей")
        if my_selected_str == "Кли":
            print("Вы педофил")
        if my_selected_str == "Скарамучча":
            print("Вы куколд")
        if my_selected_str == "Сяо":
            print("Вы женщина")


    def get_a_str(self):
        title = "Введите ваш гендер"
        label = "Ваш гендер"
        text = "Джо Байден"
        mode = QLineEdit.Password
        my_selected_str, ok = QInputDialog.getText(
            self, title, label, mode, text
        )
        print("Вы", my_selected_str)

    def get_text(self):
        title = "Напишите ваш фанфик"
        label = "Введите сюда ваш сценарий для гачимучи"
        text = "Однажды Дед повысил стоимость молитв до 3000 примогемов......"
        my_selected_str, ok = QInputDialog.getMultiLineText(
            self, title, label, text
        )
        print(my_selected_str)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
