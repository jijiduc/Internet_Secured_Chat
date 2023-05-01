import errno

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer, QMetaObject
from PyQt6.QtGui import QTextCursor

import re
import socket
import Network.functions
import Cryptology.encryption
import Cryptology.decryption
from UI.NOUVOTRUCS import NOUVOBOUTHON,NOUVOPLEINTEXTEDITION, NOUVOPLEINRSAEDITION


class Ui_MainWindow(object):
    indexDialogObjects = 0 #nombre d'elements actuels dans les deux dictionnaires qui suivent
    dictButtons = {} #dictionnaire contenant les boutons de dialogue (chaque message est representé avec un bouton)

    def setupUi(self, MainWindow): #setup de l'interface graphique je commente pas ca c'est mort
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 545)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ScrDialog = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.ScrDialog.setGeometry(QtCore.QRect(10, 10, 351, 481))
        self.ScrDialog.setWidgetResizable(True)
        self.ScrDialog.setObjectName("ScrDialog")
        self.ScrDialog.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(1, 1, 349, 80))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 351, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 420)
        self.ScrDialog.setWidget(self.scrollAreaWidgetContents)
        #self.verticalLayout.setStretch(100,100)

        self.BtnEncrypt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BtnEncrypt.setGeometry(QtCore.QRect(380, 360, 191, 31))
        self.BtnEncrypt.setObjectName("BtnEncrypt")

        self.BtnDecrypt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BtnDecrypt.setGeometry(QtCore.QRect(580, 360, 191, 31))
        self.BtnDecrypt.setObjectName("BtnDecrypt")
        self.BtnDecrypt.clicked.connect(self.DESCRYPTES)

        self.TabWidParamEncrypt = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.TabWidParamEncrypt.setGeometry(QtCore.QRect(370, 140, 411, 111))
        self.TabWidParamEncrypt.setObjectName("TabWidParamEncrypt")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.LblSansMethode = QtWidgets.QLabel(parent=self.tab_4)
        self.LblSansMethode.setGeometry(QtCore.QRect(10, 20, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LblSansMethode.setFont(font)
        self.LblSansMethode.setObjectName("LblSansMethode")

        self.TabWidParamEncrypt.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.PteCleCesar = QtWidgets.QPlainTextEdit(parent=self.tab)
        self.PteCleCesar.setGeometry(QtCore.QRect(160, 20, 231, 41))
        self.PteCleCesar.setObjectName("PteCleCesar")

        self.LblCleCesar = QtWidgets.QLabel(parent=self.tab)
        self.LblCleCesar.setGeometry(QtCore.QRect(10, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LblCleCesar.setFont(font)
        self.LblCleCesar.setObjectName("LblCleCesar")
        self.TabWidParamEncrypt.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.PteCleVegener = QtWidgets.QPlainTextEdit(parent=self.tab_2)
        self.PteCleVegener.setGeometry(QtCore.QRect(90, 20, 301, 41))
        self.PteCleVegener.setObjectName("PteCleVegener")

        self.LblCleVegener = QtWidgets.QLabel(parent=self.tab_2)
        self.LblCleVegener.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LblCleVegener.setFont(font)
        self.LblCleVegener.setObjectName("LblCleVegener")
        self.TabWidParamEncrypt.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.PteCleRSA = NOUVOPLEINRSAEDITION(parent=self.tab_3)
        self.PteCleRSA.setGeometry(QtCore.QRect(270, 20, 121, 41))
        self.PteCleRSA.setObjectName("PteCleRSA")
        self.LblCleRSA = QtWidgets.QLabel(parent=self.tab_3)
        self.LblCleRSA.setGeometry(QtCore.QRect(10, 30, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LblCleRSA.setFont(font)
        self.LblCleRSA.setObjectName("LblCleRSA")
        self.TabWidParamEncrypt.addTab(self.tab_3, "")

        self.PteDecrypted = NOUVOPLEINTEXTEDITION(parent=self.centralwidget)
        self.PteDecrypted.setGeometry(QtCore.QRect(370, 400, 411, 91))
        self.PteDecrypted.setObjectName("PteDecrypted")

        self.TeSend = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.TeSend.setGeometry(QtCore.QRect(370, 10, 411, 71))
        self.TeSend.setObjectName("TeSend")

        self.BtnSend = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BtnSend.setGeometry(QtCore.QRect(660, 90, 111, 31))
        self.BtnSend.setObjectName("BtnSend")
        self.BtnSend.clicked.connect(self.CLICKEZ)

        self.CbxType = QtWidgets.QComboBox(parent=self.centralwidget)
        self.CbxType.setGeometry(QtCore.QRect(550, 90, 101, 31))
        self.CbxType.setObjectName("CbxType")
        self.CbxType.addItem("")
        self.CbxType.addItem("")
        self.CbxType.addItem("")

        self.PteEncrypted = NOUVOPLEINTEXTEDITION(parent=self.centralwidget)
        self.PteEncrypted.setGeometry(QtCore.QRect(370, 260, 411, 91))
        self.PteEncrypted.setObjectName("PteEncrypted")

        self.BtnDepotImage = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BtnDepotImage.setGeometry(QtCore.QRect(380, 90, 161, 31))
        self.BtnDepotImage.setObjectName("BtnDepotImage")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timer = QTimer()
        self.timer.timeout.connect(self.TIMERE)
        self.timer.start(250)

        self.retranslateUi(MainWindow)
        self.TabWidParamEncrypt.setCurrentIndex(0)
        self.CbxType.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow): #pas sur d'avoir pigé pourquoi il a separé ca du setup
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BtnEncrypt.setText(_translate("MainWindow", "Encryptage ⬆"))
        self.BtnDecrypt.setText(_translate("MainWindow", "Decryptage ⬇"))
        self.LblSansMethode.setText(_translate("MainWindow", "Les messages seront envoyés tel quel."))
        self.TabWidParamEncrypt.setTabText(self.TabWidParamEncrypt.indexOf(self.tab_4), _translate("MainWindow", "Sans methode"))
        self.LblCleCesar.setText(_translate("MainWindow", "Clé (nombre entier):"))
        self.TabWidParamEncrypt.setTabText(self.TabWidParamEncrypt.indexOf(self.tab), _translate("MainWindow", "CEASAR"))
        self.LblCleVegener.setText(_translate("MainWindow", "Clé (mot):"))
        self.TabWidParamEncrypt.setTabText(self.TabWidParamEncrypt.indexOf(self.tab_2), _translate("MainWindow", "Vegener"))
        self.TabWidParamEncrypt.setTabText(self.TabWidParamEncrypt.indexOf(self.tab_3), _translate("MainWindow", "RSA"))
        self.LblCleRSA.setText(_translate("MainWindow", "Nombres (modulo, clé) ou [#keySet]:"))
        self.BtnSend.setText(_translate("MainWindow", "Envoyer"))

        self.CbxType.setCurrentText(_translate("MainWindow", "Texte"))
        self.CbxType.setItemText(0, _translate("MainWindow", "Texte"))
        self.CbxType.setItemText(1, _translate("MainWindow", "Serveur"))
        self.CbxType.setItemText(2, _translate("MainWindow", "Image"))
        self.BtnDepotImage.setText(_translate("MainWindow", "Ajouter une image..."))


    def DESCRYPTES(self):
        message = self.PteEncrypted.messageInt
        messageDeco = []
        match self.TabWidParamEncrypt.currentIndex():
            case 1:
                if self.PteCleCesar.toPlainText() == "":
                    messageDeco = Cryptology.decryption.cryptanalysis_cesar(message)
                else:
                    messageDeco = Cryptology.decryption.cesar_decode(message, int(self.PteCleCesar.toPlainText()))
            case 2:
                if self.PteCleVegener.toPlainText() == "":
                    messageDeco = ... #fonction de cryptanalyse vegener
                else:
                    messageDeco = Cryptology.decryption.vigenere_decode(message, self.PteCleVegener.toPlainText())
            case 3:
                if re.compile("\[ *[0-9]+\ *]").match(self.PteCleRSA.toPlainText()):
                    cler = int(self.PteCleRSA.toPlainText().strip("[] "))
                    if cler <= (len(self.PteCleRSA.keySets) - 1):
                        keySet = self.PteCleRSA.keySets[cler]
                        messageDeco = Cryptology.decryption.RSADecrypt(message, keySet[1], keySet[0])
                    else:
                        print("Set de clés inexistant")

                elif re.compile("[0-9]+\, *[0-9]+").match(self.PteCleRSA.toPlainText()):
                    cler = int(self.PteCleRSA.toPlainText().split(","))
                    messageDeco = Cryptology.decryption.RSADecrypt(message, cler[0], cler[1])

                else:
                    print("Format de clé invalide")
        self.PteDecrypted.clear()
        self.PteDecrypted.insertPlainText(Network.functions.int_array_to_string(messageDeco))


    def ENCRYPTE(self):
        message = Network.functions.string_to_int_array(self.PteDecrypted.toPlainText())
        messageEnco = []
        match self.TabWidParamEncrypt.currentIndex():
            case 1:
                messageEnco = Cryptology.encryption.caesar(message, int(self.PteCleCesar.toPlainText()))
            case 2:
                messageEnco = Cryptology.encryption.vigenere(message, self.PteCleVegener.toPlainText())
            case 3:
                print("nieh")

        self.PteDecrypted.messageInt = messageEnco
        self.PteDecrypted.clear()
        self.PteDecrypted.insertPlainText(Network.functions.int_array_to_string(messageEnco))

    def AddDialogObject(self, typeuh, valeurInt, contenu, prov = 'U'): #fonction pour rajouter un bouton au dialogue
        if typeuh == 's' or typeuh == 't':
            def CLICKERCOMPLIQUE(slelf):
                message = label.messageInByte
                self.PteEncrypted.messageInt = message
                self.PteEncrypted.clear()
                self.PteEncrypted.insertPlainText(Network.functions.int_array_to_string(message))


            #cree et met en forme un bouton
            label = NOUVOBOUTHON(parent=self.verticalLayoutWidget)
            label.setGeometry(QtCore.QRect(660, 90, 111, 31))
            label.setObjectName(f"dialogButton{self.indexDialogObjects}")
            label.setText(f"{contenu}")
            label.setMinimumHeight(30)
            label.clicked.connect(CLICKERCOMPLIQUE)
            label.messageInByte = valeurInt
            #le rajoute dans le layout pour qu'il soit affiché dans la zone de gauche du GUI
            self.verticalLayout.addWidget(label)
            #augmente la taille du layout a chaque rajout pour des questions d'alignement
            if self.verticalLayout.getContentsMargins()[3] != 0:
                self.verticalLayout.setContentsMargins(0,0,0,self.verticalLayout.getContentsMargins()[3] - 30)


    def CLICKEZ(self): #si le bouton d'envoi principal est enclenche
        GROSSEDATA = self.TeSend.toPlainText()
        type = self.CbxType.currentText()[0].lower()
        encroptga = ""
        cler = ""
        #cree un bouton de dialogue en fonction de l'index actuel du QTab et modifie GROSSEDATA en fonction du crypt. demandé
        match self.TabWidParamEncrypt.currentIndex():
            case 0:
                encroptga = "Pas de cryptage"
                self.AddDialogObject(type, 0, f"Utilisateur: {GROSSEDATA} ({encroptga})")
                GROSSEDATA = Network.functions.string_to_int_array(GROSSEDATA)
            case 1:
                encroptga = "Clé de César"
                cler = int(self.PteCleCesar.toPlainText())
                self.AddDialogObject(type, 0, f"Utilisateur: {GROSSEDATA} ({encroptga} : {cler})")
                GROSSEDATA = Network.functions.string_to_int_array(GROSSEDATA)
                GROSSEDATA = Cryptology.encryption.caesar(GROSSEDATA, cler)
            case 2:
                encroptga = "Vegener"
                cler = self.PteCleVegener.toPlainText()
                self.AddDialogObject(type, 0, f"Utilisateur: {GROSSEDATA} ({encroptga} : {cler})")
                GROSSEDATA = Network.functions.string_to_int_array(GROSSEDATA)
                GROSSEDATA = Cryptology.encryption.vigenere(GROSSEDATA, cler)
            case 3:
                encroptga = "RSA"
                GROSSEDATA = Network.functions.string_to_int_array(GROSSEDATA)
                if re.compile("\[ *[0-9]+\ *]").match(self.PteCleRSA.toPlainText()):
                    cler = int(self.PteCleRSA.toPlainText().strip("[] "))
                    if cler <= (len(self.PteCleRSA.keySets) - 1):
                        keySet = self.PteCleRSA.keySets[cler]
                        GROSSEDATA = Cryptology.decryption.RSADecrypt(GROSSEDATA, keySet[1], keySet[0])

                elif re.compile("[0-9]+\, *[0-9]+").match(self.PteCleRSA.toPlainText()):
                    cler = int(self.PteCleRSA.toPlainText().split(","))
                    GROSSEDATA = Cryptology.decryption.RSADecrypt(GROSSEDATA, cler[0], cler[1])

                elif self.PteCleRSA.toPlainText() == "":
                    self.PteCleRSA.keySets.append(Cryptology.encryption.newRSAKey())
                    print(
                        f"ELLES POSSEDENT LE NUMERO #{(len(self.PteCleRSA.keySets) - 1)}, FAUT METTRE \"[CE NUMERO]\" POUR LE REUTILISER.")
                    keySet = self.PteCleRSA.keySets[(len(self.PteCleRSA.keySets) - 1)]
                    GROSSEDATA = Cryptology.decryption.RSADecrypt(GROSSEDATA, keySet[1], keySet[0])

                else:
                    print("Format de clé invalide")

        #encode le message en bytes pour le transport et l'envoie
        GROSSEDATA = Network.functions.int_array_to_string(GROSSEDATA)
        GROSSEDATA = Network.functions.encode(GROSSEDATA, type)
        tcp_client.sendall(GROSSEDATA)
        #enleve le texte dans la zone d'entrée de texte de l'utilisateur
        self.TeSend.setText("")

    def TIMERE(self):  # fonction du QTimer que j'ai piquée a Guillaume et Loic
        try:  # en gros je crois il attend ici et il ecoute jusqu'a ce qu'il y ait une erreur volontaire
            myStack = bytes()
            while True:
                myStack += tcp_client.recv(1024)
                print("Stack contains:")
                print(myStack)

        except Exception as e:  # la il detecte l'erreur volontaire qui apparait quand y a plus rien a ecouter
            if len(myStack) != 0:
                print("msg get")
                if myStack[3] == ord('t'):  # pis la il vide le stack et il en fait un bouton de dialogue
                    decodInt = Network.functions.decode_to_int(myStack)
                    decodStr = Network.functions.int_array_to_string(decodInt)
                    self.AddDialogObject('t', decodInt, f"Serveur: {decodStr}", 'S')
                    print(f"Serveur: {Network.functions.int_array_to_string(Network.functions.decode_to_int(myStack))}\n")

                if myStack[3] == ord('s'):  # pis la il vide le stack et il en fait un bouton de dialogue
                    decodInt = Network.functions.decode_to_int(myStack)
                    decodStr = Network.functions.int_array_to_string(decodInt)
                    self.AddDialogObject('s', decodInt, f"Serveur: {decodStr}", 'S')
                    print(
                        f"Serveur: {Network.functions.int_array_to_string(Network.functions.decode_to_int(myStack))}\n")

                #if myStack[3] == ord('i'):  # la meme mais y a une image dans le bouton
                    #print("img")
                    #self.byteToImage(myStack)
            pass


if __name__ == "__main__":
    #ca c'est un truc que le prof a donné pour avoir du feedback pour les erreurs
    import sys
    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)
    sys.excepthook = except_hook

    #creation de la page GUI
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #connexion au srerv
    host_ip, server_port = "vlbelintrocrypto.hevs.ch", 6000
    data = Network.functions.encode("bonjour c'est les gars du fond", 't')

    # Initialize a TCP client socket using SOCK_STREAM
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # try:
    # Establish connection to TCP server and exchange data
    tcp_client.connect((host_ip, server_port))
    tcp_client.setblocking(False)

    sys.exit(app.exec())