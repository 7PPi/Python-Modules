class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def grow(self) -> None:
        self.height += 6
        self.growth = 6

    def aging(self) -> None:
        self.age += 6

    def get_info(self) -> None:
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
