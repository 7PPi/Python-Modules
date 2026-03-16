def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]
    ing = ingredients.split()
    v = False
    for element in ing:
        if element in valid:
            v = True
        else:
            v = False
    if v:
        r = f"{ingredients} - Valid"
    else:
        r = f"{ingredients} - Invalid"
    return r
