import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication, QPushButton, QLineEdit)
from PyQt5.QtGui import QPixmap
from interface import Ui_MainWindow
from Libs.player import Player
from Libs.Get_music import VK_lib
from Libs.Download_music import download

 
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
        self.USER_ID = int(sys.argv[1])
        self.play_pause.clicked.connect(self.play_pause_m)
        self.unnext.clicked.connect(self.unnext_m)
        self.next.clicked.connect(self.next_m)
        self.volume_up.clicked.connect(self.volume_up_m)
        self.volume_down.clicked.connect(self.volume_down_m)
        self.set_image()
        self.Player = Player()
        self.pause = False
        self.play = False
        self.index = '-1'
        self.volume = 50
        
        self.playlist_VK = VK_lib.get_dict(self.USER_ID)
        self.count = len(self.playlist_VK.keys()) - 1
        for k, l in self.playlist_VK.items():
            self.playlist.addItem('{}. {} - {}'.format(k, l['artist'], l['name']))
        self.playlist.itemClicked.connect(self.play_music)

    def set_image(self, path='Images/image1.jpg'):
        pixmap = QPixmap(path)
  
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        self.label.move(30, 10)


    
    def volume_up_m(self):
        if self.volume < 100:
            self.volume += 10
            self.Player.set_volume(self.volume / 100)
            self.volume_print.setText(str(self.volume) + '%')
    
    def volume_down_m(self):
        if self.volume > 0:
            self.volume -= 10 
            self.Player.set_volume(self.volume / 100)
            self.volume_print.setText(str(self.volume) + '%')

    def play_pause_m(self):
        if not self.play:
            self.next_m()
            self.play = True
            self.pause = not self.pause
            self.play_pause.setText('||')

        if self.pause:
            self.Player.unpause()
            self.play_pause.setText('||')
        else:
            self.Player.pause()
            self.play_pause.setText('|>')
        self.pause = not self.pause
    
    def play_music(self, name):
        index, name = name.text().split(maxsplit=1)
        self.name_song.setText(name)
        self.index = index[:-1]
        url = self.playlist_VK[index[:-1]]['url']
        name = download(url, name)
        self.Player.play_music(name)
        self.play_pause.setText('||')
        

    def unnext_m(self):
        if int(self.index) <= 0:
            self.index = str(self.count)
        else: 
            self.index = str(int(self.index) - 1)

        l = self.playlist_VK[self.index]
        url = l['url']
        name = '{} - {}'.format(l['artist'], l['name'])
        self.name_song.setText(name)
        name = download(url, name)
        self.Player.play_music(name)
             

    def next_m(self):
        if int(self.index) < self.count:
            self.index = str(int(self.index) + 1)
        else:
            self.index = '0'

        l = self.playlist_VK[self.index]
        url = l['url']
        name = '{} - {}'.format(l['artist'], l['name'])
        self.name_song.setText(name)
        name = download(url, name)
        self.Player.play_music(name)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())  
