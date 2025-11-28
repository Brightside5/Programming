# Displays some useful info about the environment
# usage: python osinfo.py

import os
import sys

# Extract properties of the operating system from os and sys modules
# Use the module documentation to find relevant information.
# eg. platform, shell, current directory

print(f"You are using a {sys.platform} system")

if shell := os.getenv("SHELL"):
    print(f"Your shell is {shell}")

print(f"Your current directory is {os.getcwd()}")

if path := os.getenv("PATH"):
    print("Your PATH includes these directories:")
    path_dirs = path.split(os.pathsep)
    for path_dir in path_dirs:
        print(path_dir)
        