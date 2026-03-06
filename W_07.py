class Employee():
    def __init__(self,empId, name, basicSalary, rating):
        self.__empId = empId
        self.__name = name
        self.__basicSalary = int(basicSalary)
        self.__rating = int(rating)

    @property
    def basicSalary(self):
        if self.__basicSalary < 0 : raise Exception("Give some money ")
        else  : return self.__basicSalary
    @property
    def rating (self):
        if self.__rating <0 | self.__rating >5 : raise Exception("Invalid rating")
        return self.__rating
    
    def calculate_net_salary(self):
        rate = self.rating
        if rate ==1 : bonus = 0
        elif rate ==2 : bonus = 5/100
        elif rate ==3 : bonus = 10/100
        elif rate ==4 : bonus = 15/100
        elif rate ==5 : bonus = 20/100
        net = int(bonus) * int(self.__basicSalary)
        return int(self.__basicSalary) + net
    


def display_net_salary(obj):
    if obj is None : raise Exception("You have not created an employee")
    else : print("The net salary is : "+ str(obj.calculate_net_salary()))

def display_details(obj,final) : 
    if obj is None : print("A new Employee hasn't been added yet")
    print(final)


while True:
    final = [['Test', 'Salary', 'Rating', 'Net Salary']]
    idx = 0
    print("\nInventory Management System")
    print("1. Add Employee")
    print("2. Calculate Net Salary")
    print("3. Display Employee details")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        id = input("Enter Employee ID")
        name = input("Enter Employee name")
        salary = input("Enter the Basic Salary")
        rate = input("Enter the rating")
        idx  += 1
        e = Employee(id,name,salary,rate)
        temp = [idx,salary,rate,e.calculate_net_salary()]
        final.append(temp)
        print("Employee added successfully!")



    elif choice == "2":
        display_net_salary(e)
    
    elif choice == "3":
        display_details(e,final)

    elif choice == "4":
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Try again.")