from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtWidgets
from sys import argv, exit
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(280, 250, 201, 51))
        self.generate_button.setObjectName("generate_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Жёлтые окружности"))
        self.generate_button.setText(_translate("MainWindow", "Сгенерировать"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.circles = []

    def initUi(self):
        self.setupUi(self)
        self.generate_button.clicked.connect(self.generate_circles)

    def generate_circles(self):
        self.circles = []
        for _ in range(3):
            size = randint(20, 200)
            x1, y1 = randint(0, 780 - size), randint(0, 580 - size)
            self.circles.append((x1, y1, size, size))
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for circle in self.circles:
            qp.setBrush(
                QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.drawEllipse(*circle)
        qp.end()


if __name__ == "__main__":
    app = QApplication(argv)
    main_window = MainWindow()
    main_window.show()
    exit(app.exec())
