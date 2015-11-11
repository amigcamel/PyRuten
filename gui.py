# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from crawler import crawl
import layout
import sys


class PyRuten(QtGui.QWidget, layout.Ui_widget):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        # set fix size for the widget
        self.setFixedSize(self.width(), self.height())
        self.setup_funcs()

    def setup_funcs(self):
        # buttons
        self.btn_crawl.clicked.connect(self.go)

    def go(self):
        url = self.url_input.text()
        res = crawl(url)
        self.qas.setText('\n'.join(res))


def main():
    app = QtGui.QApplication(sys.argv)
    form = PyRuten()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
