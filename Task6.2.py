from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import QStringListModel

class Product:
    def __init__(self, name, quantity, weight):
        self.name = name
        self.quantity = quantity
        self.weight = weight

    def get_total_weight(self):
        return self.quantity * self.weight


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Product List')
        self.products = []
        self.total_weight = 0

        # Создание основной виджет и макет
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        # Создание виджет формы и макет
        self.form_widget = QWidget()
        self.form_layout = QVBoxLayout()
        self.form_widget.setLayout(self.form_layout)

        # Создание полей формы
        self.name_field = QLineEdit()
        self.quantity_field = QLineEdit()
        self.weight_field = QLineEdit()

        # Добавление поля формы в макет формы
        self.form_layout.addWidget(QLabel('Name:'))
        self.form_layout.addWidget(self.name_field)
        self.form_layout.addWidget(QLabel('Quantity:'))
        self.form_layout.addWidget(self.quantity_field)
        self.form_layout.addWidget(QLabel('Weight (kg):'))
        self.form_layout.addWidget(self.weight_field)

        # Кнопка "Создать форму"
        self.add_button = QPushButton('Add Product')
        self.add_button.clicked.connect(self.add_product)

        # Добавление кнопку формы в макет формы
        self.form_layout.addWidget(self.add_button)

        # Добавление виджет формы в основной макет
        self.main_layout.addWidget(self.form_widget)

        # Создание виджет и макет списка продуктов
        self.list_widget = QWidget()
        self.list_layout = QVBoxLayout()
        self.list_widget.setLayout(self.list_layout)

        # Добавление виджет списка товаров в основной макет
        self.main_layout.addWidget(self.list_widget)

        # Создание первоначальный список продуктов
        self.add_product('Яблоко', 10, 0.2)
        self.add_product('Банан', 5, 0.15)

    def add_product(self, name=None, quantity=None, weight=None):
        if name is None:
            name = self.name_field.text()
        if quantity is None:
            quantity = int(self.quantity_field.text())
        if weight is None:
            weight = float(self.weight_field.text())

        product = Product(name, quantity, weight)
        self.products.append(product)

        # Обновить общий вес
        self.total_weight += product.get_total_weight()

        # Добавить товар в список товаров
        self.list_layout.addWidget(QLabel(f'{product.name}: {product.quantity} x {product.weight} kg'))

        # Обновить метку общего веса
        self.update_total_weight_label()

        # Очистить поля формы
        self.name_field.clear()
        self.quantity_field.clear()
        self.weight_field.clear()

    def update_total_weight_label(self):
        if hasattr(self, 'total_weight_label'):
            self.total_weight_label.setText(f'Общий вес: {self.total_weight:.2f} kg')
        else:
            self.total_weight_label = QLabel(f'Общий вес: {self.total_weight:.2f} kg')
            self.main_layout.addWidget(self.total_weight_label)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

