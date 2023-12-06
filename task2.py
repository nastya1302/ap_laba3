import os
import shutil
import csv
from typing import List


def copy_images(old_dir: str, names: List[str], save_dir: str) -> None:
    """
    The function takes as input the name for the .csv file,
    creates a .csv file with the passed name and writes the column headers.
    The function copies one image from the old directory to the new one,
    changing the name, and immediately writes its absolute, relative paths and class name to the .csv file.
    """
    os.chdir(save_dir)
    new_dir: str = "dataset2"
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    abs_path: str = os.path.abspath(new_dir)
    rel_path: str = os.path.relpath(new_dir)
    with open("Annotasion2" + ".csv", "w", newline="") as f:
        filewriter = csv.writer(f, delimiter=",", lineterminator="\r")
        filewriter.writerow(["Absolute path", "Relative path", "Class name"])
        for name in names:
            path: str = os.path.join(old_dir, name)
            list_images: List[str] = os.listdir(path)
            for img in list_images:
                shutil.copy(os.path.join(path, img), os.path.join(new_dir, f"{name}_{img}"))
                filewriter.writerow(
                    [
                        os.path.join(abs_path, f"{name}_{img}"),
                        os.path.join(rel_path, f"{name}_{img}"),
                        name,
                    ]
                )


def main(path: str, save_dir: str) -> None:
    """
    The main() function is fed a list of class names, the names of
    the old and new directories. A new .csv file is created for the
    new data. A directory with a new name is created, into which images
    from the old directory with the changed name will be copied and their
    new absolute and relative paths will be written to the .csv file at the same time.
    """
    copy_images(path, ["rose", "tulip"], save_dir)


if __name__ == "__main__":
    main("dataset1/")
