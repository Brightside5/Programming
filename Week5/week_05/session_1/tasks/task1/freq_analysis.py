# Frequency analysis is a method of breaking certain ciphers which involves counting the frequency of letters/symbols
# because English has quite a clear distribution of letters, with spikes on common letters such as 'e', 'i' and 's'

# Ask the user for a filename
# open and read the file 
# and count how many instances of each letter are in the program
# hint: use a dictionary!

# Additional hints:
# - Remember to handle the case where the file might not exist
# - You'll need to check each character to see if it's a letter
# - Dictionary pattern: if key exists, increment; if not, set to 1
# - Consider converting to lowercase for consistent counting
try:
    name = input("Please enter the file name:\n")
    with open(name, "r") as infile:
        text = infile.read()
        freq = {}
        for char in text.lower():
            if char.isalpha():
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
        for letter, count in sorted(freq.items()):
            print(f"{letter}: {count}")
except FileNotFoundError:
    print("The file doesn't exist.")