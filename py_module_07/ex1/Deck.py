from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
import random


class Deck:
    def __init__(self) -> None:
        self.deck = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            if card == card_name:
                self.deck.pop(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        return self.deck.pop()

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        costs = 0
        for card in self.deck:
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1
            costs += card.cost

        return {
            "total_cards": len(self.deck),
            "creatures": creatures,
            "spells": spells,
            "artififacts": artifacts,
            "avg_cost": round(costs / len(self.deck), 1)
        }
