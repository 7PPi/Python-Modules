from . import elements


def healing_potion() -> str:
    return (
        f"Healing potion brewed with {elements.create_fire()} and "
        f"{elements.create_water()}"
    )


def strength_potion() -> str:
    return (f"Strength potion brewed with"
            f"{elements.create_earth()} and {elements.create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with"
            f"{elements.create_air()} and {elements.create_water()}")


def wisdom_potion() -> str:
    return (
        "Wisdom potion brewed with all elements: "
        f"{elements.create_fire()}, {elements.create_air()}, "
        f"{elements.create_earth()}, {elements.create_water()}"
    )
