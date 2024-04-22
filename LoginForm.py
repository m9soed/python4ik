from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFormLayout, QLabel, QCheckBox, QMessageBox, QComboBox
from PySide6.QtCore import Slot
import re


class Window(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Данные об аккаунте")
        self.setMinimumSize(365, 230)

        layout = QFormLayout()

        self.surname = QLabel("Фамилия: ")
        self.surname_field = QLineEdit()
        layout.addRow(self.surname, self.surname_field)

        self.name = QLabel("Имя: ")
        self.name_field = QLineEdit()
        layout.addRow(self.name, self.name_field)

        self.patronymic = QLabel("Отчество: ")
        self.patronymic_field = QLineEdit()
        layout.addRow(self.patronymic, self.patronymic_field)

        self.mail = QLabel("Почта: ")
        self.mail_field = QLineEdit()
        layout.addRow(self.mail, self.mail_field)

        self.phone_number = QLabel("Номер телефона: ")
        self.phone_number_field = QLineEdit()
        layout.addRow(self.phone_number, self.phone_number_field)

        self.hobbies = QLabel("Увлечения:")
        self.combobox = QComboBox()
        self.combobox.addItems(["Моделирование", "Музыка", "Путешествия"])
        layout.addRow(self.hobbies, self.combobox)

        personal_data_consent = QCheckBox("Я согласен с политикой обработки персональных данных")
        layout.addRow(personal_data_consent)

        advertising_offers_consent = QCheckBox("Я хочу получать рекламные предложения")
        layout.addRow(advertising_offers_consent)

        apply_btn = QPushButton("Применить")
        layout.addRow(apply_btn)
        apply_btn.clicked.connect(self.checkValidation)

        self.setLayout(layout)

    def validateFullName(self, name):
        if re.match(r"^[а-яА-Я]+$", name):
            return True
        else:
            return False

    def validateMail(self, mail):
        if re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", mail):
            return True
        else:
            return False

    def validateNumber(self, number):
        if re.match(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", number):
            return True
        else:
            return False

    @Slot(str)
    def checkValidation(self):
        if self.validateFullName(self.surname_field.text()) and self.validateFullName(
                self.name_field.text()) and self.validateFullName(self.patronymic_field.text()) and self.validateMail(self.mail_field.text()) and self.validateNumber(self.phone_number_field.text()):

            message = QMessageBox()
            message.setText("Всё верно!")
            message.setWindowTitle("Успех!")
            message.exec()
        else:
            message = QMessageBox()
            message.setText("Проверьте правильность введённых данных")
            message.setWindowTitle("Ошибка!")
            message.exec()


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
