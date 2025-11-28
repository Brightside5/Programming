# Copies a directory tree (ie. folder and subfolder contents)
# usage: python copytree.py <source-dir> <dest-dir>
# eg. python copytree.py testdir testcopy

import sys
import shutil   # explore the methods available in this module

try:
    source = sys.argv[1]
    destination = sys.argv[2]
except IndexError:
    sys.exit("Usage: python copytree.py <source-dir> <dest-dir>")

shutil.copytree(source, destination)