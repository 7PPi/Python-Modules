"""Module documentation."""
from typing import Any
class Plant:
    """Plant class."""
    def __init__(self, name: str, height: float) -> None:
        """__init__ function."""
        self.name = name
        self.height = height

    def grow(self) -> None:
        """grow function."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def report(self) -> None:
        """report function."""
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """FloweringPlant class."""
    def __init__(self, name: str, height: float, color: str) -> None:
        """__init__ function."""
        super().__init__(name, height)
        self.bloom = False
        self.color = color

    def report(self) -> None:
        """report function."""
        print(f"- {self.name}: ", end="")
        print(f"{self.height}cm, {self.color} flowers (blooming)")
        self.bloom = True


class PrizeFlower(FloweringPlant):
    """PrizeFlower class."""
    def __init__(self, name: Any, height: float, color: str, prize: int) -> None:
        """__init__ function."""
        super().__init__(name, height, color)
        self.prize = prize

    def report(self) -> None:
        """report function."""
        print(f"- {self.name}: ", end="")
        print(f"{self.height}cm, {self.color} flowers (blooming)", end="")
        print(f", Prize points: {self.prize} ")
        self.bloom = True


class Garden:
    """Garden class."""
    count: int = 0

    def __init__(self, owner: str) -> None:
        """__init__ function."""
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.plants_added: int = 0
        self.growth: int = 0
        Garden.count += 1

    def add_plants(self, plants: list[Plant], report: bool = True) -> None:
        """add_plants function."""
        for plant in plants:
            self.plants.append(plant)
            self.plants_added += 1
            if report:
                print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        """grow_all function."""
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.growth += 1

    def score(self) -> int:
        """score function."""
        score = 0
        for plant in self.plants:
            score += plant.height
            if plant.__class__ == PrizeFlower:
                score += plant.prize
            if plant.__class__ == PrizeFlower and plant.bloom:
                score += 15
            if plant.__class__ == FloweringPlant and plant.bloom:
                score += 15
        return score


class GardenManager:
    """GardenManager class."""

    class GardenStats:
        """GardenStats class."""
        def __init__(self, regular: int, flowering: int, prize: int) -> None:
            """__init__ function."""
            self.regular = regular
            self.flowering = flowering
            self.prize = prize

    def __init__(self) -> None:
        """__init__ function."""
        self.gardens: dict[str, Garden] = {}

    def add_garden(self, garden: Garden) -> None:
        """add_garden function."""
        self.gardens[garden.owner] = garden

    def grow(self, owner: str) -> None:
        """grow function."""
        print(f"\n{owner} is helping all plants grow..")
        self.gardens[owner].grow_all()

    @classmethod
    def create_garden_network(cls, gardens: list[Garden]) -> Any:
        """create_garden_network function."""
        manager = cls()
        for garden in gardens:
            manager.add_garden(garden)
        return manager

    @staticmethod
    def get_stats(garden: Garden) -> GardenStats:
        """get_stats function."""
        stats = GardenManager.GardenStats(0, 0, 0)
        for plant in garden.plants:
            match plant:
                case PrizeFlower():
                    stats.prize += 1
                case FloweringPlant():
                    stats.flowering += 1
                case Plant():
                    stats.regular += 1
        return stats

    def print_stats(self, owner: str) -> None:
        """print_stats function."""
        print(f"\n=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.gardens[owner].plants:
            plant.report()
        print(f"\nPlants added: {self.gardens[owner].plants_added},", end="")
        print(f" Total growth: {self.gardens[owner].growth}cm")
        stats = GardenManager.get_stats(self.gardens[owner])
        print(f"Plant types: {stats.regular} regular,", end="")
        print(f" {stats.flowering} flowering, {stats.prize} prize flowers")

    def print_total(self) -> None:
        """print_total function."""
        validate: bool = True
        for owner, garden in self.gardens.items():
            for plant in garden.plants:
                if plant.height < 0:
                    validate = False
        print(f"\nHeight validation test: {validate}")
        print("Garden scores - ", end="")
        score_items: list[str] = []
        for owner, garden in self.gardens.items():
            score_items.append(f"{owner}: {garden.score()}")
        print(", ".join(score_items))
        print(f"Total gardens managed: {Garden.count}")


def main() -> None:
    """Demonstrate garden creation, growth, and reporting across managers."""

    print("=== Garden Management System Demo ===\n")
    alice = Garden("Alice")
    alice.add_plants(
        [
            Plant("Oak Tree", 100),
            FloweringPlant("Rose", 25, "red"),
            PrizeFlower("Sunflower", 50, "yellow", 10),
        ]
    )
    alice.grow_all()
    manager = GardenManager.create_garden_network([alice])
    manager.print_stats("Alice")
    manager.add_garden(Garden("Bob"))
    manager.gardens["Bob"].add_plants(
        [
            Plant("Magnolia", 60),
            Plant("Caxinde", 32)
        ],
        False,
    )
    manager.print_total()


if __name__ == "__main__":
    main()
