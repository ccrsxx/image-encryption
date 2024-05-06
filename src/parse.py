import os
import sys


def parse_argv() -> str:
    if len(sys.argv) < 2:
        print("Please provide a file path")
        quit()

    file_exists = os.path.exists(sys.argv[1])

    if not file_exists:
        print("File not found")
        quit()

    return sys.argv[1]
