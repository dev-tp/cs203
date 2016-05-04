#include <iostream>

#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QSpacerItem>
#include <QVBoxLayout>

#include "window.h"

Window::Window(QWidget *parent): QWidget(parent) {
    this->resize(500, 600);
    this->input.setPlaceholderText("UInt8");
    this->input.setMaxLength(4);

    QPushButton *display = new QPushButton("Display", this);
    QHBoxLayout *container = new QHBoxLayout;
    QSpacerItem *spacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);
    container->addSpacerItem(spacer);
    container->addWidget(new QLabel("Enter a number:", this));
    container->addWidget(&this->input);
    container->addWidget(display);
    container->addSpacerItem(spacer);

    QObject::connect(display, SIGNAL(clicked()), this, SLOT(handleEvent()));
    QObject::connect(&this->input, SIGNAL(returnPressed()), this, SLOT(handleEvent()));

    QVBoxLayout *group = new QVBoxLayout;
    group->addWidget(&this->canvas);
    group->addLayout(container);

    QGridLayout *grid = new QGridLayout(this);
    grid->addLayout(group, 0, 0, 1, 1);
}

Window::~Window() {
    delete this;
}

void Window::handleEvent() {
    std::string value = this->input.text().toStdString();
    if(isNumeric(value)) {
        this->canvas.reset();
        this->canvas.drawBranches(std::stoi(value) + 1);
        this->canvas.update();
    }
}

bool Window::isNumeric(std::string str) {
    try {
        std::string::size_type szt;
        std::stod(str, &szt);
    } catch(std::invalid_argument) {
        return false;
    }
    return true;
}