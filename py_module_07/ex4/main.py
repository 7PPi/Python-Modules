from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPatform

if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===")

    print("\nRegistering Tournament Cards...")
    tournament = TournamentPatform()
    cards = [
            TournamentCard("Fire Dragon", "dragon_001", 0, 0, 1200, 5, 5, 5),
            TournamentCard("Ice Wizard", "wizard_001", 0, 0, 1150, 5, 5, 5)
            ]
    for card in cards:
        print(f"\n{card.name} (ID: {card.id})")
        print(f"-Interfaces: {card.interfaces}")
        print(f"-Rating: {card.rating}")
        print(f"-Record: {card.wins}-{card.losses}")
        tournament.register_card(card)

    print("\nCreating tournament match...")
    print("Match resut:", tournament.create_match("dragon_001", "wizard_001"))

    print("\nTournament Leaderboard:")
    leaderboard = tournament.get_leaderboard()
    i = 1
    for position in leaderboard:
        print(f"{i}. {position[0]} - Rating: {position[1]} ({position[2]})")
        i += 1

    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
