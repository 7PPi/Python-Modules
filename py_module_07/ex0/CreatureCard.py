"""Module documentation."""
from typing import Any
from .Card import Card


class CreatureCard(Card):
    """CreatureCard class."""
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        """__init__ function."""
        try:
            super().__init__(name, cost, rarity)
            self.attack = int(attack)
            self.type = 'Creature'
            self.health = health
        except ValueError:
            return "ERROR: Card's attack is not numerical value."

    def play(self, game_state: Any) -> dict:
        """play function."""
        info = super().play(game_state)
        info.update({"effect": "Creature summoned to battlefield"})
        return info

    def attack_target(self, target: Any) -> dict:
        """attack_target function."""
        if self.attack >= target.health:
            result = True
            damage = self.attack
        else:
            result = False
            damage = target.health - self.attack

        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": damage,
            "combat_resolved": result
        }

    def get_card_info(self) -> dict:
        """get_card_info function."""
        info = super().get_card_info()
        info.update({"type": self.type,
                     "attack": self.attack,
                    "health": self.health})
        return info
