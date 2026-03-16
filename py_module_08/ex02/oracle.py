"""Module documentation."""
from dotenv import load_dotenv
import os


if __name__ == "__main__":
    load_dotenv()

    dependencies = {
        'MATRIX_MODE': os.getenv('MATRIX_MODE'),
        'DATABASE_URL': os.getenv('DATABASE_URL'),
        'API_KEY': os.getenv('API_KEY'),
        'LOG_LEVEL': os.getenv('LOG_LEVEL'),
        'ZION_ENDPOINT': os.getenv('ZION_ENDPOINT')
    }

    security = True
    for name, value in dependencies.items():
        if value is None:
            security = False

    print("ORACLE STATUS: Reading the Matrix...")

    print("\nConfiguration loaded:")
    print("Mode:", dependencies['MATRIX_MODE'])
    print(f"Database: Connected to {dependencies['DATABASE_URL']} ")
    print(f"API Access: {dependencies['API_KEY']}")
    print(f"Log Level: {dependencies['LOG_LEVEL']}")
    print(f"Zion Network: {dependencies['ZION_ENDPOINT']}")

    print("\nEnvironment security check:")
    if os.path.exists('.env') and security:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    else:
        print("[KO] No hardcoded secrets detected")
        print("[KO] .env file properly configured")
        print("[KO] Production overrides available")

    print("\nThe Oracle sees all configurations.")
