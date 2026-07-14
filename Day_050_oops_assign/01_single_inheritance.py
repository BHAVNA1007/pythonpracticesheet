'''
ASSIGNMENT 1: Hospital Management System (Single Inheritance)
Scenario
A software company has been hired to develop a Hospital Management System. Every person associated with the hospital has some common details, but each category has its own unique information.
Create a base class Person containing:
Person ID
Name
Age
Mobile Number
Create the following derived classes:
Doctor
Specialization
Experience (Years)
Consultation Fee
Nurse
Department
Shift (Day/Night)
Salary
Patient
Disease
Ward Number
Bill Amount
Functional Requirements
Create a menu-driven application.
========== Hospital Management ==========
1. Add Doctor
2. Add Nurse
3. Add Patient
4. Display Doctor Details
5. Display Nurse Details
6. Display Patient Details
7. Exit
Sample Input
Enter Choice : 1

Enter Doctor ID : 101
Enter Name : Rahul Sharma
Enter Age : 45
Enter Mobile : 9876543210
Enter Specialization : Cardiologist
Enter Experience : 18
Enter Consultation Fee : 1500
Sample Output
Doctor Added Successfully

----------- Doctor Details -----------

Doctor ID          : 101
Name               : Rahul Sharma
Age                : 45
Mobile             : 9876543210
Specialization     : Cardiologist
Experience         : 18 Years
Consultation Fee   : ₹1500
'''


class Person:

   def __init__(self, person_id, name, age, mob):
        
        self.person_id = person_id 
        self.name = name
        self.age = age
        self.mob = mob

class Doctor(Person):

   def __init__(self, person_id, name, age, mob, spec, exp, confee):

       super().__init__(person_id, name, age, mob)
 
       self.spec = spec
       self.exp = exp
       self.confee = confee

   def display(self):
       
       print("\n-----Doctors Details-----\n")
       print("Doctor id: ", self.person_id)
       print("Name : ", self.name) 
       print("Age : ", self.age)  
       print("Mobile no: ", self.mob)   
       print("Specialization : ",self.spec)
       print("Experience : ",self.exp)
       print("Consultation Fee ", self.confee)
      
  
class Nurse(Person):
   
    def __init__(self, person_id, name, age, mob, dep, shift, salary):
        
        super().__init__(person_id, name, age, mob)

        self.dep = dep
        self.shift = shift
        self.salary = salary

    def display(self):
       
       print("\n-----Nurse Details-----\n")
       print("Nurse id: ", self.person_id)
       print("Name: ", self.name) 
       print("Age: ", self.age)  
       print("Mobile no: ", self.mob)   
       print("Department: ",self.dep)
       print("Shift(Day/Night): ",self.shift)
       print("Salary ",self.salary)


class Patient(Person):
  
    def __init__(self,person_id, name, age, mob, disease, ward, bill):

        super().__init__(person_id, name, age, mob)

        self.disease = disease
        self.ward = ward
        self.bill = bill

    def display(self):
       
       print("\n-----Patient Details-----\n")
       print("Patient id: ", self.person_id)
       print("Name: ", self.name) 
       print("Age: ", self.age)  
       print("Mobile no: ", self.mob)   
       print("Disease: ",self.disease)
       print("Ward Number : ",self.ward)
       print("Bill Amount: ", self.bill)


while True:
  
     print("\n========== Hospital Management ========== \n")

     print("1. Add Doctor")
     print("2. Add Nurse")
     print("3. Add Patient")
     print("4. Display Doctor Details")
     print("5. Display Nurse Details")
     print("6. Display Patient Details")
     print("7. Exit")
 
     choice = int(input("\nEnter Choice: "))

     match choice:
   
         case 1:
              
              d_id = int(input("Enter docter id: "))
              d_name = input("Enter doctor name: ")
              d_age = int(input("Enter age: ")) 
              d_mob = int(input("Enter mob no.: "))
              d_spec = input("Enter specialization: ")
              d_exp = int(input("Enter Experience: ")) 
              d_fee = int(input("Enter consultation fee: ")) 
            
              d = Doctor(d_id, d_name, d_age, d_mob, d_spec, d_exp, d_fee)
              print("\nDoctor Added Successfully")


         case 2:
              
              n_id = int(input("Enter Nurse id: "))
              n_name = input("Enter  name: ")
              n_age = int(input("Enter age: ")) 
              n_mob = int(input("Enter mob no.: "))
              n_dep = input("Enter Department: ")
              n_shift = input("Enter shift(Day/Night): ") 
              n_salary = int(input("Enter salary: ")) 
            
              n = Nurse(n_id, n_name, n_age, n_mob, n_dep,  n_shift, n_salary)
              print("\nNurse Added Successfully")


         case 3:
              
              p_id = int(input("Enter Patient id: "))
              p_name = input("Enter  name: ")
              p_age = int(input("Enter age: ")) 
              p_mob = int(input("Enter mob no.: "))
              p_dis = input("Enter Disease: ")
              p_ward = input("Enter Ward Number: ") 
              p_bill = int(input("Enter Bill Amount: ")) 
            
              p = Patient(p_id, p_name, p_age, p_mob, p_dis,  p_ward, p_bill)
              print("\nPatient Added Successfully")              

         case 4:
              d.display()
  
         case 5:
              n.display()
 
         case 6:
              p.display()

         case 7:
              print("\nThank you for visiting... ")  
              

         case _:
              print("\nEnter valid choice: ")
              break
             

          
                    


 















