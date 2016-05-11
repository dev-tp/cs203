#ifndef CANVAS_H
#define CANVAS_H

#include <vector>

#include <QLine>
#include <QPaintEvent>
#include <QWidget>

class Canvas: public QWidget {
    Q_OBJECT
    std::vector<QLine> lines;

    void drawSnowflake(int, int, int, int, int);

public:
    explicit Canvas(QWidget *parent=0);
    ~Canvas();

    void drawTriangle(int);
    void reset();

protected:
    void paintEvent(QPaintEvent*);
};

#endif