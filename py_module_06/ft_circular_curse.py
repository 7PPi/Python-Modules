from alchemy import grimoire


if __name__ == "__main__":
    print("=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    print('validate_ingredients("fire air")',
          grimoire.validate_ingredients("fire air"))
    print('validate_ingredients("dragon scales"):',
          grimoire.validate_ingredients("dragon scales"))

    print("\nTesting spell recording with validation:")
    print('record_spell("Fireball", "fire air"):',
          grimoire.record_spell("Fireball", "fire air"))
    print('record_spell("Dark Magic", "shadow"):',
          grimoire.record_spell("Dark Magic", "shadow"))

    print("\nesting late import technique:")
    print('record_spell("Lightning", "air"):',
          grimoire.record_spell("Lightning", "air"))

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
