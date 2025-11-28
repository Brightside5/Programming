# Using the pathlib module: 
# https://docs.python.org/3/library/pathlib.html

# usage: python pathinfo.py

from pathlib import Path

file_path = Path("testdir/subdir1/test2.txt")

print("Path:", file_path)

# test some pathlib features
# is_file(), is_dir()
# name, stem, suffix, parent

print("Path:", file_path)
print("Is this a file?", file_path.is_file())
print("File name:", file_path.name)
print("File stem:", file_path.stem)
print("File suffix:", file_path.suffix)
print("Parent:", file_path.parent)
print("Is parent a directory?", file_path.parent.is_dir())

new_path = file_path.parent / "newfile.txt"
print("New path:", new_path)

# Same as the above code, but simpler:
new_path = file_path.with_stem("newfile")

# Write something into a file
new_path.write_text("Hello World!")

# Read it back
text = new_path.read_text()
print(f"Contents of {new_path.name}: {text}")
