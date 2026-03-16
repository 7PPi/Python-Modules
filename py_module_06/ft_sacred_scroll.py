import alchemy
from alchemy import elements

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===")

    print("\nTesting direct module access:")
    print("alchemy.elements.create_fire():", elements.create_fire())
    print("alchemy.elements.create_water():", elements.create_water())
    print("alchemy.elements.create_earth():", elements.create_earth())
    print("alchemy.elements.create_air():", elements.create_air())

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print("alchemy.elements.create_fire():", alchemy.create_fire())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.elements.create_water():", alchemy.create_water())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.elements.create_earth():", alchemy.create_earth())
    except AttributeError:
        print("alchemy.elements.create_earth(): AttributeError - not exposed")

    try:
        print("alchemy.elements.create_air():", alchemy.create_air())
    except AttributeError:
        print("alchemy.elements.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print("Version: ", alchemy.__version__)
    print("Author:", alchemy.__author__)
