"""Module documentation."""
from typing import Any
class Plant:
    """Plant class."""
    def __init__(self, name: str, height: float, age: int) -> None:
        """__init__ function."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Flower class."""
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        """__init__ function."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """bloom function."""
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    """Tree class."""
    def __init__(self, name: str, height: float, age: int, t_d: float) -> None:
        """__init__ function."""
        super().__init__(name, height, age)
        self.t_d = t_d

    def produce_shade(self) -> None:
        """produce_shade function."""
        diameter = self.t_d / 100
        radius = diameter / 2
        shade = 3.1416 * (radius ** 2)
        print(f"{self.name} provides {shade :.2f} square meters of shade\n")


class Vegetable(Plant):
    """Vegetable class."""
    def __init__(self, name: Any, height: Any, age: Any,  h_s: str, n_v: str) -> None:
        """__init__ function."""
        super().__init__(name, height, age)
        self.h_s = h_s
        self.n_v = n_v


def main() -> Any:
    """main function."""
    print("=== Garden Plant Types ===\n")
    garden: list = [
        Flower("Rose", 45, 90, "red"),
        Flower("Button pom", 3, 5, "green"),
        Tree("Oak", 120, 550, 20),
        Tree("Willow", 425, 750, 50),
        Vegetable("Tomato", 50, 80, "summer", "rich in vitamin C"),
        Vegetable("Cucumber", 30, 40, "autumn", "rich in potassium"),
    ]

    for plant in garden:
        print(f"{plant.name} ({plant.__class__.__name__}):", end="")
        print(f"{plant.height}cm , {plant.age} days, ", end="")
        match plant:
            case Flower():
                print(f"{plant.color} color")
                plant.bloom()
            case Tree():
                print(f"{plant.t_d}cm diameter")
                plant.produce_shade()
            case Vegetable():
                print(f"{plant.h_s} harvest")
                print(f"{plant.name} is rich in {plant.n_v}\n")


if __name__ == "__main__":
    main()
