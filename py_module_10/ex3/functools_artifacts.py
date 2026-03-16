import functools
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    result = 0
    if operation == "min":
        result = functools.reduce(min, spells)
    elif operation == "max":
        result = functools.reduce(max, spells)
    elif operation == "mul":
        result = functools.reduce(operator.mul, spells)
    elif operation == "add":
        result = functools.reduce(operator.add, spells)
    return result


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
            "fire_enchant": functools.partial(
                base_enchantment, 50, "fire_enchant"),
            "ice_enchant": functools.partial(
                base_enchantment, 50, "ice_enchant"),
            "lightning_enchant": functools.partial(
                base_enchantment, 50, "lightning_enchant"),
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def dispatch(data: Any):
        return ("Unknown data")

    @dispatch.register(int)
    def _(data: int):
        return f"Spell damage: {data}"

    @dispatch.register(str)
    def _(data: str):
        return f"Enchament: {data}"

    @dispatch.register(list)
    def _(data: list):
        return f"Multicast: {data}"
    return dispatch


# Helpers
def partial(power, element, target):
    return f"{element} attacks with {power} force at {target}"


if __name__ == "__main__":
    try:
        spell_powers = [42, 34, 50, 40, 38, 15]
        operations = ['add', 'multiply', 'max', 'min']
        fibonacci_tests = [18, 15, 18]

        print("Testing spell reducer...")
        print("Sum: ", spell_reducer(spell_powers, "add"))
        print("Product:", spell_reducer(spell_powers, "mul"))
        print("Max:", spell_reducer(spell_powers, "max"))

        print("\nTesting partial enchanter..")
        attacks = partial_enchanter(partial)
        print(attacks["fire_enchant"]("me"))

        print("\nTesting memoized fibonacci...")
        print("Fib(10):", memoized_fibonacci(10))
        print("Fib(15):", memoized_fibonacci(15))

        print("\nTesting spell dispatcher...")
        dispatch = spell_dispatcher()
        print(dispatch(50))
    except Exception as e:
        print("ERROR: ", e)
