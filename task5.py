import os
from typing import List


class MyIterator:
    def __init__(self, class_name: str, dir: str):
        """
        Initializes the iterator by setting the class name,
        a counter from scratch, a list with the names of elements,
        the maximum value equal to the number of elements.
        """
        self.class_name: str = class_name
        self.counter: int = 0
        self.dir: str = dir
        self.path: str = os.path.join(dir, class_name)
        self.data: List[str] = os.listdir(self.path)
        self.limit: int = len(self.data)

    def __next__(self):
        """
        The method returns the next image of the class and increments the counter.
        If the counter reaches the maximum value, an exception is thrown StopIteration.
        """
        if self.counter < self.limit:
            path: str = os.path.join(
                self.path, self.data[self.counter]
            )
            self.counter += 1
            return path
        else:
            raise StopIteration
