"""Module documentation."""
from typing import Any
from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """EliteCard class."""
    def __init__(self, name: str, cost: int, rarity: str, health: int,
                 combat_type: str,
                 attack: int, defense: int, mana: int) -> None:
        """__init__ function."""
        super().__init__(name, cost, rarity)
        self.health = health
        self.combat_type = combat_type
        self.damage = attack
        self.type = "Elite"
        self.defense = defense
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        """play function."""
        info = super().play(None)
        info.update({"effect"})

    def attack(self, target: str) -> dict:
        """attack function."""
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        """defend function."""
        if incoming_damage < self.defense:
            blocked = self.defense - incoming_damage
            alive = True
        else:
            blocked = self.defense if self.defense > -1 else 0
            damage = incoming_damage - self.defense
            self.health -= damage
            if self.health <= 0:
                alive = False
                self.health = 0
            else:
                alive = True
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": blocked,
            "still_alive": alive
        }

    def get_combat_stats(self) -> dict:
        """get_combat_stats function."""
        return {
            "attack": self.damage,
            "heath": self.health,
            "defense": self.defense
            }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """cast_spell function."""
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost
        }

    def channel_mana(self, amount: int) -> dict:
        """channel_mana function."""
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        """get_magic_stats function."""
        return {
            "available_mana": self.mana
        }
