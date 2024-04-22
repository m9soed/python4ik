from PySide6.QtCore import QSize, Qt, Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, \
    QCheckBox, QWidget, QSpinBox, QHBoxLayout


class MainWindow(QMainWindow):

    @Slot()
    def checkButton(self):
        if self.check.isChecked():
            self.check.setFont(QFont("Roboto", 12, QFont.Bold))
            self.summ1 = 45 * int(self.spinBox.value())
            self.labPrice.setText("Стоимость: " + str(45 * int(self.spinBox.value())) + " руб")
            self.lableRezult.setText("Общая стоимость покупки: " + str(self.summ1 + self.summ2 + self.summ3) + " руб.")
        else:
            self.check.setFont(QFont("Seqoe UI", 9))
            self.summ1 = 0
            self.labPrice.setText("Стоимость: 0")
            self.lableRezult.setText("Общая стоимость покупки: " + str(self.summ1 + self.summ2 + self.summ3) + " руб.")

    @Slot()
    def checkButton2(self):
        if self.check2.isChecked():
            self.check2.setFont(QFont("Roboto", 12, QFont.Bold))
            self.summ2 = 80 * int(self.spinBox2.value())
            self.labPrice2.setText("Стоимость: " + str(80 * int(self.spinBox2.value())) + " руб")
            self.lableRezult.setText("Общая стоимость покупки: " + str(self.summ1 + self.summ2 + self.summ3) + " руб.")
        else:
            self.check2.setFont(QFont("Seqoe UI", 9))
            self.summ2 = 0
            self.labPrice2.setText("Стоимость: 0")
            self.lableRezult.setText("Общая стоимость покупки: " + str(self.summ1 + self.summ2 + self.summ3) + " руб.")

    @Slot()
    def checkButton3(self):
        if self.check3.isChecked():
            self.check3.setFont(QFont("Roboto", 12, QFont.Bold))
            self.summ3 = 125 * int(self.spinBox3.value())
            self.labPrice3.setText("Стоимость: " + str(125 * int(self.spinBox3.value())) + " руб")
            self.lableRezult.setText("Общая стоимость покупки: " + str(self.summ1 + self.summ2 + self.summ3) + " руб.")
        else:
            self.check3.setFont(QFont("Seqoe UI", 9))
            self.summ3 = 0
            self.labPrice3.setText("Стоимость: 0")
            self.lableRezult.setText("Общая стоимость покупки: " + str(self.summ1 + self.summ2 + self.summ3) + " руб.")

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        self.summ1 = 0

        self.summ2 = 0

        self.summ3 = 0

        self.lableRezult = QLabel("Общая стоимость покупки: " + str(self.summ1 + self.summ2 + self.summ3) + " руб.")

        self.check = QCheckBox("Молоко")
        self.check.stateChanged.connect(self.checkButton)

        lable = QLabel("Цена: 60 руб/шт")
        self.labPrice = QLabel("Стоимость: 0")

        self.spinBox = QSpinBox()
        self.spinBox.setRange(1, 1000)
        self.spinBox.setSuffix(" шт")
        self.spinBox.valueChanged.connect(self.checkButton)

        Layout = QHBoxLayout()

        Layout.addWidget(self.check)
        Layout.addWidget(lable)
        Layout.addWidget(self.spinBox)
        Layout.addWidget(self.labPrice)

        layout.addLayout(Layout)

        self.check2 = QCheckBox("Хлеб")
        self.check2.stateChanged.connect(self.checkButton2)

        lable2 = QLabel("Цена: 43 руб/шт")
        self.labPrice2 = QLabel("Стоимость: 0")

        self.spinBox2 = QSpinBox()
        self.spinBox2.setRange(1, 1000)
        self.spinBox2.setSuffix(" шт")
        self.spinBox2.valueChanged.connect(self.checkButton2)

        Layout = QHBoxLayout()

        Layout.addWidget(self.check2)
        Layout.addWidget(lable2)
        Layout.addWidget(self.spinBox2)
        Layout.addWidget(self.labPrice2)

        layout.addLayout(Layout)

        self.check3 = QCheckBox("Бутылка воды")
        self.check3.stateChanged.connect(self.checkButton3)

        lable3 = QLabel("Цена: 125 руб/шт")
        self.labPrice3 = QLabel("Стоимость: 0")

        self.spinBox3 = QSpinBox()
        self.spinBox3.setRange(1, 1000)
        self.spinBox3.setSuffix(" шт")
        self.spinBox3.valueChanged.connect(self.checkButton3)

        Layout = QHBoxLayout()

        Layout.addWidget(self.check3)
        Layout.addWidget(lable3)
        Layout.addWidget(self.spinBox3)
        Layout.addWidget(self.labPrice3)

        layout.addLayout(Layout)
        layout.addWidget(self.lableRezult)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
