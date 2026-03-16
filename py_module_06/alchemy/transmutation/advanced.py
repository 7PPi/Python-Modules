"""Module documentation."""
from typing import Any
from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """philosophers_stone function."""
    return (
        f"Philosopher's stone created using {lead_to_gold()}"
        f"and {healing_potion()}"
    )


def elixir_of_life() -> str:
    """elixir_of_life function."""
    return "Elixir of life: eternal youth achieved!"
