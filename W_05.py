


inventory = {}
def add_item():
 item_id = input("Enter item ID: ")
 item_name = input("Enter item name : ")
 quantity = input("Enter quantity : ")
 price = input("Enter price : ")
 inventory[item_id]

 # Add item_id, name, quantity, price to inventory
 pass
def update_quantity():
 # Update quantity of an existing item
 pass

def search_item():
 # Search item using item_id and display details
 pass
def display_items():
 # Display all items in inventory
 pass
def total_inventory_value():
 # Calculate and display total inventory value
 pass
def low_stock_items():
 # Display items with quantity less than 5
 pass
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