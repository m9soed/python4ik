import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, \
    QListWidgetItem, QMessageBox, QLabel, QListView
from PySide6.QtCore import QStringListModel


class NoteItem(QWidget):
    def __init__(self, note_id, text, parent=None):
        super().__init__(parent)
        self.note_id = note_id
        self.text_label = QLabel(text)
        self.id_label = QLabel(str(note_id))
        layout = QHBoxLayout()
        layout.addWidget(self.id_label)
        layout.addWidget(self.text_label)

        self.setLayout(layout)


class NotesApp(QWidget):
    def __init__(self):
        super().__init__()

        self.data = []
        self.count = 0

        # Создаем главный вертикальный лэйаут
        main_layout = QVBoxLayout()

        # Создаем лэйаут для поля ввода и кнопки
        input_layout = QHBoxLayout()

        # Создаем поле для ввода текста новой заметки
        self.new_note_input = QLineEdit()

        # Создаем кнопку для добавления заметки в список
        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_note)

        # Добавляем поле ввода и кнопку в лэйаут для них
        input_layout.addWidget(self.new_note_input)
        input_layout.addWidget(add_button)

        # Создаем список заметок
        self.notes_list = QListView()
        self.notes_list.clicked.connect(self.delete_note)

        # Добавляем поле ввода, кнопку и список заметок в главный лэйаут
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.notes_list)

        # Устанавливаем главный лэйаут для виджета
        self.setLayout(main_layout)


    def add_note(self):
        new_note_text = self.new_note_input.text()
        if new_note_text.strip() != '':
            self.count += 1
            new_note_text = str(self.count) + ' ' + new_note_text
            self.data.append(new_note_text)
            self.notes_list.setModel(QStringListModel(self.data))
            self.new_note_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Вы не ввели данные")

    def delete_note(self, item):
        self.data.remove(self.data[item.row()])
        self.notes_list.setModel(QStringListModel(self.data))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    notes_app = NotesApp()
    notes_app.show()
    sys.exit(app.exec())