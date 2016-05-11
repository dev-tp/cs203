#include <cmath>

#include <QPainter>

#include "canvas.h"

Canvas::Canvas(QWidget *parent): QWidget(parent) {
    this->setMinimumSize(500, 500);
}

Canvas::~Canvas() {}

void Canvas::reset() {
    lines.clear();
}

void Canvas::drawSnowflake(int n, int x0, int y0, int x1, int y1) {
    if (n == 0) {
        lines.push_back(QLine(x0, y0, x1, y1));
    } else {
        int dx = x1 - x0;
        int dy = y1 - y0;

        int x2 = x0 + dx / 3;
        int y2 = y0 + dy / 3;
        int x3 = 0.5 * (x0 + x1) + sqrt(3) * (y0 - y1) / 6;
        int y3 = 0.5 * (y0 + y1) + sqrt(3) * (x1 - x0) / 6;
        int x4 = x0 + 2 * dx / 3;
        int y4 = y0 + 2 * dy / 3;

        drawSnowflake(n-1, x0, y0, x2, y2);
        drawSnowflake(n-1, x2, y2, x3, y3);
        drawSnowflake(n-1, x3, y3, x4, y4);
        drawSnowflake(n-1, x4, y4, x1, y1);
    }
}

void Canvas::drawTriangle(int iterations) {
    drawSnowflake(iterations, 20, 280, 280, 280);
    drawSnowflake(iterations, 280, 280, 150, 20);
    drawSnowflake(iterations, 150, 20, 20, 280);
}

void Canvas::paintEvent(QPaintEvent *event) {
    QPainter painter(this);
    for (QLine line : this->lines)
        painter.drawLine(line);
}