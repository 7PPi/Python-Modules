"""Module documentation."""
from typing import Any
class Plant:
    """Plant class."""
    def __init__(self, name: str, height: float, age: int) -> None:
        """__init__ function."""
        self.name = name
        self.height = height
        self.age = age

    def pplant(self) -> None:
        """pplant function."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    count: int = 0
    plants: list = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunfower", 80, 45),
        Plant("Fern", 15, 120),
        ]
    for plant in plants:
        plant.pplant()
        count += 1

    print(f"\n Total plants created: {count}")
