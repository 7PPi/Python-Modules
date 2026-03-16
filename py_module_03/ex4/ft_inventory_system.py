"""Module documentation."""
from typing import Any
import sys


def ft_inventory_system() -> None:
    """ft_inventory_system function."""
    print("=== Inventory System Analysis ===")
    i: int = 1
    inventory: dict = {}
    total_items: int = 0
    max_v: int = 0
    min_v: int = 200000000
    try:
        if (len(sys.argv) == 1):
            raise ValueError("ERROR: Invalid input, You didnt insert any data")
        while i < len(sys.argv):
            find = False
            name = ""
            number = ""
            for ch in sys.argv[i]:
                if ch == ":":
                    find = True
                elif not find:
                    name += ch
                else:
                    number += ch
            if not find:
                raise ValueError("ERROR: Invalid data format.")
            inventory[name] = int(number)
            i += 1
        for items in inventory.values():
            total_items += items
            if items > max_v:
                max_v = items
            if items < min_v:
                min_v = items

        print("Total items in inventory: ", total_items)
        print("Unique item types: ", len(inventory))

        print("\n=== Current Inventory ===")
        i = 0
        levelm = max_v
        while max_v > 0 and i < len(inventory):
            for item, qunt in inventory.items():
                if max_v == qunt:
                    per = (qunt/total_items)*100
                    print(f"{item}: {qunt} units ({per:.1f}%)")
                    i += 1
            max_v -= 1

        print("\n=== Inventory Statistics ===")
        pr: bool = False
        for item, qunt in inventory.items():
            if qunt == levelm and not pr:
                print(f"Most abundant: {item} ({qunt} units)")
                pr: bool = True
        pr: bool = False
        for item, qunt in inventory.items():
            if qunt == min_v and not pr:
                print(f"Least abundant: {item} ({qunt} units)")
                pr: bool = True

        print("\n=== Item Categories ===")
        entries = [f"'{item}': {qunt}" for item, qunt in inventory.items()
                   if qunt == levelm]
        print(f"Moderate: {{{', '.join(entries)}}}")

        scarce_entries = [f"'{item}': {qunt}"
                          for item, qunt in inventory.items()
                          if qunt != levelm]
        print(f"Scarce: {{{', '.join(scarce_entries)}}}")

        print("\n=== Management Suggestions ===")
        entries = [f"{item}" for item, qunt in inventory.items()
                   if qunt == min_v]
        print(f"Restock needed: {entries}")

        print("\n=== Dictionary Properties Demo ===")
        entries = [f"{item}" for item in inventory.keys()]
        print(f"Dictionary keys: {entries}")
        entries = [f"{item}" for item in inventory.values()]
        print(f"Dictionary valeus: {entries}")
        for k in inventory.keys():
            entries = k
            break
        print(f"Sample lookup - '{entries}'", end="")
        if inventory.get(entries) is None:
            entries = False
        else:
            entries = True
        print(f" in inventory: {entries}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    ft_inventory_system()
