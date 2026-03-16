def ft_count_harvest_recursive() -> None:
    days: str = input("Days unitl harvest: ")
    i: int = 1

    def ftrecurvise(i) -> None:
        if i > int(days):
            print("Harvest time!")
            return
        else:
            print(f"Day {i}")
            return (ftrecurvise(i + 1))
    ftrecurvise(i)
