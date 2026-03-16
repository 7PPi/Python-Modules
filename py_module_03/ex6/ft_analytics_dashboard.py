def ft_analystics_dashboard() -> None:
    players: list = [
        ["alice", 2002, True, "north",
         ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon']],
        ["bob", 1450, True, "sul",
         ['first_kill', 'level_10', 'boss_slayer', 'collector']],
        ["charlie", 2500, True, "east",
         ['level_10', 'treasure_hunter', 'boss_slayer',
          'speed_demon', 'perfectionist']],
        ["diana", 1200, False, "west", ['first_kill', 'level_10']]
    ]
    data: list = []
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    data = [p[0] for p in players if p[1] > 2000]
    print(f"High scorers ( >2000): {data}")
    data.clear()
    data = [p[1] * 2 for p in players]
    print(f"Scores doubled: {data}")
    data.clear()
    data = [p[0] for p in players if p[2]]
    print(f"Active players: {data}\n")

    print("=== Dict Comprehension Examples ===")
    lib: dict = {p[0]: p[1] for p in players if p[2]}
    scores = {"high": 0, "medium": 0, "low": 0}
    for p in players:
        if p[1] > 2000:
            scores["high"] += 1
        elif p[1] > 1000:
            scores["medium"] += 1
        else:
            scores["low"] += 1
    print(f"Player scores: {lib}")
    print(f"Score categories: {scores}")
    lib.clear()
    lib = {p[0]: len(p[4]) for p in players if p[2]}
    print(f"Achievement counts: {lib}")

    print("\n=== Set Comprehension Examples ===")
    se: set = {p[0] for p in players}
    print(f"Unique players: {se}")
    se.clear()
    se = {ach for p in players for ach in p[4]}
    print(f"Unique achievements: {se}")
    se.clear()
    se = {p[3] for p in players if p[2]}
    print(f"Active regions: {se}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    se.clear()
    se = {ach for p in players for ach in p[4]}
    print(f"Total unique achievements: {len(se)}")
    t: int = 0
    top: int = 0
    best: int = []
    for p in players:
        t += p[1]

    for p in players:
        if p[1] > top:
            top = p[1]
    for p in players:
        if p[1] == top:
            best = p
            break

    print(f"Average score: {t / len(players):.1f}")
    print(f"Top performer: {best[0]} ", end="")
    print(f"({best[1]} points, {len(best[4])} achievements)")


if __name__ == "__main__":
    ft_analystics_dashboard()
