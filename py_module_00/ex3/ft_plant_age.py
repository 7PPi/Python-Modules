"""Module documentation."""
from typing import Any
def ft_plant_age() -> None:
    """ft_plant_age function."""
    age: str = input("Enter plant age in days: ")
    if int(age) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
