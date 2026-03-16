from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, health: int,
                 combat_type: str,
                 attack: int, defense: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.health = health
        self.combat_type = combat_type
        self.damage = attack
        self.type = "Elite"
        self.defense = defense
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        info = super().play(None)
        info.update({"effect"})

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
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
        return {
            "attack": self.damage,
            "heath": self.health,
            "defense": self.defense
            }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "available_mana": self.mana
        }
