#!/usr/bin/env python
import sys
import subprocess

MAX_VERSION = (3, 11)

# ✅ Compare major.minor
current_version = sys.version_info[:2]

if current_version <= MAX_VERSION:
    # Build command: start with pylint, add args from command line
    command = ["pylint"] + sys.argv[1:]

    print("[INFO] Running:", " ".join(command))
    result = subprocess.run(command)
    sys.exit(result.returncode)
else:
    print(f"[WARNING] Skipping pylint: Python {current_version[0]}.{current_version[1]} > {MAX_VERSION[0]}.{MAX_VERSION[1]}")
    sys.exit(0)
