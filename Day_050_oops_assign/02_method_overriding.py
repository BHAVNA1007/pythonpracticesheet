'''
ASSIGNMENT 2: Employee Payroll Management System (Method Overriding + Menu Driven)
Scenario
An IT company has three categories of employees.
Create a base class Employee.
Common Details
Employee ID
Name
Department
Derived Classes
FullTimeEmployee
Monthly Salary
Bonus
Salary Formula
Salary = Monthly Salary + Bonus
PartTimeEmployee
Hourly Rate
Total Hours Worked
Salary Formula
Salary = Hourly Rate × Hours
ContractEmployee
Project Name
Contract Amount
Salary Formula
Salary = Contract Amount
Functional Requirements
========== Payroll System ==========

1. Add Full Time Employee
2. Add Part Time Employee
3. Add Contract Employee
4. Display Full Time Salary
5. Display Part Time Salary
6. Display Contract Salary
7. Exit
Sample Input
Choice : 2

Employee ID : 205
Name : Aman Verma
Department : Testing

Hourly Rate : 350
Hours Worked : 160
Sample Output
Employee Added Successfully

Employee ID : 205
Name : Aman Verma
Department : Testing

Hourly Rate : 350
Hours Worked : 160

Total Salary : ₹56000
'''

class Employee:

    def __init__(self, emp_id, name, dep):

        self.emp_id = emp_id
        self.name = name
        self.dep = dep

    def display(self):
     
        print("Employee ID: ", self.emp_id) 
        print("Name: ", self.name)
        print("Department: ", self.dep) 

    def salary(self):
        pass

    
class FullTimeEmployee(Employee):

    def __init__(self, emp_id,  name, dep, m_salary, bonus):
    
        super().__init__(emp_id, name, dep)
        self.m_salary = m_salary
        self.bonus = bonus



    def salary(self):
     
        print("Monthly Salary: ", self.m_salary) 
        print("Bonus: ", self.bonus)    
       
        self.salary = self.m_salary + self.bonus
        print("Total Salary: ", self.salary )

class PartTimeEmployee(Employee):

    def __init__(self, emp_id, name, dep, h_rate, t_h_w):

        super().__init__(emp_id, name, dep)
        self.h_rate = h_rate
        self.t_h_w = t_h_w


    def salary(self):
     
        print("Hourly Rate: ", self.h_rate) 
        print("Hours Worked: ", self.t_h_w)    

        self.salary = self.h_rate * self.t_h_w
        print("Total Salary: ", self.salary )



class ContractEmployee(Employee):

    def __init__(self, emp_id, name, dep, project_name, contract_amount):

        super().__init__(emp_id, name, dep)
        self.project_name = project_name
        self.contract_amount = contract_amount


    def salary(self):
     
        print("Project Name: ", self.project_name) 
        print("Contract Amount: ", self.contract_amount)    
 
        print("Total Salary: ", self.contract_amount)
    

f = None
p = None
c = None

while True:

     print("\n========== Payroll System ==========\n")

     print("1. Add Full Time Employee")
     print("2. Add Part Time Employee")
     print("3. Add Contract Employee")
     print("4. Display Full Time Salary")
     print("5. Display Part Time Salary")
     print("6. Display Contract Salary")
     print("7. Exit")

     choice = int(input("\nEnter choice: "))

     match choice:
  
         case 1:
               id = int(input("Enter id: "))
               name = input("Enter name: ")
               dep = input("Enter Department: ")

               m_s = int(input("Enter monthly salary: "))
               bonus = int(input("Enter Bonus: "))
               
               f =FullTimeEmployee(id, name, dep, m_s, bonus) 
                
               print("\nEmployee Added Successfilly")

         case 2:
               id = int(input("Enter id: "))
               name = input("Enter name: ")
               dep = input("Enter Department: ")

               h_r = int(input("Enter Hourly Rate: "))
               h_w = int(input("Enter Hourse Worked: "))

               p =PartTimeEmployee(id, name, dep, h_r, h_w)

               print("\nEmployee Added Successfully")


         case 3:
               id = int(input("Enter id: "))
               name = input("Enter name: ")
               dep = input("Enter Department: ")

               p_n = input("Enter Project Name: ")
               c_a = int(input("Enter Contract Amount: "))
               
               c = ContractEmployee(id, name, dep, p_n, c_a)
               print("\nContract Employee Added Successfully")

         case 4:
              
               if f:
                   f.display()
                   f.salary()
               else:
                   print("No fulltime emp exits ...")  

         case 5:
               
               if p:
                   p.display()
                   p.salary() 
               else:
                   print("No parttime emp exits...") 

         case 6:
              
              if c:
                  c.display()
                  c.salary() 
              else:
                   print("No parttime emp exits...") 
  
         case 7:

               print("Exit........")

               break   
   
       
              
