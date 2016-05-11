#include <QPainter>

#include "canvas.h"

Canvas::Canvas(QWidget *parent): QWidget(parent) {
    this->setMinimumSize(500, 500);
}

Canvas::~Canvas() {}

void Canvas::paintEvent(QPaintEvent *event) {
    QPainter painter(this);
    for (QLine line : lines)
        painter.drawLine(line);
}

void Canvas::reset() {
    lines.clear();
}

void Canvas::drawBranches(int order, int x, int y, int size) {
    if (order <= 0) return;

    this->drawH(x, y, size);

    int x0 = x - size / 2;
    int x1 = x + size / 2;
    int y0 = y - size / 2;
    int y1 = y + size / 2;

    drawBranches(order - 1, x0, y0, size / 2);
    drawBranches(order - 1, x0, y1, size / 2);
    drawBranches(order - 1, x1, y0, size / 2);
    drawBranches(order - 1, x1, y1, size / 2);
}

void Canvas::drawH(int x, int y, int size) {
    int x0 = x - size / 2;
    int x1 = x + size / 2;
    int y0 = y - size / 2;
    int y1 = y + size / 2;

    lines.push_back(QLine(x0, y0, x0, y1));
    lines.push_back(QLine(x1, y0, x1, y1));
    lines.push_back(QLine(x0, y, x1, y));
}