# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/railfence.ui'
#
# Created by: PyQt5 UI code generator 5.15.11

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 360, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.txtKey = QtWidgets.QTextEdit(self.centralwidget)
        self.txtKey.setGeometry(QtCore.QRect(250, 220, 551, 41))
        self.txtKey.setObjectName("txtKey")

        self.txtPlaintext = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPlaintext.setGeometry(QtCore.QRect(250, 110, 551, 87))
        self.txtPlaintext.setObjectName("txtPlaintext")

        self.txtCiphertext = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCiphertext.setGeometry(QtCore.QRect(250, 330, 551, 171))
        self.txtCiphertext.setObjectName("txtCiphertext")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 220, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt.setGeometry(QtCore.QRect(650, 540, 93, 41))
        self.btnDecrypt.setObjectName("btnDecrypt")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 110, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.btnEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncrypt.setGeometry(QtCore.QRect(270, 540, 93, 41))
        self.btnEncrypt.setObjectName("btnEncrypt")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 30, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # ✅ Label chứa thông tin sinh viên
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 70, 400, 30))
        font_info = QtGui.QFont()
        font_info.setPointSize(13)
        font_info.setItalic(True)
        self.label_5.setFont(font_info)
        self.label_5.setStyleSheet("color: #004d40;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rail Fence Cipher - HUTECH"))
        self.label_3.setText(_translate("MainWindow", "Cipher Text:"))
        self.label_2.setText(_translate("MainWindow", "Key:"))
        self.btnDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.label.setText(_translate("MainWindow", "Plain Text:"))
        self.btnEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.label_4.setText(_translate("MainWindow", "RAILFENCE CIPHER"))
        self.label_5.setText(_translate("MainWindow", "NGUYỄN THÁI HOÀNG - 2280601053"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
