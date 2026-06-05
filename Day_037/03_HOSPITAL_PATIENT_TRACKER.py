'''
======================
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2

============================================================
'''
from collections import namedtuple

n = int(input("Enter no of patient:  "))

patients = namedtuple("patients",['patient_id', 'patient_name', 'age', 'disease'])

hospital = []

for i in range(n):
   print(f"Enter patient{i+1} details:")
   id = input("Enter patient id: ")
   name = input("Enter patient name: ")
   age = input("Enter  patient age: ")
   d = input("Enter disease: ")
   hospital.append(patients(id,name,age,d))



for patient in hospital:
    print(patient.patient_id,end=' ')
    print(patient.patient_name,end=' ')
    print(patient.age,end=' ')
    print(patient.disease,end=' ')
    print()


print("\nPatients Above 60: ")
for patient in hospital:

    if  patient.age > '60':
 
        print(patient.patient_id,end=' ')
        print(patient.patient_name,end=' ')
        print(patient.age,end=' ')
        print(patient.disease,end=' ')
        print()


src = input("\nEnter patient ID: ")

for patient in hospital:

    if  patient.patient_id == src:
        print("patient Found: ")
        print(patient.patient_id,end=' ')
        print(patient.patient_name,end=' ')
        print(patient.age,end=' ')
        print(patient.disease,end=' ')
print()


count = 0
for patient in hospital:

    if patient.disease == "Diabetes":
        count += 1
        
print()
print("Patients with Diabetes: ")
print(count)



         















