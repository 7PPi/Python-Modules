"""Module documentation."""
from typing import Any
class GardenError(Exception):
    """GardenError class."""
    pass


class PlantError(GardenError):
    """PlantError class."""
    pass


class WaterError(GardenError):
    """WaterError class."""
    pass


def check_errors() -> None:
    """check_errors function."""
    print("=== Custom Garden Errors Demo ==")
    try:
        temp = 50
        water = 0
        try:
            print("\nTesting PlantError...")
            if temp > 36:
                raise PlantError(
                    "Caught PlantError: The tomato plant is wilting!"
                )
        except PlantError as e:
            print(e)

        try:
            print("\nTesting WaterError...")
            if water < 1:
                raise WaterError(
                    "Caught WaterError: Not enough water in the tank!"
                )
        except WaterError as e:
            print(e)

        try:
            print("\nTesting catching all garden errors...")
            if temp > 36 and water < 1:
                raise GardenError(
                    "Caught a garden error: The tomato plant is wilting!\n"
                    "Caught a garden error: Not enough water in the tank!"
                )
        except GardenError as e:
            print(e)
    except ValueError as e:
        print(f"{e}")

    print("\nAll custom error types work correctly")


if __name__ == "__main__":
    check_errors()
