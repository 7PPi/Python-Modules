"""Module documentation."""
from typing import Any
def ft_ancient_text() -> Any:
    """ft_ancient_text function."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        file = open("ancient_fragment.txt", "r")
        print("Connection established...\n")

        context = file.read()
        print("RECOVERED DATA:")
        print(context)
        print("\nData recovery complete. Storage unit disconnected.")
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except PermissionError:
        print("ERROR: Storage vault unreadable. Permission Denied!!")
        file.close()


if __name__ == "__main__":
    ft_ancient_text()
