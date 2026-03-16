def ft_water_reminder() -> None:
    days: str = input("Days since last watering: ")
    if int(days) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
