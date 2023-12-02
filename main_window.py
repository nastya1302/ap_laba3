import sys
import os
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QFileDialog,
    QPushButton,
    QMessageBox,
    QGridLayout,
)
from PyQt5.QtGui import QIcon

import task1 
# from task2 import copy_images as copy
# from task3 import copy_images as copy_random
# from task5 import MyIterator


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setStyleSheet("background: rgb(220, 208, 255); font: 10pt Comic Sans MS")

    def initUI(self):

        self.button1 = QPushButton("Select dataset", self)
        self.button1.setStyleSheet("background: rgb(200, 208, 255)")
        self.button1.clicked.connect(self.getDataset)

        self.button2 = QPushButton("Create annotasion for source dataset", self)
        self.button2.setStyleSheet("background: rgb(200, 208, 255)")
        self.button2.clicked.connect(self.create_csv)

        self.button3 = QPushButton("Create new dataset and annotasion", self)
        self.button3.setStyleSheet("background: rgb(200, 208, 255)")

        self.button4 = QPushButton("Create new random dataset and annotasion", self)
        self.button4.setStyleSheet("background: rgb(200, 208, 255)")

        self.button5 = QPushButton("Next rose", self)
        self.button5.setStyleSheet("background: rgb(200, 208, 255)")

        self.button6 = QPushButton("Next tulip", self)
        self.button6.setStyleSheet("background: rgb(200, 208, 255)")

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.button1, 1, 0)
        grid.addWidget(self.button2, 2, 0)
        grid.addWidget(self.button3, 3, 0)
        grid.addWidget(self.button4, 4, 0)
        grid.addWidget(self.button5, 5, 0)
        grid.addWidget(self.button6, 6, 0)

        self.setLayout(grid)
        self.setGeometry(300, 300, 700, 300)
        self.setWindowTitle("FLOWERS")
        self.setWindowIcon(QIcon("WindowIcon.png"))
        self.show()

    def getDataset(self):
        self.dirlist = QFileDialog.getExistingDirectory(self, 'Select Folder')

    def create_csv(self):
        task1.main(self.dirlist)

    def close_event(self, event):
        reply = QMessageBox.question(
            self,
            "Message",
            "Are you sure to quit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main() -> None:
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
