import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLCDNumber, QLineEdit


class Exe(QWidget):
    def __init__(self):
        super().__init__()
        self.inirUI()

    def inirUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('6 program')

        self.first_value = QLineEdit(self)
        self.first_value.resize(90, 30)
        self.first_value.move(20, 30)

        self.second_value = QLineEdit(self)
        self.second_value.resize(90, 30)
        self.second_value.move(20, 90)

        self.b = QPushButton(self)
        self.b.resize(30, 90)
        self.b.move(120, 30)
        self.b.clicked.connect(self.habr)

        self.win1 = QLCDNumber(self)
        self.win1.move(160, 30)

        self.win2 = QLCDNumber(self)
        self.win2.move(160, 60)

        self.win3 = QLCDNumber(self)
        self.win3.move(160, 90)

        self.win4 = QLCDNumber(self)
        self.win4.move(160, 120)

        self.res = 0

    def habr(self):
        n1 = int(self.first_value.text())
        n2 = int(self.second_value.text())

        self.res = n1 + n2
        self.win1.display(self.res)

        self.res = n1 - n2
        self.win2.display(self.res)

        self.res = n1 / n2
        self.win3.display(self.res)

        self.res = n1 * n2
        self.win4.display(self.res)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exe()
    ex.show()
    exit(app.exec())
