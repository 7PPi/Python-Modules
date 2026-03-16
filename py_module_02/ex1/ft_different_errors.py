def garden_operations() -> None:
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    try:
        print("\nTesting ZeroDivisionError...")
        4 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)

    try:
        print("\nTesting FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError:"
              " No such file: 'missing.txt'")

    try:
        print("\nTesting KeyError...")
        plant = {"plant": "rose"}
        print(plant["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")

    try:
        print("\nTesting multiple errors together...")
        int("abc")
        10 / 0
    except (
        ValueError,
        ZeroDivisionError,
        FileNotFoundError,
        KeyError,
    ):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
