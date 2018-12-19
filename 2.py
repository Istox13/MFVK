import Libs.player as player
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p = True
        self.pl = False
        uic.loadUi('main.ui',self)
        self.play_music.clicked.connect(self.pause)
 
    def pause(self):
        if not self.pl:
            self.pl = True
            player.Player.play_music(player.Player, "C://Users/Istox13/Downloads/1.mp3")
        if self.p:
            player.Player.pause(player.Player)
        else:
            player.Player.unpause(player.Player)
        self.p = not self.p

 
 
def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_()) 
    player.Player()


main()
