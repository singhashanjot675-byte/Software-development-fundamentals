item_counter = 1000

def add_inventory_item():
    global item_counter
    
    print("Adding Inventory Item:\n")
    
    item_name = input("Item Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per Item: "))
    
    item_id = item_counter
    item_counter += 1
    
    print("\nItem Name:", item_name)
    print("Item ID:", item_id)
    print("Quantity:", quantity)
    print("Price per Item: $%.2f" % price)
    
    return item_name, item_id, quantity, price


add_inventory_item()