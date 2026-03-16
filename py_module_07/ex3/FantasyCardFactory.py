from .CardFactory import CardFactory
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, Effect_type
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creature = {
            "dragon": ("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5),
            "goblin": ("Goblin", 2, Rarity.LEGENDARY.value, 2, 1)
        }
        self._spell = {
                "fireball": ("Fireball", 3, Rarity.RARE.value,
                             Effect_type.DAMAGE.value)
        }
        self._artifact = {
            "mana_ring": ("Mana Crystal", 2, Rarity.COMMON.value, 5,
                          "Permanent: +1 mana per turn"),
            "bolt": ("Lighting Bolt", 2, Rarity.COMMON.value, 5,
                     "Permanent: +1 mana per turn")
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in self._creature:
            (name, cost, rarity, attack,
             health) = self._creature[name_or_power]
            return CreatureCard(name, cost, rarity, attack, health)
        else:
            (name, cost, rarity, attack,
             health) = random.choice(list(self._creature.values()))
            return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in self._spell:
            (name, cost, rarity, effect) = self._spell[name_or_power]
            return SpellCard(name, cost, rarity, effect)
        else:
            (name, cost, rarity,
             effect) = random.choice(list(self._spell.values()))
            return SpellCard(name, cost, rarity, effect)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in self._artifact:
            (name, cost, rarity, durability,
             effect) = self._artifact[name_or_power]
            return ArtifactCard(name, cost, rarity, durability, effect)
        else:
            (name, cost, rarity, durability,
             effect) = random.choice(list(self._artifact.values()))
            return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict:
        deck = {
            "creatures": [],
            "spells": [],
            "artifacts": []
        }
        for i in range(size):
            type = random.choice(list(deck.keys()))
            if type == "creatures":
                deck["creatures"].append(self.create_creature())
            elif type == "spells":
                deck["spells"].append(self.create_spell())
            elif type == "artifacts":
                deck["artifacts"].append(self.create_artifact())
        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": list(self._creature),
            "spells": list(self._spell),
            "artifacts": list(self._artifact)
        }
