"""Module documentation."""
from typing import Any
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """AggressiveStrategy class."""
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """execute_turn function."""
        mana = 5
        used = 0
        damage = 0
        sorted_hand = []
        remaining_cards = hand.copy()
        while remaining_cards:
            cheapest_index = 0
            for index, card in enumerate(remaining_cards):
                if (
                    card.cost
                    < remaining_cards[cheapest_index].cost
                ):
                    cheapest_index = index
            sorted_hand.append(remaining_cards.pop(cheapest_index))
        played_cards = []
        cards_played = []
        for card in sorted_hand:
            if mana - card.cost >= 0:
                mana -= card.cost
                used += card.cost
                played_cards.append(card)
                cards_played.append(card.name)
        for card in played_cards:
            if isinstance(card, ArtifactCard):
                damage += card.cost
            elif isinstance(card, SpellCard):
                damage += card.cost
            elif isinstance(card, CreatureCard):
                damage += card.attack
        return {
            "cards_played": cards_played,
            "mana_used": used,
            "targets": self.prioritize_targets(battlefield)[0],
            "damage_dealt": damage
        }

    def get_strategy_name(self) -> str:
        """get_strategy_name function."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """prioritize_targets function."""
        order = []
        order2 = []
        targets = []
        for card in available_targets:
            if isinstance(card, CreatureCard):
                order.append(card.health)
        order.sort()
        for card in available_targets:
            if not isinstance(card, CreatureCard):
                order2.append(card.cost)
        order2.sort()
        for c in order:
            for card in available_targets:
                if isinstance(card, CreatureCard) and card.health == c:
                    targets.append(card.name)
        for c in order2:
            for card in available_targets:
                if not isinstance(card, CreatureCard) and card.cost == c:
                    targets.append(card.name)

        return targets
