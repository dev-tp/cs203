#ifndef WINDOW_H
#define WINDOW_H

#include <QLineEdit>
#include <QWidget>

#include "canvas.h"

class Window: public QWidget {
    Q_OBJECT
    QLineEdit input;
    Canvas canvas;

    bool isNumeric(std::string);

public:
    explicit Window(QWidget *parent=0);
    ~Window();

public slots:
    void handleEvent();
};

#endif