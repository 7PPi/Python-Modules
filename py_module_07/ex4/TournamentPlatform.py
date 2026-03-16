"""Module documentation."""
from typing import Any
from .TournamentCard import TournamentCard
import random


class TournamentPatform:
    """TournamentPatform class."""
    def __init__(self) -> None:
        """__init__ function."""
        self.cards = {}
        self.matches_played = 0
        self.total_ratings = 0

    def register_card(self, card: TournamentCard) -> str:
        """register_card function."""
        self.cards.update({card.id: card})
        return card.id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """create_match function."""
        try:
            self.matches_played += 1
            winner = random.choice([card1_id, card2_id])
            loser = card1_id if card1_id != winner else card2_id
            winner = self.cards[winner]
            loser = self.cards[loser]
            winner.update_wins(1)
            loser.update_losses(1)

            return {
                "winner": winner.id,
                "loser": loser.id,
                "winner_rating": winner.calculate_rating(),
                "loser_rating": loser.calculate_rating()
            }
        except KeyError:
            return "ERROR: Card id not found"

    def get_leaderboard(self) -> list:
        """get_leaderboard function."""
        leaderboard = []
        ratings = [rate.rating for rate in self.cards.values()]
        ratings.sort(reverse=True)
        for rate in ratings:
            for id, card in self.cards.items():
                if card.rating == rate:
                    leaderboard.append((card.name, card.rating,
                                        f"{card.wins}-{card.losses}"))
        return leaderboard

    def generate_tournament_report(self) -> dict:
        """generate_tournament_report function."""
        count = 0
        total_r = 0
        for card in self.cards.values():
            total_r += card.rating
            count += 1
        return {
            "total_cards": count,
            "matches_played": self.matches_played,
            "avg_rating": round(total_r / count),
            "platform_status": "active"
        }
