from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.type = 'Artifact'
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        effect = 'Permanent: +1 mana per turn'
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect
        }

    def activate_ability(self) -> dict:
        return {
            "artificial": self.name,
            "ability_triggered": True,
            "durability_remaining": self.durability
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": self.type,
                    "durability": self.durability,
                     "effect": self.effect})
        return info
