# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 522)
        MainWindow.setMinimumSize(QtCore.QSize(752, 522))
        MainWindow.setMaximumSize(QtCore.QSize(752, 522))
        font = QtGui.QFont()
        font.setKerning(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.playlist = QtWidgets.QListWidget(self.centralwidget)
        self.playlist.setGeometry(QtCore.QRect(420, 0, 331, 501))
        self.playlist.setMinimumSize(QtCore.QSize(331, 501))
        self.playlist.setMaximumSize(QtCore.QSize(331, 501))
        self.playlist.setObjectName("playlist")
        self.play_pause = QtWidgets.QPushButton(self.centralwidget)
        self.play_pause.setGeometry(QtCore.QRect(110, 440, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.play_pause.setFont(font)
        self.play_pause.setObjectName("play_pause")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(200, 460, 75, 23))
        self.next.setObjectName("next")
        self.unnext = QtWidgets.QPushButton(self.centralwidget)
        self.unnext.setGeometry(QtCore.QRect(30, 460, 75, 23))
        self.unnext.setObjectName("unnext")
        self.volume_up = QtWidgets.QPushButton(self.centralwidget)
        self.volume_up.setGeometry(QtCore.QRect(300, 450, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.volume_up.setFont(font)
        self.volume_up.setObjectName("volume_up")
        self.volume_down = QtWidgets.QPushButton(self.centralwidget)
        self.volume_down.setGeometry(QtCore.QRect(380, 450, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.volume_down.setFont(font)
        self.volume_down.setObjectName("volume_down")
        self.volume_print = QtWidgets.QLabel(self.centralwidget)
        self.volume_print.setGeometry(QtCore.QRect(330, 450, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.volume_print.setFont(font)
        self.volume_print.setAutoFillBackground(False)
        self.volume_print.setObjectName("volume_print")
        self.name_song = QtWidgets.QLabel(self.centralwidget)
        self.name_song.setGeometry(QtCore.QRect(20, 410, 381, 20))
        self.name_song.setAcceptDrops(False)
        self.name_song.setText("")
        self.name_song.setObjectName("name_song")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Player for VK"))
        self.play_pause.setText(_translate("MainWindow", "|>"))
        self.next.setText(_translate("MainWindow", ">>"))
        self.unnext.setText(_translate("MainWindow", "<<"))
        self.volume_up.setText(_translate("MainWindow", "↑"))
        self.volume_down.setText(_translate("MainWindow", "↓"))
        self.volume_print.setText(_translate("MainWindow", "50%"))

