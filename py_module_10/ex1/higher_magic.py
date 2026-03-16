def spell_combiner(spell1: callable, spell2: callable) -> callable:
    if callable(spell1) and callable(spell2):
        return lambda x: (spell1(x), spell2(x))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    if callable(base_spell):
        return lambda x: base_spell(x) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    if callable(condition) and callable(spell):
        return lambda x: spell(x) if condition(x) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    valid_spells = [spell for spell in spells if callable(spell)]
    return lambda x: [spell(x) for spell in valid_spells]


# Helpers
def hit(name: str) -> str:
    return f"Fireball hits {name}"


def heal(name: str) -> str:
    return f"Heals {name}"


def base(power: int) -> int:
    return power


def condition(spell: str) -> bool:
    return spell == "Fire"


if __name__ == "__main__":
    try:
        print("Testing spell combiner...")
        dual_cast = spell_combiner(hit, heal)

        print(f"Combined spell result: {dual_cast('Dragon')[0]}", end="")
        print(f", {dual_cast('Dragon')[1]}")

        mega_power = power_amplifier(base, 3)
        print("\nTesting power amplifier...")
        print("Original: 10, Amplified:", mega_power(10))

        cond = conditional_caster(condition, hit)
        print("\nTesting conditional caster...")
        print(cond("Fire"))

        sequence = spell_sequence([hit, heal])
        print("\nTesting spell sequence...")
        print(sequence("drag"))
    except Exception as e:
        print("ERROR: ", e)
