"""Module documentation."""
from typing import Any
def ft_count_harvest_iterative() -> None:
    """ft_count_harvest_iterative function."""
    days: str = input("Days unitl harvest: ")
    i: int = 1
    while i <= int(days):
        print(f"Day {i}")
        i = 1 + i
    print("Harvest time!")
