import sys
import os
from Libs.Get_music import VK_lib
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
 
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(300, 300, 250, 70)
        self.setWindowTitle('Введите ID')    

        self.btn = QPushButton('ОК', self)
        self.btn.resize(50, 20)
        self.btn.move(25, 40)
 
        self.btn.clicked.connect(self.input_ID)

        self.label = QLabel(self)
        self.label.resize(125, 20)
        self.label.move(100, 40)

        self.name_input = QLineEdit(self)
        self.name_input.resize(200, 20)
        self.name_input.move(25, 10)

    def User_name(self):
        self.label.setText(VK_lib.get_name(int(self.name_input.text())))

    def input_ID(self):
        self.label.setText('')
        if self.name_input.text().isdigit():
            self.User_name()
            if os.name == 'nt':
                os.system('python run.py {}'.format(self.name_input.text()))
            else:
                os.system('python3 run.py {}'.format(self.name_input.text()))

        else:
            self.label.setText("Некорректный ввод")

 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())  