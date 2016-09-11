#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

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

        grid = QtGui.QGridLayout(self)  # Sets Window's layout to a QGridLayout
        grid.addLayout(group, 0, 0, 1, 1)

    @QtCore.pyqtSlot()
    def handle_event(self):
        value = self.input_text.text()
        if Window.is_value_numeric(value):
            self.canvas.reset()
            self.canvas.draw_curve(int(value) + 1)
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
        self.x, self.y = 0, 0
        self.old_x, self.old_y = 0, 0
        self.angle = angle
        self.lines = []

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for line in self.lines:
            painter.drawLine(line)

    def draw_curve(self, order):
        if order <= 0:
            return

        self._turn_left(90)
        self._joint(order - 1)
        self._go_forward(10)

        self._turn_left(-90)
        self.draw_curve(order - 1)
        self._go_forward(10)
        self.draw_curve(order - 1)

        self._turn_left(-90)
        self._go_forward(10)
        self._joint(order - 1)
        self._turn_left(90)

    def _joint(self, order):
        if order <= 0:
            return

        self._turn_left(-90)
        self.draw_curve(order - 1)
        self._go_forward(10)

        self._turn_left(90)
        self._joint(order - 1)
        self._go_forward(10)
        self._joint(order - 1)

        self._turn_left(90)
        self._go_forward(10)
        self.draw_curve(order - 1)
        self._turn_left(-90)

    def _turn_left(self, delta):
        self.angle += delta

    def _go_forward(self, step):
        self.old_x, self.old_y = self.x, self.y
        self.x += step * math.cos(math.radians(self.angle))
        self.y += step * math.sin(math.radians(self.angle))
        self.lines.append(QtCore.QLine(self.old_x, self.old_y, self.x, self.y))

    def reset(self):
        self.old_x, self.old_y = 0, 0
        self.x, self.y = 0, 0
        del self.lines[:]  # clear list


def main():
    app = QtGui.QApplication(["something_clever"])
    window = Window()
    window.setWindowTitle("Hilbert Curve")
    window.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()
