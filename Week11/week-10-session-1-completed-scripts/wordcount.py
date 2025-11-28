# Counts 'words' in a file, even if it has been compressed with gzip
# Usage: python wordcount.py <textfile>
# eg. python wordcount.py testdir/frankenstein.txt.gz

import gzip  # to handle zipped files look for gzip.open() to access the file
import sys

try:
    filename = sys.argv[1]
except IndexError:
    sys.exit("Usage: python wordcount.py <textfile>")

if filename.endswith(".gz"):
    infile = gzip.open(filename, mode="rt")
else:
    infile = open(filename, mode="rt")

word_count = 0
for line in infile:
    words = line.split()
    word_count += len(words)

# or, as a more efficient one-liner:
#word_count = sum(len(line.split()) for line in infile)

print(word_count)