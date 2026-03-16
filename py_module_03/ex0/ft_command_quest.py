import sys

if __name__ == "__main__":
    i = 1
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided")
    else:
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]} ")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")
