"""Module documentation."""
from typing import Any
from ex0.Card import Card
from enum import Enum


class Effect_type(Enum):
    """Effect_type class."""
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    """SpellCard class."""
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        """__init__ function."""
        super().__init__(name, cost, rarity)
        self.type = 'Spell'
        if effect_type in [member.value for member in Effect_type]:
            self.effect_type = effect_type
        else:
            self.effect_type = Effect_type.DAMAGE.value

    def play(self, game_state: dict) -> dict:
        """play function."""
        effect = f"Deal {self.cost} damage to target"
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect
        }

    def resolve_effect(self, targets: list) -> dict:
        """resolve_effect function."""
        return {
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True
        }

    def get_card_info(self) -> dict:
        """get_card_info function."""
        info = super().get_card_info()
        info.update({"type": self.type,
                     "effect type": self.effect_type})
        return info
