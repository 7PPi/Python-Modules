

def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int,
) -> None:
    try:
        if plant_name is None:
            raise ValueError("Error: Plant name cannot be empty!")

        if int(water_level) < 1:
            raise ValueError(
                f"Error: Water level {water_level} is too low (min 1)"
            )
        elif int(water_level) > 10:
            raise ValueError(
                f"Error: Water level {water_level} is too high (max 10)"
            )

        if int(sunlight_hours) < 2:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        elif int(sunlight_hours) > 12:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
            )

        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(e)


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    check_plant_health("tomato", 5, 5)

    print("\nTesting empty plant name...")
    check_plant_health(None, 5, 5)

    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 5)

    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 1)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
