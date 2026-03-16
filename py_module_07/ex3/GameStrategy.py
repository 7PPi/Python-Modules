"""Module documentation."""
from typing import Any
from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """GameStrategy class."""
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """execute_turn function."""
        ...

    @abstractmethod
    def get_strategy_name(self) -> str:
        """get_strategy_name function."""
        ...

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """prioritize_targets function."""
        ...
