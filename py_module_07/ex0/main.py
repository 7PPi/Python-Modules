from .CreatureCard import CreatureCard
from .Card import Rarity

if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")

    print("\nCreatureCard Info:")
    card1 = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
    print(card1.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {card1.is_playable(6)}")
    print(f"Play result: {card1.play(None)}")

    print("\nFire Dragon attacks Goblin Warrior:")
    card2 = CreatureCard("Goblin Warrior", 5, Rarity.RARE.value, 6, 5)

    print(f"Attack result: {card1.attack_target(card2)}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {card2.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")
