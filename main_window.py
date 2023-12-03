import sys
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QFileDialog,
    QPushButton,
    QLabel,
    QGridLayout
)
from PyQt5.QtGui import QIcon, QPixmap

import task1
import task2
import task3
from task5 import MyIterator


class Example(QWidget):
    
    def __init__(self) -> None:
        """
        Constructor for creating a window.
        """
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        """
        Placement of buttons in the application.
        """
        self.button1 = QPushButton("Select dataset", self)
        self.button1.setStyleSheet("background: rgb(200, 208, 255)")
        self.button1.setFixedSize(500, 60)
        self.button1.clicked.connect(self.getDataset)

        self.button2 = QPushButton("Create annotasion for source dataset", self)
        self.button2.setStyleSheet("background: rgb(200, 208, 255)")
        self.button2.setFixedSize(500, 60)
        self.button2.clicked.connect(self.create_csv)

        self.button3 = QPushButton("Create new dataset and annotasion", self)
        self.button3.setStyleSheet("background: rgb(200, 208, 255)")
        self.button3.setFixedSize(500, 60)
        self.button3.clicked.connect(self.copy)

        self.button4 = QPushButton("Create new random dataset and annotasion", self)
        self.button4.setStyleSheet("background: rgb(200, 208, 255)")
        self.button4.setFixedSize(500, 60)
        self.button4.clicked.connect(self.copy_random)

        self.rose_iterator: MyIterator = MyIterator("rose", "dataset1")
        self.tulip_iterator: MyIterator = MyIterator("tulip", "dataset1")

        self.button5 = QPushButton("Next rose", self)
        self.button5.setStyleSheet("background: rgb(200, 208, 255)")
        self.button5.setFixedSize(500, 60)
        self.button5.clicked.connect(self.next_rose)

        self.button6 = QPushButton("Next tulip", self)
        self.button6.setStyleSheet("background: rgb(200, 208, 255)")
        self.button6.setFixedSize(500, 60)
        self.button6.clicked.connect(self.next_tulip)

        self.label = QLabel(self)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.button1, 0, 0)
        grid.addWidget(self.button2, 1, 0)
        grid.addWidget(self.button3, 2, 0)
        grid.addWidget(self.button4, 3, 0)
        grid.addWidget(self.button5, 4, 1)
        grid.addWidget(self.button6, 5, 1)
        grid.addWidget(self.label, 0, 1, 4, 1)

        self.setLayout(grid)
        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle("FLOWERS")
        self.setStyleSheet("background: rgb(220, 208, 255); font: 10pt Comic Sans MS")
        self.setWindowIcon(QIcon("WindowIcon.png"))

    def getDataset(self) -> None:
        """
        Asking the user for the path to the source dataset.
        """
        self.dirlist: str = QFileDialog.getExistingDirectory(self, "Select Folder")

    def create_csv(self) -> None:
        """
        Creating csv file for the source dataset.
        """
        task1.main(self.dirlist)

    def copy(self) -> None:
        """
        Copies dataset 1 to dataset 2 with new names and creates a csv file.
        """
        task2.main(self.dirlist)

    def copy_random(self) -> None:
        """
        Copies dataset 1 to dataset 3 with random names and creates a csv file.    
        """
        task3.main(self.dirlist)

    def next_rose(self) -> None:
        """
        By placing the following class image in the window.
        """
        self.rose_path: str = next(self.rose_iterator)
        image = QPixmap(self.rose_path)
        image_rez = image.scaledToWidth(500)
        self.label.setPixmap(image_rez)

    def next_tulip(self) -> None:
        """
        By placing the following class image in the window.
        """
        self.tulip_path: str = next(self.tulip_iterator)
        image = QPixmap(self.tulip_path)
        image_rez = image.scaledToWidth(500)
        self.label.setPixmap(image_rez)
        

def main() -> None:
    """
    An application object is being created.
    """
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
