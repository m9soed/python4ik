from PySide6.QtCore import QSize, Qt, QDate, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QDateTimeEdit, QVBoxLayout, QTextEdit, QWidget

from datetime import datetime


class MainWindow(QMainWindow):

    @Slot()
    def timedelta(self):
        nowdate = datetime.now()

        delta = nowdate - datetime.strptime(self.dateTimeEdit.text(), "%d/%m/%Y")

        self.textEdit.setMarkdown("**1. Лет:** " + str(delta.days // 365) + "\n\n"
                                                                            "**2. Месяцев:** " + str(
            delta.days // 30) + "\n\n"
                                "**3. Дней:** " + str(delta.days) + "\n\n"
                                                                    "**4. Часов:** " + str(
            delta.total_seconds() // 3600) + "\n\n"
                                             "**5. Минут:** " + str(delta.total_seconds() // 60) + "\n\n"
                                                                                                   "**6. Секунд:** " + str(
            delta.total_seconds()) + "\n\n"
                                  )

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)

        layout = QVBoxLayout()

        self.dateTimeEdit = QDateTimeEdit(QDate.currentDate())
        self.dateTimeEdit.setMaximumDate(QDate.currentDate())
        self.dateTimeEdit.setDisplayFormat("dd/MM/yyyy")
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.dateChanged.connect(self.timedelta)

        layout.addWidget(self.dateTimeEdit)
        layout.addWidget(self.textEdit)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
