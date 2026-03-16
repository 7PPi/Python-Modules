"""Module documentation."""
from typing import Any
class Plant:
    """Plant class."""
    def __init__(self, name: str, height: float, age: int) -> None:
        """__init__ function."""
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def grow(self) -> None:
        """grow function."""
        self.height += 6
        self.growth = 6

    def aging(self) -> None:
        """aging function."""
        self.age += 6

    def get_info(self) -> None:
        """get_info function."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        if self.growth != 0:
            print(f"Growth this week: +{self.growth}cm")


if __name__ == "__main__":
    flower = Plant('Rose', 25, 30)
    print("=== Day 1 ===")
    flower.get_info()
    for i in range(1, 2):
        flower.aging()
        flower.grow()
        print(f"=== Day {i * 7} ===")
        flower.get_info()
