"""Module documentation."""
from typing import Any
from abc import ABC, abstractmethod


class Rankable(ABC):
    """Rankable class."""
    @abstractmethod
    def calculate_rating(self) -> int:
        """calculate_rating function."""
        ...

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """update_wins function."""
        ...

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """update_losses function."""
        ...

    @abstractmethod
    def get_rank_info(self) -> dict:
        """get_rank_info function."""
        ...
