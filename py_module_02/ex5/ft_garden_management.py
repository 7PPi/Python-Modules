class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def addplant(self, plantllist: list) -> None:
        print("\nAdding plants to garden...")
        try:
            for plant in plantllist:
                if plant[0] is None:
                    raise PlantError(
                        "Error adding plant: Plant name cannot be empty!"
                    )
                print(f"Added {plant[0]} successfully")
        except PlantError as e:
            print(e)
        else:
            print("Added all plants successfully")

    def waterplant(self, plantllist: list) -> None:
        print("\nWatering plants...")
        print("Opening watering system")
        try:
            for plant in plantllist:
                if plant[0] is None:
                    raise GardenError(
                        "Error checking plant water level:"
                        " Plant name cannot be empty!"
                    )
                if int(plant[1]) < 1:
                    raise WaterError(
                        f"Not enough water to water {plant[0]}"
                    )
                print(f"Watering {plant[0]} - success")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self, plantllist: list) -> None:
        print("Checking plant health..")
        try:
            for plant in plantllist:
                if plant[0] is None:
                    raise GardenError(
                        "Error checking plant health:"
                        " Plant name cannot be empty!"
                    )
                if plant[1] < 2:
                    raise WaterError(
                        f"Error checking {plant[0]}: Water level {plant[1]} "
                        "is too low (min 2)"
                    )
                elif plant[1] > 10:
                    raise WaterError(
                        f"Error checking {plant[0]}: Water level {plant[1]} "
                        "is too high (max 10)"
                    )

                if plant[2] < 1:
                    raise GardenError(
                        f"Error checking {plant[0]}: Sunlight hours {plant[2]}"
                        " is too low (min 1)"
                    )
                if plant[2] > 12:
                    raise GardenError(
                        f"Error checking {plant[0]}:"
                        f" Sunlight hours {plant[2]} "
                        "is too high (max 12)"
                    )
                print(
                    f"{plant[0]}: healthy (water: {plant[1]}, sun: {plant[2]})"
                )
        except GardenError as e:
            print(e)
        except WaterError as e:
            print(e)
        else:
            print("All plants are healthy!")
        finally:
            print("Done checking plant health\n")

    def recovery(self, water: int) -> None:
        print("Testing error recovery...")
        try:
            if int(water) < 2:
                raise GardenError(
                    "Caught GardenError: Not enough water in tank"
                )
            print("Garden tank level is good!")
        except GardenError as e:
            print(e)
        except ValueError as e:
            print(f"Invalid input: {e}")
        finally:
            print("System recovered and continuing...")


def test_garden_management() -> None:
    garden = GardenManager()
    plantllist = [
        ["tomato", 4, 4],
        ["lettuce", 2, 20],
        [None, 4, 0]
    ]
    print("=== Garden Management System ===")
    garden.addplant(plantllist)
    plantllist = [
        ["tomato", 4, 4],
        ["lettuce", 2, 20]
    ]
    garden.waterplant(plantllist)
    garden.check_plant_health(plantllist)
    garden.recovery(1)
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
