
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton,QTextEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
#from UI.button import *
import sys
"""""
Classe fenêtre : affichage du chat
"""""

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.setWindowTitle("Internet_Secured_Chat")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = QTextEdit()
        layout.addWidget(self.input)

        button = QPushButton("Print Text")
        button.clicked.connect(self.display)
        layout.addWidget(button)

    def display(self):
        print(self.input.toPlainText())

    def update(self):
        self.label.setText("New and Updated Text")

    def get(self):
        print(self.label.text())

        # layout = QVBoxLayout()
        # self.setLayout(layout)

        # label = QLabel("Hello World")
        # label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # layout.addWidget(label)



