def crisis_response(file: str) -> None:
    try:
        print(f"\nCRISIS ALERT: Attempting access to '{file}'...")
        with open(file, 'r') as test:
            print(f"SUCCESS: Archive recovered - {test.read()}")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("Something went wrong!!")


def routine_response(file: str) -> None:
    try:
        print("\nROUTINE ACCESS: ", end='')
        print(f"Attempting access to '{file}'...")
        with open(file, 'r') as archive:
            print(f"SUCCESS: Archive recovered - ''{archive.read()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("Something went wrong!!")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    crisis_response('lost_archive.txt')
    crisis_response('classified_vault.txt')
    routine_response('standard_archive.txt')

    print("\nAll crisis scenarios handled successfully. Archives secure.")
