from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QRadioButton, \
    QButtonGroup
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):

    @Slot()
    def clicked_radiobuttons(self):
        if self.group.checkedId() == 1:
            self.label.setText("Самое холодное время года")
        elif self.group.checkedId() == 2:
            self.label.setText("Cезон между зимой и летом")
        elif self.group.checkedId() == 3:
            self.label.setText("Самое тёплое время года")
        else:
            self.label.setText("Cезон между летом и зимой")

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()
        laYout = QHBoxLayout()

        radioWinter = QRadioButton('Зима')
        radioWinter.setChecked(True)
        radioSpring = QRadioButton('Весна')
        radioSummer = QRadioButton('Лето')
        radioAutumn = QRadioButton('Осень')
        self.group = QButtonGroup()
        self.group.addButton(radioWinter, id=1)
        self.group.addButton(radioSpring, id=2)
        self.group.addButton(radioSummer, id=3)
        self.group.addButton(radioAutumn, id=4)

        layout.addWidget(radioWinter)
        layout.addWidget(radioSpring)
        layout.addWidget(radioSummer)
        layout.addWidget(radioAutumn)

        self.label = QLabel("Самое холодное время года")
        self.label.setWordWrap(True)

        laYout.addLayout(layout)
        laYout.addWidget(self.label)

        container = QWidget()
        container.setLayout(laYout)

        self.group.buttonClicked.connect(self.clicked_radiobuttons)
        self.setCentralWidget(container)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
