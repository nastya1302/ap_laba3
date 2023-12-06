import csv
import os
from typing import List


def writing_absolute_path(name: str) -> List[str]:
    """
    The function accepts the name of the class and the name of the directory as input.
    The function gets the absolute path to the specified directory
    and a list of the names of the elements in it. Adds absolute paths
    of elements to the list. Returns a list of paths.
    """
    abs_path: str = os.path.abspath(name)
    list_images: List[str] = os.listdir(abs_path)
    rez_paths: List[str] = []
    for i in list_images:
        rez_paths.append(os.path.join(abs_path, i))
    return rez_paths


def writing_relative_path(name: str, dir: str) -> List[str]:
    """
    The function accepts the name of the class and the name of the directory as input.
    The function gets the relative path to the specified directory
    and a list of the names of the elements in it. Adds relative paths
    of elements to the list. Returns a list of paths.
    """
    rel_path: str = os.path.relpath(name)
    list_images: List[str] = os.listdir(rel_path)
    rez_paths: List[str] = []
    for i in list_images:
        rez_paths.append(os.path.join(dir, rel_path, i))
    return rez_paths


def creating_csvfile(namecsv: str, names: List[str], path: str, save_dir: str):
    """
    The function takes as input the name for the .csv file,
    creates a .csv file with the passed name and writes the column headers.
    The function opens a .csv file and writes absolute and relative paths to the desired columns.
    """
    os.chdir(save_dir)
    with open(namecsv + ".csv", "w", newline="") as f:
        filewriter = csv.writer(f, delimiter=",", lineterminator="\r")
        filewriter.writerow(["Absolute path", "Relative path", "Class name"])
        for name in names:
                os.chdir(path)
                dir: str = os.path.split(path)[1]
                abs_paths: List[str] = writing_absolute_path(name)
                rel_paths: List[str] = writing_relative_path(name, dir)
                for abs_path, rel_path in zip(abs_paths, rel_paths):
                    filewriter.writerow([abs_path, rel_path, name])


def main(path: str, save_dir: str) -> None:
    """
    Calls a function to create .csv file.
    """
    creating_csvfile("Annotasion", ["rose", "tulip"], path, save_dir)


if __name__ == "__main__":
    main("dataset1/")
