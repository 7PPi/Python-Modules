"""Module documentation."""
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    print("\nConfiguring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Avaiable types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    engine.configure_engine(factory, strategy)
    print("Actions:", engine.simulate_turn())
    print(engine.get_engine_status())

    print("")
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
