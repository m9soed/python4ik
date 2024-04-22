from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Расписание ПИЭ-3")

        layout = QGridLayout()

        layout.addWidget(QLabel("ПИЭ-31БО"), 0, 1,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("ПИЭ-32БО"), 0, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(QLabel("Понедельник"), 1, 1, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        for i in range(4):
            layout.addWidget(QLabel(str(i + 1) + ":"), i + 2, 0)
        layout.addWidget(QLabel("Алгоритмы обработки информации"), 2, 2)
        layout.addWidget(QLabel("Алгоритмы обработки информации"), 3, 1)
        layout.addWidget(QLabel("Разработка программных приложений"), 3, 2)
        layout.addWidget(QLabel("Алгоритмы обработки информации"), 4, 1, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("Разработка программных приложений"), 5, 1)

        layout.addWidget(QLabel(""), 6, 1, 1, 2)

        layout.addWidget(QLabel("Вторник"), 7, 1, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        for i in range(2):
            layout.addWidget(QLabel(str(i + 1) + ":"), 6 + i + 2, 0)
        layout.addWidget(QLabel("Предметно-ориентированные ЭИС"), 8, 1, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("Предметно-ориентированные ЭИС"), 9, 1, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(QLabel(""), 10, 1, 1, 2)

        layout.addWidget(QLabel("Среда"), 11, 1, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        for i in range(3):
            layout.addWidget(QLabel(str(i + 1) + ":"), 11 + i + 2, 0)
        layout.addWidget(QLabel(""), 12, 1, 2, 2)
        layout.addWidget(QLabel("Программная инженерия"), 14, 1, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("Программная инженерия"), 15, 1, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(QLabel("ПИЭ-31БО"), 0, 4,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("ПИЭ-32БО"), 0, 5,
                         alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(QLabel("Четверг"), 1, 4, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        for i in range(4):
            layout.addWidget(QLabel(str(i + 1) + ":"), i + 2, 3)
        layout.addWidget(QLabel("Прикладная статистика"), 4, 4)
        layout.addWidget(QLabel("Проектирование информационных систем"), 4, 5)
        layout.addWidget(QLabel("Менеджмент"), 5, 4, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(QLabel(""), 6, 4, 1, 2)

        layout.addWidget(QLabel("Пятница"), 7, 4, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        for i in range(4):
            layout.addWidget(QLabel(str(i + 1) + ":"), 6 + i + 2, 3)
        layout.addWidget(QLabel("Прикладная статистика"), 8, 4, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("Проектирование информационных систем"), 9, 4)
        layout.addWidget(QLabel("Прикладная статистика"), 9, 5)
        layout.addWidget(QLabel("Прикладная физическая культура"), 10, 4, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("Проектирование ифнормационных систем"), 11, 4, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(QLabel(""), 12, 4, 1, 2)

        layout.addWidget(QLabel("Суббота"), 13, 4, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("1:"), 14, 3)
        layout.addWidget(QLabel("Право"), 14, 4, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
