from PySide6.QtCore import Signal, Qt, Slot, QMimeData
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QPushButton
from PySide6.QtGui import QDrag


class DragButton(QPushButton):

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            drag.setMimeData(QMimeData())
            drag.exec(Qt.MoveAction)


class LogLabel(QLabel):

    eventHappened = Signal(str)

    def __init__(self):
        super().__init__()

        self.setText("Начать")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.eventHappened.emit("Pressed")


class Window(QWidget):
    def __init__(self):

        super().__init__()
        self.setAcceptDrops(True)
        self.layout = QVBoxLayout()
        self.setWindowTitle("Click then drag and drop")
        self.setMinimumSize(400, 400)

        self.label = LogLabel()
        self.label.eventHappened.connect(self.addWidget)

        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.position()
        widget = e.source()
        for n in range(self.layout.count()):
            w = self.layout.itemAt(n).widget()
            self.layout.insertWidget(n-1, widget)
            break
        e.accept()

    @Slot(str)
    def addWidget(self):
        self.layout.removeWidget(self.label)
        self.label.deleteLater()
        btn = DragButton("Button")
        self.layout.addWidget(btn)
        btn.setMinimumSize(200, 100)

        btnDown = DragButton("Drag on me")
        self.layout.addWidget(btnDown)
        btnDown.setMinimumSize(200, 100)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
