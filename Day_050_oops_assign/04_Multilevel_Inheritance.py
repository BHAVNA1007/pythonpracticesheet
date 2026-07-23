'''
ASSIGNMENT 4: Banking Loan Management System (Multilevel Inheritance)
Scenario
A bank wants software for loan management.
Class Hierarchy
Person
     ↓
Customer
     ↓
LoanAccount
Person
Name
Age
Mobile Number
Customer
Customer ID
Account Number
LoanAccount
Loan Amount
Interest Rate
Loan Tenure
Functional Requirements
Add Customer Loan Details
Display Loan Details
Exit
Sample Input
Customer Name : Ajay Singh
Age : 36
Mobile : 9999999999

Customer ID : C101
Account Number : 100245785

Loan Amount : 500000
Interest Rate : 8.5
Loan Tenure : 5
Sample Output
----------- Loan Details -----------

Customer Name : Ajay Singh
Customer ID : C101
Account Number : 100245785

Loan Amount : ₹500000
Interest Rate : 8.5%
Loan Tenure : 5 Years
'''

class Person:

   def __init__(self, name, age, mob):

        self.name = name
        self.age = age
        self.mob = mob

   def display(self):
   
       print("Name: ", self.name)
       #print("Age: ", self.age)
       #print("Mobile No: ", self.mob)

class Customer(Person):

   def __init__(self, name, age, mob, cust_id, acc_no):

       super().__init__(name, age, mob)

       self.cust_id = cust_id
       self.acc_no = acc_no

   def cust_info(self):
  
      print("Customer Id: ", self.cust_id)
      print("Account  No: ", self.acc_no)
 
class LoanAccount(Customer):
  
   def __init__(self, name, age, mob, cust_id, acc_no, loan_amount, rate, loan_tenure):

      super().__init__(name, age, mob, cust_id, acc_no)

      self.loan_amount = loan_amount
      self.rate = rate
      self.loan_tenure = loan_tenure


   def loan_info(self):

      print("Loan Amount: ", self.loan_amount)
      print("Interest Rate: ", self.rate)
      print("Loan Tenure: ", self.loan_tenure)
   
      
cust_name = input("Customer Name: ")
age = int(input("Age: "))
mob = int(input("Mobile: "))


cust_id = input("Customer Id: ")
acc_no = int(input("Account Number: "))


loan_amount = int(input("Loan Amount: "))
rate = float(input("Interest Rate: "))
loan_tenure = int(input("Loan Tenure: "))

l = LoanAccount(cust_name, age, mob, cust_id, acc_no, loan_amount, rate, loan_tenure)

print("\n----------- Loan Details -----------\n")

l.display()
l.cust_info()
print()
l.loan_info()



