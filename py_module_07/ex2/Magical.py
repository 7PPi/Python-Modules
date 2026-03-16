"""Module documentation."""
from typing import Any
from abc import ABC, abstractmethod


class Magical(ABC):
    """Magical class."""
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """cast_spell function."""
        ...

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """channel_mana function."""
        ...

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """get_magic_stats function."""
        ...
