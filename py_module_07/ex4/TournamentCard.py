"""Module documentation."""
from typing import Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """TournamentCard class."""
    def __init__(self, name: str, id: str, wins: int, losses: int,
                 rating: int, attack_power: Any, defense: Any, health: Any) -> None:
        """__init__ function."""
        try:
            self.name = name
            self.id = id
            self.wins = int(wins)
            self.losses = int(losses)
            self.rating = int(rating)
            self.interfaces = ["Card", "Combatable", "Rankable"]
            self.health = int(health)
            self.damage = int(attack_power)
            self.defense = int(defense)
        except ValueError as e:
            print("ERROR: Non-numeric value detected,", e)

    def play(self, game_state: dict) -> dict:
        """play function."""
        return super().play(None)

    def attack(self, target: Any) -> dict:
        """attack function."""
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_power,
        }

    def calculate_rating(self) -> int:
        """calculate_rating function."""
        self.rating = self.rating + (self.wins * 16) - (self.losses * 16)
        return self.rating

    def update_wins(self, wins: int) -> None:
        """update_wins function."""
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        """update_losses function."""
        self.losses += losses

    def get_rank_info(self) -> dict:
        """get_rank_info function."""
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        """get_tournament_stats function."""
        return {
            "card": self.name,
            "rating": self.rating,
            "record": f"{self.wins} - {self.losses}"
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
