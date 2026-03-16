"""Module documentation."""
from typing import Any
def record_spell(spell_name: str, ingredients: str) -> str:
    """record_spell function."""
    from .validator import validate_ingredients
    validation = validate_ingredients(ingredients)
    if "Valid" in validation:
        return f"Spell recorded: {spell_name} ({validation})"
    else:
        return f"Spell rejected: {spell_name} ({validation})"
