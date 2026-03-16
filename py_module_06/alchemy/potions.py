"""Module documentation."""
from typing import Any
from . import elements


def healing_potion() -> str:
    """healing_potion function."""
    return (
        f"Healing potion brewed with {elements.create_fire()} and "
        f"{elements.create_water()}"
    )


def strength_potion() -> str:
    """strength_potion function."""
    return (f"Strength potion brewed with"
            f"{elements.create_earth()} and {elements.create_fire()}")


def invisibility_potion() -> str:
    """invisibility_potion function."""
    return (f"Invisibility potion brewed with"
            f"{elements.create_air()} and {elements.create_water()}")


def wisdom_potion() -> str:
    """wisdom_potion function."""
    return (
        "Wisdom potion brewed with all elements: "
        f"{elements.create_fire()}, {elements.create_air()}, "
        f"{elements.create_earth()}, {elements.create_water()}"
    )
