"""Module documentation."""
from typing import Any
def check_temperature(temp_str: int) -> None:
    """check_temperature function."""
    try:
        temp = int(temp_str)
        if (temp > 0 and temp < 40):
            print(f"Temperature {temp}°C is perfect for plants!")
        elif (temp < 0):
            print(f"TError: {temp}°C is too cold for plants (min 0°C)")
        elif (temp > 40):
            print(f"Error: {temp}C is too hot for plants (max 40°C)")
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")


def test_temperature_input() -> None:
    """test_temperature_input function."""
    print("=== Garden Temperature Checker ===")

    temp = 25
    print(f"\nTesting temperature: {temp}")
    check_temperature(temp)

    temp = "abc"
    print(f"\nTesting temperature: {temp}")
    check_temperature(temp)

    temp = 100
    print(f"\nTesting temperature: {temp}")
    check_temperature(temp)

    temp = -50
    print(f"\nTesting temperature: {temp}")
    check_temperature(temp)

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
