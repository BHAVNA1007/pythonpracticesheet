'''
2.Hospital Management System – Oldest Patient

A hospital wants to give priority to the oldest patient during a free health check-up camp. The patient details are stored as tuples containing the patient's name and age.

As a Python developer, write a program to identify the oldest patient using the reduce() function with a lambda expression.

Input
patients = [
    ("Rahul", 45),
    ("Sneha", 62),
    ("Amit", 38),
    ("Kiran", 71),
    ("Pooja", 55)
]
Expected Output
Oldest Patient: Kiran
'''
from functools import reduce
n = int(input("Enter n: "))

patients = []

for i in range(n):
   name = input(f"Enter name of patient{i+1}: ")
   age = int(input(f"Enter age of patient{i+1}: "))
   p_info = (name, age)
   patients.append(p_info)
print(patients)

res = reduce(lambda x,y: x if x[1]>y[1] else y,patients)
   
print("Oldest Patient:", res[0]) 


