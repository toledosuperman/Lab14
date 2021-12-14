#function to create and check ID
def employeeID():
    while True:
        myid = input("Enter employee ID: ")
        
        if myid == "":
            print("Employee ID cannot be empty.")
        elif len(myid) > 7:
            print("Employee ID needs to be less than 8 digits.")
        elif myid.isdigit():
            break
        else:
            print("The employee ID has non numeric characters. Enter again")
    return myid

#function to create and check name
def employeename():
    while True:
        name = input("Enter employee name: ")

        if name.strip() == "":
            print("Employee name can not be empty.")
        elif name.lower().replace("-", "").replace("'", "").replace(" ", "").isalpha():
            break
        else:
            print("Enter correct employee name.")  
    return name

#function to create and check email
def employeeemail():
    while True:
        email = input("Enter employee email: ")
        
        if len(set("!\"'#$%^&*()= +,<>/?;:[]{}\\").intersection(set(email))) > 0:
            print("Do not use any of these characters: ! \" ' # $ % ^ & * ( ) = + , < > / ? ; : [ ] { } \\. Try again.")
        elif email.strip().replace("@", "").replace(".", "").replace("_", "").isalnum():
            break
        else:
            print("Try again.")
    return email

#function to create and check street address
def employeeaddress():
    while True:
        address=input("Enter employee street address: ")
        if len(set("!\"'$%^&*= +_<>?;:[]{}").intersection(set(email))) > 0:
            print("Do not use any of these characters: ! \" ' $ % ^ & * = + _ < > ? ; : [ ] { }. Try again.")
        elif email.strip().replace("@", "").replace(".", "").replace("_", "").isalnum():
            break
        else:
            print("Try again.")
    return address

#function to create and check salary      
def employeesalary():
    while True:
        salary = float(input("Enter salary: "))
        try:
            if salary < 18 or salary > 27:
                print("Salary should be between 18 and 27.")
            else:
                break
        except:
            print("Salary is in an invalid format.")
            
    return salary

#drive program to create list and prompt for info
employees = list()
while True:
    myid = employeeID()
    name = employeename()
    email = employeeemail()
    address = employeeaddress()
    salary = employeesalary()
    
    employee = {
        "Id: ": myid,
        "Name: ": name,
        "Email: ": email,
        "Address: ": address,
        "Salary: ": salary
    }
    
    employees.append(employee)
    
#method to quit program  
    quit = input("Do you want to quit? Y/N ").lower()
    if quit == "y":
        break
    
#add IT to name and increase salary
for employee in employees:
    employee["Name: "] = employee["Name: "] + " IT Department"
    employee["Salary: "] = employee["Salary: "] * 1.3
    
#print list   
print(employees)
