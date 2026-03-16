"""Module documentation."""
from typing import Any
def ft_count_harvest_recursive() -> None:
    """ft_count_harvest_recursive function."""
    days: str = input("Days unitl harvest: ")
    i: int = 1

    def ftrecurvise(i: Any) -> None:
        """ftrecurvise function."""
        if i > int(days):
            print("Harvest time!")
            return
        else:
            print(f"Day {i}")
            return (ftrecurvise(i + 1))
    ftrecurvise(i)
