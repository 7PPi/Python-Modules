"""Module documentation."""
import importlib
import sys


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")

    print("\nChecking dependencies:")
    rate = 0
    try:
        pandas = importlib.import_module("pandas")
        print(f"[OK] {pandas.__name__} ({pandas.__version__}) ", end="")
        print("- Data manipulation ready")
        rate += 1
    except ImportError:
        print("[ERROR] pandas missing")

    try:
        requests = importlib.import_module("requests")
        print(f"[OK] {requests.__name__} ({requests.__version__}) ", end="")
        print("- Network access ready")
        rate += 1
    except ImportError:
        print("[ERROR] requests missing")

    try:
        matplotlib = importlib.import_module("matplotlib")
        plt = importlib.import_module("matplotlib.pyplot")
        print(f"[OK] {matplotlib.__name__} ({matplotlib.__version__})", end="")
        print("- Visualization ready")
        rate += 1
    except ImportError:
        print("[ERROR] matplotlib missing")

    if rate != 3:
        print("\nERROR: Your enviroment doesnt", end="")
        print(" have teh necessary dependencies")
        print('Use "pip install -r requirements.txt" or "poetry install"'
              ' to install dependences')
        sys.exit(1)

    print("\nAnalyzing Matrix data..")
    try:
        data = requests.get("https://randomuser.me/api/?results=1000")
        data = data.json()
        ages = []

        for user in data["results"]:
            ages.append(user["dob"]["age"])

        sample = pandas.DataFrame({
            "age": ages
        })

        print(f"Processing {ages.__len__()} data points...")
        print("Generating visualization...")
        plt.hist(sample["age"], bins=30)
        plt.title("Age Distribution")
        plt.xlabel("Age")
        plt.ylabel("Frequency")

        print("\nAnalysis complete!")

        plt.savefig("matrix_analysis.png")
        print("Results saved to: matrix_analysis.png}")
    except Exception as e:
        print(f"ERROR: {e}")
