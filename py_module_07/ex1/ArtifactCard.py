"""Module documentation."""
from typing import Any
from ex0.Card import Card


class ArtifactCard(Card):
    """ArtifactCard class."""
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        """__init__ function."""
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.type = 'Artifact'
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """play function."""
        effect = 'Permanent: +1 mana per turn'
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect
        }

    def activate_ability(self) -> dict:
        """activate_ability function."""
        return {
            "artificial": self.name,
            "ability_triggered": True,
            "durability_remaining": self.durability
        }

    def get_card_info(self) -> dict:
        """get_card_info function."""
        info = super().get_card_info()
        info.update({"type": self.type,
                    "durability": self.durability,
                     "effect": self.effect})
        return info
