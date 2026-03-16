from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def timer() -> str:
        print(f"Casting {func.__name__}...")
        start = time.time()
        resullt = func()
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        print(resullt)
    return timer


def power_validator(min_power: int) -> callable:
    def power(func: callable):
        @wraps(func)
        def validator(self, spell_name: str, power: int):
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self, spell_name, power)
        return validator
    return power


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def retries(*args):
            result = f"Spell casting failed after {max_attempts} attempt"
            for i in range(1, max_attempts + 1):
                try:
                    result = func(*args)
                    break
                except Exception:
                    print(f"Spell failed, retrying... ({i}/{max_attempts})")
            return result
        return retries
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for ch in name:
            if not ch.isalpha() and not ch.isspace():
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


# helper
def fireball() -> None:
    return "Result: Fireball cast!"


def rtry(name: str) -> None:
    int(name)
    return "Spell casted!!"


if __name__ == "__main__":
    try:
        mage = MageGuild()
        print("Testing spell timer...")
        spell_timer(fireball)()

        print("\nTesting MageGuild...")
        print(mage.validate_mage_name("etchipoq lisbon"))
        print(mage.validate_mage_name("etchipoq 42"))

        print(mage.cast_spell("Lighting", 15))
        print(mage.cast_spell("Lighting", 5))

        print("\nTesting retry spell...")
        spell = retry_spell(3)(rtry)(3)
        print(spell)
    except Exception as e:
        print("ERROR: ", e)
