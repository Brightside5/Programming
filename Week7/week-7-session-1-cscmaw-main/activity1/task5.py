# Create a Character class with the following fields:
# (1) name - the name of the character
# (2) health - the health of the character, with value between 0 to 100
# (3) attack_power - the attack power of the character, with value between 10 to 100

# When an instance of Character is created, the value to all three fields are required.

class Character:
    def __init__(self, name, health=100, power=10):
        self.name = name
        self.health = health
        self.attack_power = power

# Once completed, create two instances of Character to two of your most favourite game characters.
character1 = Character("Mario", 100, 50)
character2 = Character("Link", 80, 60)

# Then, write code to print the details of each character.
print(f"Character 1 - Name: {character1.name}, Health: {character1.health}, Attack Power: {character1.attack_power}")
print(f"Character 2 - Name: {character2.name}, Health: {character2.health}, Attack Power: {character2.attack_power}")
