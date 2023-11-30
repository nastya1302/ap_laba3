import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon

# from task1 import creating_csvfile, write_path
# from task2 import copy_images as copy
# from task3 import copy_images as copy_random
# from task5 import MyIterator


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("FLOWERS")
        self.setWindowIcon(QIcon("WindowIcon.png"))
        self.show()


def main() -> None:
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
