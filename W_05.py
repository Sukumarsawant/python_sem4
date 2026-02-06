


inventory = {}
def add_item():
    item_id = input("Enter item ID: ")
    inventory[item_id] = {}
    inventory[item_id][0] = input("Enter item name : ")
    inventory[item_id][1] = int(input("Enter quantity : "))
    inventory[item_id][2] = float(input("Enter price : "))
    item_name = inventory[item_id][0]
    print(f"item '{item_name}' added successfully !!!")

def update_quantity():
    item_id = input("Enter the item ID : ")
    new_quantity = int(input("Enter the updated quantity"))
    inventory[item_id][1] = new_quantity

def search_item():
    item_id = input("Enter the item id : ")
    if item_id in inventory:
        print(f"Item found : '{inventory[item_id]}'")
    else:
        print("Item not found!!!")


def display_items():
    print("-" * 53) 
    print(f"| {"ID":^5} | {"Name":^20} | {"qty":>5} | {"price":>10} | ")
    print("-" * 53)
    for item_id,v in inventory.items():
        print(f"| {item_id:^5} | {v[0]:<20} | {v[1]:>5} | {v[2]:>10} | ")
    print("-" * 53)

def total_inventory_value():
    t_val = 0
    for item_id,v in inventory.items():
       t_val += v[2]
    print(f"Total inventory value : {t_val}")
 
def low_stock_items():
    ct =0
    print("Following are the low stack item : ")
    for item_id,v in inventory.items():
        if v[1]<5 : 
            print(f"{v[0] + '\n'}")
            ct  = ct+1
    if ct == 0 : print("No low stock item ")

# -------- MENU DRIVEN PROGRAM --------
while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Update Quantity")
    print("3. Search by Item ID")
    print("4. Display All Items")
    print("5. Total Inventory Value")
    print("6. Low Stock Items")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_item()
    elif choice == "2":
        update_quantity()
    elif choice == "3":
        search_item()
    elif choice == "4":
        display_items()
    elif choice == "5":
        total_inventory_value()
    elif choice == "6":
        low_stock_items()
    elif choice == "7":
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Try again.")