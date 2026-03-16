"""Module documentation."""
from typing import Any
from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """CardFactory class."""
    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """create_creature function."""
        ...

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """create_spell function."""
        ...

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """create_artifact function."""
        ...

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """create_themed_deck function."""
        ...

    @abstractmethod
    def get_supported_types(self) -> dict:
        """get_supported_types function."""
        ...
