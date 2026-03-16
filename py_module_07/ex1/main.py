from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard, Effect_type
from .Deck import Deck

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    creature = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 7)
    spell = SpellCard('Lightning Bolt', 3, Rarity.RARE.value,
                      Effect_type.DAMAGE.value)
    artifact = ArtifactCard('Mana Crystal', 2, Rarity.COMMON.value,
                            2, 'Permanent: +1 mana per turn')

    deck = Deck()
    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)
    print(f"Deck stats: {deck.get_deck_stats()}")
    deck.shuffle()

    i = 0
    print("\nDrawing and playing cards:")
    while i < 3:
        card = deck.draw_card()
        info = card.get_card_info()
        print(f'\nDrew: {info["name"]} ({info["type"]})')
        print(f"Play result: {card.play(None)}")
        i += 1

    print("\nPolymorphism in action: Same interface, ", end="")
    print("different card behaviors!")
