"""Module documentation."""
from typing import Any
def ft_plot_area() -> None:
    """ft_plot_area function."""
    length: str = input("Enter length: ")
    width: str = input("Enter width: ")
    area: int = int(length) * int(width)
    print("Plot area: ", area)
