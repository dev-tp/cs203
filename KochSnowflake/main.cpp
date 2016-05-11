#include <QApplication>
#include "window.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    Window window;
    window.setWindowTitle("Koch Snowflake");
    window.show();
    return app.exec();
}