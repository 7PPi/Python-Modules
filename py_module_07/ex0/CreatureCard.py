from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        try:
            super().__init__(name, cost, rarity)
            self.attack = int(attack)
            self.type = 'Creature'
            self.health = health
        except ValueError:
            return "ERROR: Card's attack is not numerical value."

    def play(self, game_state) -> dict:
        info = super().play(game_state)
        info.update({"effect": "Creature summoned to battlefield"})
        return info

    def attack_target(self, target) -> dict:
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
        info = super().get_card_info()
        info.update({"type": self.type,
                     "attack": self.attack,
                    "health": self.health})
        return info
