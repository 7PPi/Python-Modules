"""Module documentation."""
from typing import Any
from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """lead_to_gold function."""
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """stone_to_gem function."""
    return f"Stone transmuted to gem using {create_earth()}"
