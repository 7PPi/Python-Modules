"""Module documentation."""
from typing import Any
def water_plants(plant_list: list) -> None:
    """water_plants function."""
    print("Opening watering system")
    success = True
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("None")
            print(f"Watering {plant}")

    except ValueError as e:
        print(f"Error: Cannot water {e} - invalid plant")
        success = False
    finally:
        print("Closing watering system (cleanup)")
    if success:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    """test_watering_system function."""
    print("=== Garden Watering System ===")
    plant = ["tomato", "lettuce", "carrot"]
    print("\nTesting normal watering...")
    water_plants(plant)

    print("\nTesting with errors...")
    plant = ["tomato", None]
    water_plants(plant)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
