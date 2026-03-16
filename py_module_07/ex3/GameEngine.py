from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.hand = None
        self.strategy = None
        self.hand = []
        self.cards_count = 0
        self.battlefield = []
        self.turns = 0
        self.damage = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.battlefield.append(CreatureCard('Enemy Player', 2, "c", 2, 5))
        self.battlefield.append(CreatureCard('Enemy Goblin', 3, "c", 2, 5))
        self.battlefield.append(SpellCard("Fireball", 3, "rare", "damage"))

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            return "ERROR: Must configure engine first"
        self.cards_count = 3
        deck = self.factory.create_themed_deck(self.cards_count)
        for cards in deck.values():
            for card in cards:
                self.hand.append(card)
        result = self.strategy.execute_turn(self.hand, self.battlefield)
        print(f"Hand: {[name.name for name in self.hand]}")

        print("\nTurn execution:")
        print("Strategy:", self.strategy.get_strategy_name())
        self.damage += result['damage_dealt']
        self.turns += 1
        return result

    def get_engine_status(self) -> dict:
        print("\nGame Report:")
        if not self.factory or not self.strategy:
            return "ERROR: Must simulate turn first"
        return {
            "turns simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.damage,
            "cards_created": self.cards_count
        }
