"""Module documentation."""
from typing import Any
class Plant:
    """Plant class."""
    def __init__(self, name: str, height: float, age: int) -> None:
        """__init__ function."""
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        """show function."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)

    p1.show()
    p2.show()
    p3.show()
