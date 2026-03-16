"""Module documentation."""
from typing import Any
from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    """Rarity class."""
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    """Card class."""
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """__init__ function."""
        try:
            self.name = name
            self.cost = int(cost)
            if rarity in [member.value for member in Rarity]:
                self.rarity = rarity
            else:
                self.rarity = Rarity.COMMON.value
        except ValueError:
            return "ERROR: Card's cost is not numerical value."

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """play function."""
        return {
            "card_played": self.name,
            "mana_used": self.cost
        }

    def get_card_info(self) -> dict:
        """get_card_info function."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """is_playable function."""
        return (available_mana >= self.cost)
