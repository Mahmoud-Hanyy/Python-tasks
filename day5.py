#Question1
import sqlite3
class Employee:
    all_employees = []
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            department TEXT,
            salary REAL
        )
    """)
    conn.commit()

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.all_employees.append(self)

        Employee.cursor.execute("""
            INSERT INTO employee (first_name, last_name, age, department, salary)
            VALUES (?, ?, ?, ?, ?)
        """, (self.first_name, self.last_name, self.age, self.department, self.salary))
        Employee.conn.commit()

        self.id = Employee.cursor.lastrowid

    def transfer(self, new_department):
        self.department = new_department
        Employee.cursor.execute("""
            UPDATE employee SET department = ? WHERE id = ?
        """, (self.department, self.id))
        Employee.conn.commit()

    def fire(self):
        Employee.all_employees = [emp for emp in Employee.all_employees if emp != self]
        Employee.cursor.execute("DELETE FROM employee WHERE id = ?", (self.id,))
        Employee.conn.commit()

    def show(self):
        print(f"ID: {self.id} | Name: {self.first_name} {self.last_name} | Age: {self.age} | "
              f"Department: {self.department} | Salary: {self.salary}")

    @staticmethod
    def list_employees():
        Employee.cursor.execute("SELECT * FROM employee")
        rows = Employee.cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | Age: {row[3]} | Department: {row[4]} | Salary: {row[5]}")

    def __del__(self):
        Employee.conn.close()


#Question2
class Employee:
    all_employees = []

    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            department TEXT,
            salary REAL,
            is_manager INTEGER,
            managed_department TEXT
        )
    """)
    conn.commit()

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        self.is_manager = False
        self.managed_department = None

        Employee.all_employees.append(self)

        Employee.cursor.execute("""
            INSERT INTO employee (first_name, last_name, age, department, salary, is_manager, managed_department)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (self.first_name, self.last_name, self.age, self.department, self.salary, 0, None))
        Employee.conn.commit()

        self.id = Employee.cursor.lastrowid

    def transfer(self, new_department):
        self.department = new_department
        Employee.cursor.execute("""
            UPDATE employee SET department = ? WHERE id = ?
        """, (self.department, self.id))
        Employee.conn.commit()

    def fire(self):
        Employee.all_employees = [emp for emp in Employee.all_employees if emp != self]
        Employee.cursor.execute("DELETE FROM employee WHERE id = ?", (self.id,))
        Employee.conn.commit()

    def show(self):
        print(f"ID: {self.id} | Name: {self.first_name} {self.last_name} | Age: {self.age} | "
              f"Department: {self.department} | Salary: {self.salary}")

    @staticmethod
    def list_employees():
        Employee.cursor.execute("SELECT * FROM employee")
        rows = Employee.cursor.fetchall()
        for row in rows:
            if row[6]:  # is_manager
                salary_display = "Confidential"
                managed_dept = row[7]
                print(f"[Manager] ID: {row[0]} | Name: {row[1]} {row[2]} | Age: {row[3]} | Department: {row[4]} | "
                      f"Salary: {salary_display} | Manages: {managed_dept}")
            else:
                print(f"[Employee] ID: {row[0]} | Name: {row[1]} {row[2]} | Age: {row[3]} | Department: {row[4]} | "
                      f"Salary: {row[5]}")

class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.is_manager = True
        self.managed_department = managed_department

        Employee.cursor.execute("""
            UPDATE employee SET is_manager = ?, managed_department = ? WHERE id = ?
        """, (1, self.managed_department, self.id))
        Employee.conn.commit()

    def show(self):
        print(f"ID: {self.id} | Name: {self.first_name} {self.last_name} | Age: {self.age} | "
              f"Department: {self.department} | Salary: Confidential | Manages: {self.managed_department}")

def main():
    while True:
        print("\n========= Employee Management System =========")
        print("add  - Add new employee/manager")
        print("list - List all employees")
        print("tran - Transfer an employee")
        print("fire - Fire an employee")
        print("q    - Quit")
        choice = input("Enter command: ").strip().lower()

        if choice == "add":
            emp_type = input("Is this a manager (m) or employee (e)? ").strip().lower()
            fname = input("First Name: ")
            lname = input("Last Name: ")
            age = int(input("Age: "))
            dept = input("Department: ")
            salary = float(input("Salary: "))

            if emp_type == "m":
                managed_dept = input("Managed Department: ")
                Manager(fname, lname, age, dept, salary, managed_dept)
                print("✅ Manager added.")
            else:
                Employee(fname, lname, age, dept, salary)
                print("✅ Employee added.")

        elif choice == "list":
            Employee.list_employees()

        elif choice == "tran":
            eid = int(input("Enter Employee ID to transfer: "))
            new_dept = input("Enter new department: ")
            emp = next((e for e in Employee.all_employees if e.id == eid), None)
            if emp:
                emp.transfer(new_dept)
                print("✅ Department updated.")
            else:
                print("❌ Employee not found.")

        elif choice == "fire":
            eid = int(input("Enter Employee ID to fire: "))
            emp = next((e for e in Employee.all_employees if e.id == eid), None)
            if emp:
                emp.fire()
                print("✅ Employee fired.")
            else:
                print("❌ Employee not found.")

        elif choice == "q":
            print("👋 Exiting...")
            break

        else:
            print("❗ Unknown command. Try again.")

if __name__ == "__main__":
    main()
