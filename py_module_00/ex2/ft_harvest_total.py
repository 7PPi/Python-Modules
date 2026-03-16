def ft_harvest_total() -> None:
    i: int = 1
    total: int = 0
    while i < 4:
        harvest = input(f"Day {i} harvest: ")
        total = total + int(harvest)
        i = 1 + i
    print("Total harvest: ", total)
