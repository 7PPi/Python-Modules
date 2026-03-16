def mage_counter() -> callable:
    counter = 0

    def inner() -> int:
        nonlocal counter
        counter += 1
        return counter
    return inner


def spell_accumulator(initial_power: int) -> callable:
    def inner(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power
    return inner


def enchantment_factory(enchantment_type: str) -> callable:
    def inner(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return inner


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key: str, value: str) -> None:
        vault.update({key: value})

    def recall(key) -> str:
        stored = vault.get(key)
        if stored is None:
            stored = "Memory not found"
        return stored
    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":
    try:
        print("Testing mage_counter...")
        counter = mage_counter()
        print(f"Call 1: {counter()}")
        print(f"Call 2: {counter()}")
        print(f"Call 3: {counter()}")

        print("\nTesting spell accumulator...")
        acuumulator = spell_accumulator(10)
        print(f"Spell 1: {acuumulator(5)}")
        print(f"Spell 2: {acuumulator(5)}")
        print(f"Spell 3: {acuumulator(5)}")

        print("\nTesting enchantment factory...")
        flame = enchantment_factory("Flaming")
        froze = enchantment_factory("Froze")
        print(flame("Sword"))
        print(froze("Shield"))

        print("\nTesting memory vault...")
        vault = memory_vault()
        print("Storing and recalling the the data...")
        vault["store"]("name", "etchipoq")
        print(vault["recall"]("name"))
        print(vault["recall"]("project"))
    except Exception as e:
        print("ERROR: ", e)
