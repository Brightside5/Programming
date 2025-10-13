# Step 1: Create an empty list for the shopping list.
# optional: see if there is an existing shopping list file and load that
# hint: use try/except to check if the file exists, or import os and use os.path.exists()

shopping_list = []
try:
    with open('shopping_list.txt', 'r') as file:
        shopping_list = [line.strip() for line in file]
except FileNotFoundError:
    pass

# Step 2: Define a function to add an item to the list.
# Prompt the user for the item name and add it to the list.

def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"Added {item} to the list.")

# Step 3: Define a function to remove an item from the list.
# Prompt the user for the item name to remove and delete it from the list if it exists.
# hint: use list.remove() or check if item is in list first

def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed {item} from the list.")
    else:
        print(f"{item} not found in the list.")

# Step 4: Define a function to write the current shopping list to a file called 'shopping_list.txt'.
# hint: use 'w' mode to overwrite the file each time with the current list
# hint: don't forget \n for new lines

def save_list():
    with open('shopping_list.txt', 'w') as file:
        for item in shopping_list:
            file.write(item + '\n')

# Step 5: create the main program loop with a small menu system which lets the user:
# - Call the functions to add or remove items.
# - After each action, write the updated shopping list to 'shopping_list.txt'.
# - Add a way of exiting the program
# hint: use a while loop with a menu and user choice

while True:
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        add_item()
        save_list()
    elif choice == '2':
        remove_item()
        save_list()
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")