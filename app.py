import mysql.connector

# Name: Rory Stiff
# Project: Employee Managment system using mysql database

# Define Employee class
class Employee:
    
    
     # mysql Database connection

    con = mysql.connector.connect(
            host ="localhost",
            user="root",
            password="thsrocks",
            database="employee"
            
        )


    cursor = con.cursor()
    
    
    
     # Method to check if an employee exists
    def check_employee(self, emp_id):
        query = "SELECT * FROM employees WHERE id = %s"
        Employee.cursor.execute(query, (emp_id,))
        result = Employee.cursor.fetchone()
        return result is not None

    # Method to add an employee
    def add_employee(self):
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        department = input("Enter employee department: ")
        position = input("Enter employee position: ")
        salary = float(input("Enter employee salary: "))

        query = "INSERT INTO employees (name, age, department, position, salary) VALUES (%s, %s, %s, %s, %s)"
        Employee.cursor.execute(query, (name, age, department, position, salary))
        Employee.con.commit()
        print("Employee added successfully!")

    # Method to remove an employee
    def remove_employee(self):
        emp_id = int(input("Enter employee ID to remove: "))
        if self.check_employee(emp_id):
            query = "DELETE FROM employees WHERE id = %s"
            Employee.cursor.execute(query, (emp_id,))
            Employee.con.commit()
            print("Employee removed successfully!")
        else:
            print("Employee not found!")

    # Method to display an employee
    def display_employee(self):
        emp_id = int(input("Enter employee ID to display: "))
        if self.check_employee(emp_id):
            query = "SELECT * FROM employees WHERE id = %s"
            Employee.cursor.execute(query, (emp_id,))
            result = Employee.cursor.fetchone()
            
            print(f"ID: {result[0]}, Name: {result[1]}, Age: {result[2]}, Department: {result[3]}, Position: {result[4]}, Salary: {result[5]}")
        else:
            print("Employee not found!")

    # Method to display all employees
    def display_employees(self):
        query = "SELECT * FROM employees"
        Employee.cursor.execute(query)
        results = Employee.cursor.fetchall()
        for row in results:
             print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}, Position: {row[4]}, Salary: {row[5]}")

    # Method to exit the program
    def exit(self):
        Employee.con.close()
        print("Connection closed. Exiting program...")
        exit()

    
      
# Main function to run the program
def main():
    emp = Employee()
    while True:
        print("\nWelcome to the Employee management record system")
        print('--------------------------------------------------')
        print('Please select one of the following options:')
        print("1). Add Employee")
        print("2). Remove Employee")
        print("3). Display Employee")
        print("4). Display All Employees")
        print("5). Exit\n")
        
        choice = input("Enter your choice: ")
     
        
        if choice == '1':
            emp.add_employee()
        elif choice == '2':
            emp.remove_employee()
        elif choice == '3':
            emp.display_employee()
        elif choice == '4':
            emp.display_employees()
        elif choice == '5':
            emp.exit()
        else:
            print("Invalid choice. Please select a valid option.")
            
if __name__ == "__main__":
    main()