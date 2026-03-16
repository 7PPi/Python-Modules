
"""Module documentation."""
from typing import Any
def ft_achievement_tracker() -> None:
    """ft_achievement_tracker function."""
    alice: set = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob: set = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie: set = {'level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist'}
    all_achive = set()
    rare = set()

    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice achieviments: {alice}")
    print(f"Player bob achieviments: {bob}")
    print(f"Player charlie achieviments: {charlie}")

    all_achive = alice | bob | charlie
    print("\n=== Achievement Analytics ===w")
    print(f"All unique achievements: {all_achive}")
    print(f"Total unique achievements: {len(alice | bob | charlie)}\n")
    print(f"Common to all players: {alice & bob & charlie}")

    for achievement in all_achive:
        count = 0
        if achievement in bob:
            count += 1
        if achievement in alice:
            count += 1
        if achievement in charlie:
            count += 1
        if count == 1:
            rare.add(achievement)

    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()
