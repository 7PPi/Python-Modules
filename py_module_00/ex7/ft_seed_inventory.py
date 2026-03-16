def ft_seed_inventory(name: str, qunt: int, type: str) -> None:
    if type == "packets":
        print(f"{name} seeds: {qunt} {type} available")
    elif type == "grams":
        print(f"{name} seeds: {qunt} {type} total")
    elif type == "area":
        print(f"{name} seeds: {qunt} {type} square meters")
    else:
        print("Unknown unit type")
