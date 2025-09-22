items = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.8,
    "grapes": 2.0,
    "watermelon": 3.0
}

item_selected = input("Enter the item you want to purchase (apple, banana, orange, grapes, watermelon): ").strip().lower()
quantity = int(input("Enter the quantity: "))

total_cost = 0

if item_selected == "apple":
    total_cost = items["apple"] * quantity