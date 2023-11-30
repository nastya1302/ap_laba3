import os
from typing import List


class MyIterator:
    def __init__(self, class_name: str):
        """
        Initializes the iterator by setting the class name,
        a counter from scratch, a list with the names of elements,
        the maximum value equal to the number of elements.
        """
        self.class_name: str = class_name
        self.counter: int = 0
        self.data: List[str] = os.listdir(os.path.join("dataset1", class_name))
        self.limit: int = len(self.data)

    def __next__(self):
        """
        The method returns the next image of the class and increments the counter.
        If the counter reaches the maximum value, an exception is thrown StopIteration.
        """
        if self.counter < self.limit:
            path: str = os.path.join(
                "dataset1", self.class_name, self.data[self.counter]
            )
            self.counter += 1
            return path
        else:
            raise StopIteration


def main(name: str):
    """
    The function receives a class label as input, creates a new object,
    and prints the next five elements of this class.
    """
    class_name: MyIterator = MyIterator(name)

    for _ in range(5):
        print(next(class_name))


if __name__ == "__main__":
    main("rose")
