# -------A01-----------------------------------------------

inventory = {}
def add_item():
    item_id = input("Enter item ID: ")
    if item_id in inventory:
        print("Item already exists")
        return
    item_name = input("Enter item name : ")
    price = float(input("Enter price : "))
    quantity = int(input("Enter quantity : "))
    inventory[item_id] = [item_name, price, quantity]
    print(f"item '{item_name}' added successfully !!!")

def sell_item():
    item_id = input("Enter Item ID: ")
    if item_id not in inventory:
        print("Item does not exist")
        return
    sell_qty = int(input("Enter Quantity to Sell: "))
    if inventory[item_id][2] >= sell_qty:
        inventory[item_id][2] -= sell_qty
        print(f"{sell_qty} items sold. Remaining stock: {inventory[item_id][2]}")
    else:
        print("Insufficient stock")

def display_items():
    if not inventory:
        print("Inventory is empty")
        return
    print("-" * 53)
    print(f"| {'ID':^5} | {'Name':^20} | {'Price':>7} | {'Quantity':>8} |")
    print("-" * 53)
    for item_id, v in inventory.items():
        print(f"| {item_id:^5} | {v[0]:<20} | {v[1]:>7} | {v[2]:>8} |")
    print("-" * 53)

def total_inventory_value():
    t_val = 0
    for item_id, v in inventory.items():
        t_val += v[1] * v[2]
    print(f"Total inventory value : {t_val}")
 
def low_stock_items():
    found = False
    for item_id, v in inventory.items():
        if v[2] < 5:
            if not found:
                print("-" * 53)
                print(f"| {'ID':^5} | {'Name':^20} | {'Price':>7} | {'Quantity':>8} |")
                print("-" * 53)
                found = True
            print(f"| {item_id:^5} | {v[0]:<20} | {v[1]:>7} | {v[2]:>8} |")
    if not found:
        print("No low stock items")
    elif found:
        print("-" * 53)

# -------- MENU DRIVEN PROGRAM --------
while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Sell Item")
    print("3. Display Low Stock Items")
    print("4. Calculate Total Inventory Value")
    print("5. Display All Items")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_item()
    elif choice == "2":
        sell_item()
    elif choice == "3":
        low_stock_items()
    elif choice == "4":
        total_inventory_value()
    elif choice == "5":
        display_items()
    elif choice == "6":
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Try again.")
# ---------------------------------------------------------
# -----A02-----------------------------------------------

def curriculum_comparison():
    print("\nComparison Between Departments")
    dept_a = input("Enter subjects for Dept A : ").split(",")
    dept_b = input("Enter subjects for Dept B : ").split(",")
    
    a = set(s.strip() for s in dept_a if s.strip())
    b = set(s.strip() for s in dept_b if s.strip())

    all_subjects = a | b
    common_subjects = a & b
    only_a = a - b
    only_b = b - a
    exclusive = a ^ b
    similarity = (len(common_subjects) / len(all_subjects) * 100) if all_subjects else 0

    print(f"All Subjects: {all_subjects}")
    print(f"Common Subjects: {common_subjects}")
    print(f"Only Dept A: {only_a}")
    print(f"Only Dept B: {only_b}")
    print(f"Exclusive Subjects: {exclusive}")
    print(f"Similarity Percentage: {similarity:.2f}%")

if __name__ == "__main__":
    while True:
        curriculum_comparison()
        again = input("Curriculam Comparison : Do you want to compare? (y/n)")
        if again.lower() != "y":
            break
# ----------------------------------------------------------
# -----A03-----------------------------------------------
from string import punctuation

def analyze_text(text):
    
    for p in punctuation:
        text = text.replace(p, "")
    
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:10]

if __name__ == "__main__":
    print("Please input your text")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    user_text = "\n".join(lines)
    print(analyze_text(user_text))
# ----------------------------------------------------------
# -----A04-----------------------------------------------

def add_student(enrollments, course, roll):
    if course not in enrollments:
        enrollments[course] = set()
    enrollments[course].add(roll)
    print(f"Roll number {roll} enrolled in {course}.")

def remove_student(enrollments, course, roll):
    if course not in enrollments:
        print("Course not found")
        return
    if roll not in enrollments[course]:
        print("Roll number not found in this course")
        return
    enrollments[course].remove(roll)
    print(f"Roll number {roll} removed from {course}.")

def display_course(enrollments, course):
    if course not in enrollments:
        print("Course not found")
        return
    print(f"Students enrolled in {course}: {enrollments[course]}")

def list_courses(enrollments):
    if not enrollments:
        print("No courses available")
        return
    print("Courses available:")
    for course in enrollments:
        print(course)

def check_student(enrollments, roll):
    found = False
    for course, students in enrollments.items():
        if roll in students:
            if not found:
                print(f"Student {roll} is enrolled in:")
                found = True
            print(course)
    if not found:
        print("Student not enrolled in any course")

def enrollment_counts(enrollments):
    if not enrollments:
        print("No courses available")
        return
    for course, students in enrollments.items():
        print(f"{course}: {len(students)} students")

if __name__ == "__main__":
    enrollments = {}
    while True:
        print("\nCourse Enrollment Management")
        print("1. Add student")
        print("2. Remove student")
        print("3. Display students in a course")
        print("4. List all courses")
        print("5. Check student enrollment")
        print("6. Show total enrollments per course")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            course = input("Enter course name: ")
            roll = input("Enter roll number: ")
            add_student(enrollments, course, roll)
        elif choice == "2":
            course = input("Enter course name: ")
            roll = input("Enter roll number: ")
            remove_student(enrollments, course, roll)
        elif choice == "3":
            course = input("Enter course name: ")
            display_course(enrollments, course)
        elif choice == "4":
            list_courses(enrollments)
        elif choice == "5":
            roll = input("Enter roll number: ")
            check_student(enrollments, roll)
        elif choice == "6":
            enrollment_counts(enrollments)
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")