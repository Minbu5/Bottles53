import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QFont, QPixmap  # for Icons, fonts, images
from PyQt5.QtCore import Qt  # alignment


# new class inherits from QMainWindow, in which all customizations will take place
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # window settings
        self.setWindowTitle("Two Bottles")
        self.setGeometry(600, 300, 900, 700)
        intro_message = QLabel('''
                         This is puzzle program.
                         - You have two bottles with capacities 5 liters and 3 liters.
                         - Both vessels don't have markings except for full capacities (5 l. and 3 l.) respectively.
                         - You can fill bottles with water, spill out or transfer from one to another unlimited times.
                         - The goal is to get 4 liters in 5 l. bottle ''', self)

        intro_message.setStyleSheet("background-color: grey;")
        intro_message.setGeometry(80, 0, 750, 150)
        intro_message.setAlignment(Qt.AlignLeft)
        intro_message.setFont(QFont("Times New Roman", 13))


        # Bottels
        ########################################################

        # vessel 5 l
        vessel5 = QLabel(self)
        vessel5.setGeometry(170, 160, 230, 270)
        pixmap = QPixmap("assets/bottle5_0.png")
        vessel5.setPixmap(pixmap)
        vessel5.setScaledContents(True)

        # vessel 5 l menu buttons
        button_fill_5 = QPushButton("Fill 5L", self)
        button_fill_5.setGeometry(170, 450, 230, 50)
        button_fill_5.clicked.connect(self.fill_5) # send signal

        button_spill_5 = QPushButton("Spill 5L", self)
        button_spill_5.setGeometry(170, 510, 230, 50)
        button_spill_5.clicked.connect(self.spill_5)

        button_transfer_5 = QPushButton("Transfer from 5L", self)
        button_transfer_5.setGeometry(170, 570, 230, 50)
        button_transfer_5.clicked.connect(self.transfer_5)

        # vessel 3 l
        vessel3 = QLabel(self)
        vessel3.setGeometry(500, 210, 190, 220)
        pixmap = QPixmap("assets/bottle3_0.png")
        vessel3.setPixmap(pixmap)
        vessel3.setScaledContents(True)

        # vessel 3 l menu buttons
        button_fill_3 = QPushButton("Fill 3L", self)
        button_fill_3.setGeometry(500, 450, 190, 50)
        button_fill_3.clicked.connect(self.fill_3) # send signal

        button_spill_3 = QPushButton("Spill 3L", self)
        button_spill_3.setGeometry(500, 510, 190, 50)
        button_spill_3.clicked.connect(self.spill_3)

        button_transfer_3 = QPushButton("Transfer from 3L", self)
        button_transfer_3.setGeometry(500, 570, 190, 50)
        button_transfer_3.clicked.connect(self.transfer_3)

    # Button functions
    ########################################################

        # 5 liters
    def fill_5(self):
        print("filled 5l")
    def spill_5(self):
        print("Spilled 5l")
    def transfer_5(self):
        print("Transfered from 5l")

    # 3 liters
    def fill_3(self):
        print("filled 3l")
    def spill_3(self):
        print("Spilled 3l")
    def transfer_3(self):
        print("Transfered from 3l")


def main():
    app = QApplication(sys.argv)  # allows command line arguments instead could be ([]) passed
    window = MainWindow()
    window.show()  # to display window
    sys.exit(app.exec_())  # to hold window


main()

# if  __name__ == "__main__":
#     main()
