def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(
        artifacts,
        key=lambda x: x["power"],
        reverse=True,
    )
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages = list(filter(lambda x: x["power"] >= min_power, mages))
    return filtered_mages


def spell_transformer(spells: list[str]) -> list[str]:
    maped = list(map(lambda x: "* " + x + " *", spells))
    return maped


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda x: x["power"]),
        'min_power': min(mages, key=lambda x: x["power"]),
        'avg_power': round(sum([p["power"] for p in mages]) / len(mages), 2),
    }


if __name__ == "__main__":
    try:
        test = [
            {'name': "Fire Staff", 'power': 92, 'element': "vjvkd"},
            {'name': "Crystal Orb", 'power': 85, 'element': "vjvkd"},
        ]
        sorted = artifact_sorter(test)

        print("Testing artifact sorter...")
        print(f"{sorted[0]['name']} ({sorted[0]['power']} power) ", end="")
        print(f"comes before {sorted[1]['name']} ({sorted[0]['power']} power)")

        print("\nTesting spell transformer...")
        spells = ["fireball", "heal", "shield"]
        transformed = spell_transformer(spells)
        for spell in transformed:
            print(spell, end=" ")
        print()

        print("\nTesting power filter...")
        print(power_filter(test, 86))

        print("\nTesting mage stats...")
        print("max:", mage_stats(test)['max_power']["power"])
        print("min:", mage_stats(test)['min_power']["power"])
        print("avg:", mage_stats(test)['avg_power'])
    except Exception as e:
        print("ERROR: ", e)
