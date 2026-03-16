def ft_archive_creation():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    try:
        file = open('new_discovery.txt', 'w')
        print("Storage unit created successfully...")
        print("\nInscribing preservation data...")

        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        print("[ENTRY 001] New quantum algorithm discovered")

        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        print("[ENTRY 002] Efficiency increased by 347%")

        file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        print("[ENTRY 003] Archived by Data Archivist trainee")

        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ", end="")
        print("ready for long-term preservation.")
        file.close()
    except PermissionError:
        print("ERROR: Storage vault unreadable. Permission Denied!!")
        file.close()


if __name__ == "__main__":
    ft_archive_creation()
