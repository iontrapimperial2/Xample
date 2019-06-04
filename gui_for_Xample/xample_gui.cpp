#include "xample_gui.h"
#include "ui_xample_gui.h"

Xample_gui::Xample_gui(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Xample_gui)
{
    ui->setupUi(this);
}

Xample_gui::~Xample_gui()
{
    delete ui;
}
