#ifndef XAMPLE_GUI_H
#define XAMPLE_GUI_H

#include <QMainWindow>

namespace Ui {
class Xample_gui;
}

class Xample_gui : public QMainWindow
{
    Q_OBJECT

public:
    explicit Xample_gui(QWidget *parent = 0);
    ~Xample_gui();

private:
    Ui::Xample_gui *ui;
};

#endif // XAMPLE_GUI_H
