import sys
import os
import site


def venv() -> None:
    print("MATRIX STATUS: Welcome to the construct")

    print("\nCurrent Python:", sys.executable)
    print("Virtual Environment:", os.path.basename(sys.prefix))
    print("Environment Path:", sys.prefix)

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")

    print("\nPackage installation path:")
    print(site.getsitepackages()[0])


def genv():
    print("MATRIX STATUS: You're still plugged in")

    print("\nCurrent Python:", sys.executable)
    print("Virtual Environment: None detected")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print('activate # On Windows')

    print("\nThen run this program again.")


if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        venv()
    else:
        genv()
