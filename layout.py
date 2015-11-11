# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\layout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName(_fromUtf8("widget"))
        widget.resize(497, 308)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
        widget.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        widget.setWindowIcon(icon)
        widget.setWindowOpacity(0.95)
        self.url_input = QtGui.QLineEdit(widget)
        self.url_input.setGeometry(QtCore.QRect(20, 20, 381, 41))
        self.url_input.setText(_fromUtf8(""))
        self.url_input.setObjectName(_fromUtf8("url_input"))
        self.btn_crawl = QtGui.QPushButton(widget)
        self.btn_crawl.setGeometry(QtCore.QRect(410, 20, 71, 41))
        self.btn_crawl.setObjectName(_fromUtf8("btn_crawl"))
        self.qas = QtGui.QTextBrowser(widget)
        self.qas.setEnabled(True)
        self.qas.setGeometry(QtCore.QRect(20, 70, 461, 211))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qas.sizePolicy().hasHeightForWidth())
        self.qas.setSizePolicy(sizePolicy)
        self.qas.setObjectName(_fromUtf8("qas"))
        self.label = QtGui.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(410, 290, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        widget.setWindowTitle(_translate("widget", "露天問答爬蟲", None))
        self.url_input.setPlaceholderText(_translate("widget", "請輸入網址", None))
        self.btn_crawl.setText(_translate("widget", "GO", None))
        self.label.setText(_translate("widget", "Created by Aji", None))

