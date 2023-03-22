import errno

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
import socket
import Network.functions

decrypTout = False

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1063, 415)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        Dialog.setFont(font)
        self.scrollArea = QtWidgets.QScrollArea(parent=Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 341, 331))
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pteDialogue = QtWidgets.QPlainTextEdit(parent=self.scrollAreaWidgetContents)
        self.pteDialogue.setGeometry(QtCore.QRect(0, 20, 341, 311))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pteDialogue.setFont(font)
        self.pteDialogue.setReadOnly(True)
        self.pteDialogue.setObjectName("pteDialogue")
        self.lblT = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.lblT.setGeometry(QtCore.QRect(0, 0, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        self.lblT.setFont(font)
        self.lblT.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblT.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.lblT.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lblT.setObjectName("lblT")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btnSend = QtWidgets.QPushButton(parent=Dialog)
        self.btnSend.setGeometry(QtCore.QRect(260, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.btnSend.setFont(font)
        self.btnSend.setObjectName("btnSend")
        self.leSend = QtWidgets.QLineEdit(parent=Dialog)
        self.leSend.setGeometry(QtCore.QRect(20, 350, 321, 21))
        self.leSend.setObjectName("leSend")
        self.cbCrypSend = QtWidgets.QComboBox(parent=Dialog)
        self.cbCrypSend.setGeometry(QtCore.QRect(20, 370, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.cbCrypSend.setFont(font)
        self.cbCrypSend.setEditable(True)
        self.cbCrypSend.setObjectName("cbCrypSend")
        self.cbCrypSend.addItem("")
        self.cbCrypSend.addItem("")
        self.cbCrypSend.addItem("")
        self.cbCrypSend.addItem("")
        self.btnDecrypt = QtWidgets.QPushButton(parent=Dialog)
        self.btnDecrypt.setGeometry(QtCore.QRect(360, 350, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.btnDecrypt.setFont(font)
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.cbEveryDec = QtWidgets.QCheckBox(parent=Dialog)
        self.cbEveryDec.setGeometry(QtCore.QRect(710, 350, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.cbEveryDec.setFont(font)
        self.cbEveryDec.setObjectName("cbEveryDec")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=Dialog)
        self.scrollArea_2.setGeometry(QtCore.QRect(360, 10, 341, 331))
        self.scrollArea_2.setMouseTracking(True)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 339, 329))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.pteChoix = QtWidgets.QPlainTextEdit(parent=self.scrollAreaWidgetContents_2)
        self.pteChoix.setGeometry(QtCore.QRect(0, 20, 341, 311))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pteChoix.setFont(font)
        self.pteChoix.setReadOnly(False)
        self.pteChoix.setObjectName("pteChoix")
        self.lblT_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.lblT_2.setGeometry(QtCore.QRect(0, 0, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        self.lblT_2.setFont(font)
        self.lblT_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblT_2.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.lblT_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lblT_2.setObjectName("lblT_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(parent=Dialog)
        self.scrollArea_3.setGeometry(QtCore.QRect(710, 10, 341, 331))
        self.scrollArea_3.setMouseTracking(True)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 339, 329))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.pteDecrypt = QtWidgets.QPlainTextEdit(parent=self.scrollAreaWidgetContents_3)
        self.pteDecrypt.setGeometry(QtCore.QRect(0, 20, 341, 311))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pteDecrypt.setFont(font)
        self.pteDecrypt.setReadOnly(True)
        self.pteDecrypt.setObjectName("pteDecrypt")
        self.lblT_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        self.lblT_3.setGeometry(QtCore.QRect(0, 0, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        self.lblT_3.setFont(font)
        self.lblT_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblT_3.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.lblT_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lblT_3.setObjectName("lblT_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.timer = QTimer()
        self.timer.timeout.connect(self.TIMERE)
        self.timer.start(250)

        self.retranslateUi(Dialog)
        self.cbCrypSend.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.cbEveryDec.clicked.connect(self.DecryptAll)
        self.btnSend.clicked.connect(self.CLICKEZ)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblT.setText(_translate("Dialog", "Dialogue utilisateur / serveur"))
        self.btnSend.setText(_translate("Dialog", "Envoyer"))
        self.cbCrypSend.setCurrentText(_translate("Dialog", "méthode de cryptage 1"))
        self.cbCrypSend.setItemText(0, _translate("Dialog", "méthode de cryptage 1"))
        self.cbCrypSend.setItemText(1, _translate("Dialog", "méthode de cryptage 2"))
        self.cbCrypSend.setItemText(2, _translate("Dialog", "méthode de cryptage 3"))
        self.cbCrypSend.setItemText(3, _translate("Dialog", "sans cryptage"))
        self.btnDecrypt.setText(_translate("Dialog", "Decrypter"))
        self.cbEveryDec.setText(_translate("Dialog", "Tout tenter de decrypter"))
        self.lblT_2.setText(_translate("Dialog", "Choix messages à décrypter"))
        self.lblT_3.setText(_translate("Dialog", "Messages décryptés"))

    def CLICKEZ(self):
        GROSSEDATA = (self.leSend.text())
        self.pteDialogue.insertPlainText(f"Utilisateur : {GROSSEDATA}\n")
        GROSSEDATA = Network.functions.encode(GROSSEDATA,"t")
        self.leSend.setText("")
        tcp_client.sendall(GROSSEDATA)

    def DecryptAll(self):
        self.btnDecrypt.setEnabled(not self.cbEveryDec.isChecked())
        self.pteChoix.setEnabled((not self.cbEveryDec.isChecked()))
        decrypTout = self.cbEveryDec.isChecked()

    def TIMERE(self):
        try:
            myStack = bytes()
            while True:
                myStack += tcp_client.recv(1024)
                print("Stack contains:")
                print(myStack)

        except Exception as e:
            if e.args[0] == BlockingIOError:
                if len(myStack) != 0:
                    print("msg get")
                    if myStack[3] == ord('t'):
                        print("txt")
                        self.pteDialogue.insertPlainText(f"Serveur: {self.byteToString(myStack)}\n")
                    if myStack[3] == ord('i'):
                        print("img")
                        self.byteToImage(myStack)
            pass

if __name__ == "__main__":
    import sys
    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)
    sys.excepthook = except_hook

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    host_ip, server_port = "vlbelintrocrypto.hevs.ch", 6000
    data = Network.functions.encode("bonjour c'est les gars du fond", 't')

    # Initialize a TCP client socket using SOCK_STREAM
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # try:
    # Establish connection to TCP server and exchange data
    tcp_client.connect((host_ip, server_port))
    tcp_client.setblocking(False)

    sys.exit(app.exec())

