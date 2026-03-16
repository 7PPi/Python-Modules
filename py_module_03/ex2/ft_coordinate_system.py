import sys
import math


def ft_coordinate_system() -> None:
    coords: tuple = ()
    x: int = 0
    y: int = 0
    z: int = 0
    distance: int = 0
    length = 0
    print("=== Game Coordinate System ===\n")
    try:
        if len(sys.argv) == 2:
            inputs = sys.argv[1].split(',')
            length = len(inputs) + 1
            if length == 4:
                x = inputs[0]
                y = inputs[1]
                z = inputs[2]
        else:
            length = len(sys.argv)
            if length == 4:
                x = sys.argv[1]
                y = sys.argv[2]
                z = sys.argv[3]

        if length < 4:
            raise AttributeError("Oops you didnt insert enough data!!")
        elif length > 4:
            raise AttributeError("Oops you inserted too much data!!")
        else:
            coords = (x, y, z)
            print(f"Position created: {coords}")
            print("Parsing coordinates: ", end="")
            print(f'"{x}, {y}, {z}"')
            coords = (int(x), int(y), int(z))
            x, y, z = coords
            print(f"Parsed position: {coords}")
            distance = math.sqrt((x)**2 + (y)**2 + (z)**2)
            print(f"Distance between (0, 0, 0) and {coords}: {distance:.2f}")
            print("\nUnpacking demonstration:")
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except ValueError as e:
        print(f"\nError parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args: ("{e})')
    except AttributeError as e:
        print(e)


if __name__ == "__main__":
    ft_coordinate_system()
