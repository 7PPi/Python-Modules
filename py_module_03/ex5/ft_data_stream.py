import time


def fib(max) -> int:
    num: list = [0, 1]
    n: int = 0
    i: int = 0
    while i < max - 2:
        n = num[0] + num[1]
        num[0] = num[1]
        num[1] = n
        yield num[1]
        i += 1


def prime(max) -> int:
    n: int = 2
    i: int = 0
    while i < max:
        pr = True
        ctrl = 2
        while ctrl < n:
            if n % ctrl == 0:
                pr = False
            ctrl += 1
        if pr:
            yield n
            i += 1
        n += 1


def generator(max) -> list:
    i: int = 0
    names: list = ["alice", "bob", "charlie"]
    actions: list = ["killed monster", "found treasure", "leveled up"]
    data: list = []
    level: int = 0
    while i < max:
        data.append(names[i % 3])
        if i < 342:
            level = 10 + (i % 6)
        else:
            level = (i % 9) + 1
        data.append(level)
        if i < 89:
            data.append(actions[1])
        elif i < 245:
            data.append(actions[2])
        else:
            data.append(actions[0])
        yield data
        i += 1
        data.clear()


def test_gen() -> None:
    data: list = []
    i: int = 0
    high_level: int = 0
    treusure: int = 0
    level_up: int = 0
    gen = generator(1000)
    start_time: float = time.perf_counter()
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...\n")
    for event in gen:
        print(f"Event {i + 1}: Player", end="")
        print(f"{event[0]} (level {event[1]}) {event[2]}")
        i += 1
        if event[1] >= 10:
            high_level += 1
        if event[2] == "found treasure":
            treusure += 1
        elif event[2] == "leveled up":
            level_up += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {i}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treusure}")
    print(f"Level-up events: {level_up}")

    elapsed_time: float = time.perf_counter() - start_time
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {elapsed_time:.4f} seconds")

    print("\n=== Generator Demonstration ===")
    sequence = fib(10)
    for f in sequence:
        data.append(f"{f}")
    print("Fibonacci sequencence (first 10): 0, 1, ", ', '.join(data))

    primes = prime(5)
    data.clear()
    for f in primes:
        data.append(f"{f}")
    print("Prime numbers (first 5):", ', '.join(data))


if __name__ == "__main__":
    test_gen()
