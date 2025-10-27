# write code to import the item module
from item import InventoryItem


# write code to create an instance of IventoryItem with values such as
# name = "Laptop", sku = "LAP24", quantity=12, price_per_unit = 750.99
inventoryitem = InventoryItem('Laptop','LAP24',12,750.99)

# write code to display the item details
inventoryitem.display_item()


# write code to add stock by calling the add_stock method, e.g., to add 25 items
inventoryitem.add_stock(25)

# write code to remove stock by calling the remove_stock method, e.g., to remove 8 items
inventoryitem.remove_stock(8)


