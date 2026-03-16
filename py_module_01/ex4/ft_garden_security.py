class SecurePlant:
    def __init__(self, name: str) -> None:
        self._name = name
        self._age = 0
        self._height = 0
        print("Plant created: ", name)

    def set_height(self, height: float) -> None:
        if height < 0 or height > 12000:
            print("\nInvalid operation attempted: ", end="")
            print(f"height {height:.0f}cm [REJECTED]")
            if height < 0:
                print("Security: Negative height, rejected")
            else:
                print("Security: Plant too tall, rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height:.0f}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0 or age > 1826250:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            if age < 0:
                print("Security: Negative age ,rejected")
            else:
                print("Security: Plant too old, rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def get_info(self) -> None:
        print("\nCurrent plant: ", end="")
        print(f"{self._name} ({self._height}cm, {self._age} days old)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(25)
    plant.set_height(-5)
    plant.get_info()
