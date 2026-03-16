"""Module documentation."""
from typing import Any
from abc import ABC, abstractmethod


class Combatable(ABC):
    """Combatable class."""
    @abstractmethod
    def attack(self, target: Any) -> dict:
        """attack function."""
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """defend function."""
        ...

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """get_combat_stats function."""
        ...
