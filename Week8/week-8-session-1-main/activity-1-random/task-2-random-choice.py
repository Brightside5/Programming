import random

# reading & cleaning the data
with open("names.txt") as f:
    names = f.readlines()
names = [ name.strip() for name in names ]

'''
names is a list of 1000 names - each name is 2 words long (in format: firstname surname).

You have three tasks:

Task 1:

Ask the user to enter a number, and pick that many random names out of the list.


Task 2:

Create 10 new random names by picking 10 random firstnames and combining them with 10 random surnames.

Task 3:

Shuffle the list and create 250 teams of 4 random people.
Hint: use a list-of-lists to store the teams.

'''

n = int(input("Please enter the number of names you want to pick out:"))
random.seed(10)

# Task 1: Pick n random names
picked_names = random.sample(names, n)
print("Picked names:", picked_names)

# Task 2: Create 10 new random names
firstnames = [name.split()[0] for name in names]
surnames = [name.split()[1] for name in names]
new_names = [random.choice(firstnames) + " " + random.choice(surnames) for _ in range(10)]
print("New random names:", new_names)

# Task 3: Shuffle and create 250 teams of 4
random.shuffle(names)
teams = [names[i:i+4] for i in range(0, len(names), 4)]
print("Teams:")
for i, team in enumerate(teams, 1):
    print(f"Team {i}: {team}")
