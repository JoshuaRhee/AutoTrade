from kiwoom.kiwoom import *
import sys
from PyQt5.QtWidgets import *

class Main():
    def __init__(self):
        print("Main() start")

        self.use_money_percent = 0.5

        self.app = QApplication(sys.argv)
        self.kiwoom = Kiwoom()
        self.app.exec_() # 이벤트 루프 실행

if __name__ == "__main__":
    Main()