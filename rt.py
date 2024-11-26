import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QLineEdit, QPushButton


class Ff(QWidget):
    def __init__(self):
        super().__init__()
        self._count_widget = 4
        self.inirUI()

    def inirUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Прятки для виджетов')

        for i in range(self._count_widget):
            checkbox = f'checkbox{i + 1}'
            edit = f'edit{i + 1}'

            setattr(self, checkbox, QCheckBox(edit, self))
            my_check: QCheckBox = getattr(self, checkbox)
            my_check.setChecked(True)
            my_check.move(5, 10 + 40 * i)
            my_check.clicked.connect(self.hide_edit)

            setattr(self, edit, QLineEdit(f'Поле edit{i}', self))
            my_edit: QLineEdit = getattr(self, edit)
            my_edit.resize(200, 30)
            my_edit.move(150, 5 + 40 * i)

    def hide_edit(self):
        fiel: QCheckBox = self.sender()
        edit: QLineEdit = getattr(self, fiel.text())
        if fiel.isChecked():
            edit.show()
        else:
            edit.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ff()
    ex.show()
    exit(app.exec())
