import os
import shutil
import csv
import random
from typing import List


def copy_images(old_dir: str, names: List[str], save_dir: str) -> None:
    """
    The function takes as input the name for the .csv file,
    creates a .csv file with the passed name and writes the column headers.
    The function copies one image from the old directory to the new one,
    changing the name, and immediately writes its absolute, relative paths and class name to the .csv file.
    """
    os.chdir(save_dir)
    new_dir: str = "dataset3"
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    abs_path: str = os.path.abspath(new_dir)
    rel_path: str = os.path.relpath(new_dir)
    random_number: List[str] = random.sample((range(0, 10000)), 2000)
    count: int = 0
    with open("Annotasion3" + ".csv", "w", newline="") as f:
        filewriter = csv.writer(f, delimiter=",", lineterminator="\r")
        filewriter.writerow(["Absolute path", "Relative path", "Class name"])    
        for name in names:
            path: str = os.path.join(os.path.abspath(old_dir), name)
            list_images: List[str] = os.listdir(path)
            for img in list_images:
                new_name: str = f"{random_number[count]}".zfill(5)
                shutil.copy(
                    os.path.join(path, img), os.path.join(new_dir, f"{new_name}.jpg")
                )
                filewriter.writerow(
                    [
                        os.path.join(abs_path, f"{new_name}.jpg"),
                        os.path.join(rel_path, f"{new_name}.jpg"),
                        name,
                    ]
                )
                count += 1


def main(path: str, save_dir: str) -> None:
    """
    The main() function is fed a list of class names, the names of
    the old and new directories. A new .csv file is created for the
    new data. A directory with a new name is created, into which images
    from the old directory with the changed name will be copied and their
    new absolute and relative paths will be written to the .csv file at the same time.
    """
    path_dir = os.path.split(path)
    os.chdir(path_dir[0])
    copy_images(path_dir[1], ["rose", "tulip"], save_dir)


if __name__ == "__main__":
    main("dataset1/")
