import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QPushButton)
from PyQt5.QtGui import QFont, QPixmap  # for Icons, fonts, images
from PyQt5.QtCore import Qt  # alignment

import bottles
from bottles import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # window settings
        self.setWindowTitle("Two Bottles")
        self.setGeometry(600, 300, 900, 700)
        self.initUI()

    # User interface settings
    def initUI(self):
        self.intro_message = QLabel("This is puzzle program.\n"
                                    "You have two bottles with capacities 5 liters and 3 liters.\n"
                                    "Both vessels don't have markings except for full capacities (5 l. and 3 l.) respectively.\n"
                                    "You can fill bottles with water, spill out or transfer from one to another unlimited times.\n"
                                    "The goal is to get 4 liters in 5 l. bottle", self)








        self.intro_message.setStyleSheet(''' QLabel{border: 3px solid;
                                             border-color: #C5BAFF;
                                             border-radius: 15px;
                                             background-color: #C4D9FF;
                                             font-family: Times new Roman;
                                             padding-top: 0;

                                             }''')

        self.intro_message.setGeometry(80, 0, 750, 170)
        self.intro_message.setAlignment(Qt.AlignCenter)

        # set size of font relative to screen
        screen_height = QApplication.primaryScreen().availableGeometry().height()
        message_font_size = int(screen_height * 0.015)  # 1,5 % of screen height, adjust as needed depending on device
        self.intro_message.setFont(QFont("Times New Roman", message_font_size))

        # self.intro_message.setFont(QFont("Times New Roman", 13))

        # Bottles
        ########################################################

        # vessel 5 l
        self.vessel5 = QLabel(self)
        self.vessel5.setGeometry(170, 180, 230, 270)
        self.capacity5 = bottle_5["content"]
        self.pixmap = QPixmap(f"assets/5/5_{self.capacity5}.png")
        self.vessel5.setPixmap(self.pixmap)
        self.vessel5.setScaledContents(True)
        button_font_size = int(screen_height * 0.013)

        # vessel 5 l menu buttons
        self.button_fill_5 = QPushButton("Fill 5L", self)
        self.button_fill_5.setGeometry(170, 470, 230, 50)
        self.button_fill_5.clicked.connect(self.fill_5)  # send signal
        self.button_fill_5.setFont(QFont("Times New Roman", button_font_size))

        self.button_spill_5 = QPushButton("Spill 5L", self)
        self.button_spill_5.setGeometry(170, 530, 230, 50)
        self.button_spill_5.clicked.connect(self.spill_5)
        self.button_spill_5.setFont(QFont("Times New Roman", button_font_size))

        self.button_transfer_5 = QPushButton("Transfer from 5L", self)
        self.button_transfer_5.setGeometry(170, 590, 230, 50)
        self.button_transfer_5.clicked.connect(self.transfer_5)
        self.button_transfer_5.setFont(QFont("Times New Roman", button_font_size))

        # vessel 3 l
        self.vessel3 = QLabel(self)
        self.vessel3.setGeometry(500, 210, 190, 220)
        self.capacity3 = bottle_3["content"]
        self.pixmap = QPixmap(f"assets/3/3_{self.capacity3}.png")
        self.vessel3.setPixmap(self.pixmap)
        self.vessel3.setScaledContents(True)

        # vessel 3 l menu buttons
        self.button_fill_3 = QPushButton("Fill 3L", self)
        self.button_fill_3.setGeometry(500, 470, 190, 50)
        self.button_fill_3.clicked.connect(self.fill_3)  # send signal
        self.button_fill_3.setFont(QFont("Times New Roman", button_font_size))


        self.button_spill_3 = QPushButton("Spill 3L", self)
        self.button_spill_3.setGeometry(500, 530, 190, 50)
        self.button_spill_3.clicked.connect(self.spill_3)
        self.button_spill_3.setFont(QFont("Times New Roman", button_font_size))

        self.button_transfer_3 = QPushButton("Transfer from 3L", self)
        self.button_transfer_3.setGeometry(500, 590, 190, 50)
        self.button_transfer_3.clicked.connect(self.transfer_3)
        self.button_transfer_3.setFont(QFont("Times New Roman", button_font_size))

    # Button style
    ########################################################


        self.setStyleSheet('''   
                    QPushButton{
                        border: 3px solid;
                        border-color: #C5BAFF;
                        border-radius: 15px;
                        background-color: #C4D9FF;
    
                    } 
                    QPushButton:hover{
                        background-color: #E8F9FF;
                    }''')
    

    # Button functions
    ########################################################

    # 5 liters
    def fill_5(self):
        bottles.fill(bottle_5)
        self.capacity5 = bottle_5["content"]
        self.pixmap = QPixmap(f"assets/5/5_{self.capacity5}.png")
        self.vessel5.setPixmap(self.pixmap)
        self.check_4l()

    def spill_5(self):
        bottles.spill(bottle_5)
        self.capacity5 = bottle_5["content"]
        self.pixmap = QPixmap(f"assets/5/5_{self.capacity5}.png")
        self.vessel5.setPixmap(self.pixmap)
        self.check_4l()


    def transfer_5(self):
        bottles.transfer(bottle_5, bottle_3)
        self.capacity5 = bottle_5["content"]
        self.capacity3 = bottle_3["content"]
        self.pixmap = QPixmap(f"assets/5/5_{self.capacity5}.png")
        self.vessel5.setPixmap(self.pixmap)
        self.pixmap = QPixmap(f"assets/3/3_{self.capacity3}.png")
        self.vessel3.setPixmap(self.pixmap)
        self.check_4l()


    # 3 liters
    def fill_3(self):
        bottles.fill(bottle_3)
        self.capacity3 = bottle_3["content"]
        self.pixmap = QPixmap(f"assets/3/3_{self.capacity3}.png")
        self.vessel3.setPixmap(self.pixmap)
        self.check_4l()

    def spill_3(self):
        bottles.spill(bottle_3)
        self.capacity3 = bottle_3["content"]
        self.pixmap = QPixmap(f"assets/3/3_{self.capacity3}.png")
        self.vessel3.setPixmap(self.pixmap)
        self.check_4l()


    def transfer_3(self):
        bottles.transfer(bottle_3, bottle_5)
        self.capacity5 = bottle_5["content"]
        self.capacity3 = bottle_3["content"]
        self.pixmap = QPixmap(f"assets/5/5_{self.capacity5}.png")
        self.vessel5.setPixmap(self.pixmap)
        self.pixmap = QPixmap(f"assets/3/3_{self.capacity3}.png")
        self.vessel3.setPixmap(self.pixmap)
        self.check_4l()

    def check_4l(self):
        if self.capacity5 == 4:
            self.intro_message.setText('⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐\n'
                                       'Congatulations, You are master of watter and logic !!!\n'
                                       '⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  '





            )


def main():
    app = QApplication(sys.argv)  # allows command line arguments instead could be ([]) passed
    window = MainWindow()
    window.show()  # to display window
    sys.exit(app.exec_())  # to hold window


main()

# if  __name__ == "__main__":
#     main()
