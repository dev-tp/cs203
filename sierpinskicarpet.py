#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(500, 600)

        self.input_text = QtGui.QLineEdit(self)
        self.input_text.setPlaceholderText("UInt8")
        self.input_text.setMaxLength(4)
        self.input_text.returnPressed.connect(self.handle_event)
        display = QtGui.QPushButton("Display", self)
        display.clicked.connect(self.handle_event)

        container = QtGui.QHBoxLayout()
        container.addSpacerItem(QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        container.addWidget(QtGui.QLabel("Enter an order:", self))
        container.addWidget(self.input_text)
        container.addWidget(display)
        container.addSpacerItem(QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))

        self.canvas = Canvas()
        group = QtGui.QVBoxLayout()
        group.addWidget(self.canvas)
        group.addLayout(container)

        grid = QtGui.QGridLayout(self)
        grid.addLayout(group, 0, 0, 1, 1)

    @QtCore.pyqtSlot()
    def handle_event(self):
        value = self.input_text.text()
        if Window.is_value_numeric(value):
            self.canvas.reset()
            self.canvas.draw_rectangle(int(value))
            self.canvas.update()

    @staticmethod
    def is_value_numeric(value):
        try:
            float(value)
        except ValueError:
            return False
        return True


class Canvas(QtGui.QWidget):
    def __init__(self, angle=0):
        super(Canvas, self).__init__()
        self.setMinimumSize(500, 500)
        self.rectangles = []

    def draw_rectangle(self, order, x=0, y=0, size=500):
        if order <= 0 or order > 6:
            return

        size /= 3
        self.rectangles.append(QtCore.QRect(x + size, y + size, size, size))

        self.draw_rectangle(order - 1, x, y, size)
        self.draw_rectangle(order - 1, x + size, y, size)
        self.draw_rectangle(order - 1, x + size * 2, y, size)
        self.draw_rectangle(order - 1, x, y + size, size)
        self.draw_rectangle(order - 1, x + size * 2, y + size, size)
        self.draw_rectangle(order - 1, x, y + size * 2, size)
        self.draw_rectangle(order - 1, x + size, y + size * 2, size)
        self.draw_rectangle(order - 1, x + size * 2, y + size * 2, size)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for rectangle in self.rectangles:
            painter.fillRect(rectangle, QtGui.QColor(0, 0, 0))
            painter.drawRect(rectangle)

    def reset(self):
        del self.rectangles[:]


def main():
    app = QtGui.QApplication(["something_clever"])
    window = Window()
    window.setWindowTitle("Sierpinski's Carpet")
    window.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()
