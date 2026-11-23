"""CLI for Code Repair Feedback Loop."""
import argparse
from .core import CodeRepairLoop

def main():
    parser = argparse.ArgumentParser(description="Code Repair Feedback Loop CLI")
    parser.add_argument("--demo", action="store_true", help="Run repair diagnosis demo")
    args = parser.parse_args()

    sample_tb = """Traceback (most recent call last):
  File "main.py", line 12, in run
    data = json.loads(payload)
NameError: name 'json' is not defined"""

    action = CodeRepairLoop.diagnose_traceback(sample_tb)
    if action:
        print(f"Diagnosed {action.repair_type.upper()}! Suggested Fix: {action.suggested_fix}")

if __name__ == "__main__":
    main()
