
"""Safely simulate a secret leak for Git security testing."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEST_FILE = PROJECT_ROOT / "test_leak.py"

# Build a fake test token from separate pieces.
# The complete token is not stored in this source file.
TEST_VALUE = "ghp_" + "0123456789abcdef" + "0123456789abcdef" + "0123"


def generate():
    """Create a temporary file containing a fake credential."""
    TEST_FILE.write_text(
        f'# Temporary security test file\nTEST_TOKEN = "{TEST_VALUE}"\n',
        encoding="utf-8",
    )
    print("Temporary fake-secret file created: test_leak.py")


def cleanup():
    """Remove the temporary test file."""
    if TEST_FILE.exists():
        TEST_FILE.unlink()
        print("Temporary test file removed.")
    else:
        print("No temporary test file found.")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {"generate", "cleanup"}:
        print("Usage: python scripts/simulate_leak.py [generate|cleanup]")
        sys.exit(1)

    if sys.argv[1] == "generate":
        generate()
    else:
        cleanup()
