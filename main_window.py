import sys
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QFileDialog,
    QPushButton,
    QLabel,
    QGridLayout,
    QDialog,
    QVBoxLayout
)
from PyQt5.QtGui import QIcon, QPixmap
from typing import List
import os

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

        self.setWindowTitle("FLOWERS")
        self.setStyleSheet("background: rgb(220, 208, 255); font: 10pt Comic Sans MS")
        self.setWindowIcon(QIcon("WindowIcon.png"))

    def getDataset(self) -> None:
        """
        Asking the user for the path to the source dataset.
        """
        self.dirlist: str = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.iter()

    def iter(self) -> None:
        self.rose_iterator: MyIterator = MyIterator("rose", self.dirlist)
        self.tulip_iterator: MyIterator = MyIterator("tulip", self.dirlist)

    def create_csv(self) -> None:
        """
        Creating csv file for the source dataset.
        """
        paths: List[str] = self.select_foldef()
        task1.main(paths[0], paths[1])
        self.message("The annotation have been created.")

    def copy(self) -> None:
        """
        Copies dataset 1 to dataset 2 with new names and creates a csv file.
        """
        paths: List[str] = self.select_foldef()
        task2.main(paths[0], paths[1])
        self.message("The dataset and annotation have been created.")

    def copy_random(self) -> None:
        """
        Copies dataset 1 to dataset 3 with random names and creates a csv file.    
        """
        paths: List[str] = self.select_foldef()
        task3.main(paths[0], paths[1])
        self.message("The dataset and annotation have been created.")

    def next_rose(self) -> None:
        """
        By placing the following class image in the window.
        """
        rose_path: str = next(self.rose_iterator)
        if rose_path != None:
            image = QPixmap(rose_path)
            image_rez = image.scaledToWidth(500)
            self.label.setPixmap(image_rez)
        else:
            self.message("The images of this class have ended.")
            self.iter()
            self.next_rose()


    def next_tulip(self) -> None:
        """
        By placing the following class image in the window.
        """
        tulip_path: str = next(self.tulip_iterator)
        if tulip_path != None:
            image = QPixmap(tulip_path)
            image_rez = image.scaledToWidth(500)
            self.label.setPixmap(image_rez)
        else:
            self.message("The images of this class have ended.")
            self.iter()
            self.next_tulip()

    def message(self, text: str) -> None:
        dlg = QDialog(self)
        dlg.setWindowTitle("FLOWERS")
        text = QLabel(text, dlg)
        btn = QPushButton('ok', dlg)
        vbox = QVBoxLayout(dlg)
        vbox.addStretch(1)
        vbox.addWidget(text)
        vbox.addWidget(btn)
        btn.clicked.connect(dlg.close)
        dlg.exec()

    def select_foldef(self) -> List[str]:
        paths: List[str] = []
        dirlist: str = QFileDialog.getExistingDirectory(self, "Select Folder")
        save_dir: str = QFileDialog.getExistingDirectory(self, "Select Folder For Save")
        paths.append(dirlist)
        paths.append(save_dir)
        return paths


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
