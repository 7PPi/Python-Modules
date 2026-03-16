"""Module documentation."""
from .EliteCard import EliteCard

if __name__ == "__main__":
    print("=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    print("-Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: : ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats'")

    print("\nPlaying Arcane Warrior (Elite Card):")

    elite = EliteCard('Arcane Warrior', 4, "common", 4, "melee", 5, 5, 4)
    print("\nCombat phase:")
    print(f"Attack results: {elite.attack('Enemy')}")
    print(f"Defense result: {elite.defend(2)}")

    print("\nMagic phase:")
    print(f"Spell cast: {elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {elite.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")
