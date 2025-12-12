


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.closed_image = QtWidgets.QLabel(Dialog)
        self.closed_image.setGeometry(QtCore.QRect(0, 0, 391, 291))
        self.closed_image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.closed_image.setText("")
        self.closed_image.setPixmap(QtGui.QPixmap("closed-pokedex.png"))
        self.closed_image.setScaledContents(True)
        self.closed_image.setObjectName("closed_image")
        self.open_button = QtWidgets.QPushButton(Dialog)
        self.open_button.setGeometry(QtCore.QRect(40, 150, 61, 51))
        self.open_button.setCheckable(False)
        self.open_button.setObjectName("open_button")
        self.open_button.clicked.connect(self.open)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.open_button.setText(_translate("Dialog", "open"))
    def open(self):
        self.closed_image.setPixmap(QtGui.QPixmap("pokedex1.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
