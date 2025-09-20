# Week 2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists

list = {
        "Radiohead": ["OK Computer", "KID A", "In Rainbows"],
        "Kanye West": ["My beautiful Dark Twisted Fantasy", "The life of Pablo", "808 & Heartbreak"],
        "The Weeknd": ["After Hours", "Dawn FM", "Hurry Up Tomorrow"]
        }

list.update({"Lorde":["Pure Heroine", "Melodrama", "Virgin"]})

# Pretty-print the data structure
#Contrast

print(list)
pprint(list)