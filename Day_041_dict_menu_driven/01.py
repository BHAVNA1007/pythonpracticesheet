'''
1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

Accept the following information from the user:

Patient ID
Patient Name
Age
Gender
Disease
Doctor Name

Store the record in the nested dictionary.

Validation:
If the Patient ID already exists, display:

Patient ID already exists.

2. Search Patient

Accept Patient ID from the user.

If the patient exists, display complete information.

Sample Output

Patient ID : 101
Name       : Ajay
Age        : 35
Gender     : Male
Disease    : Fever
Doctor     : Dr. Sharma

If Patient ID is not found:

Patient Record Not Found

3. Update Patient Disease

Accept Patient ID.

If found:

Ask for new disease.
Update the disease information.

Sample Output

Disease Updated Successfully
4. Delete Patient Record

Accept Patient ID.

If found:

Remove the patient record.

Sample Output

Patient Record Deleted Successfully

Otherwise:

Patient Not Found
5. Display All Patients

Display all patient records in a formatted manner.

Sample Output

--------------------------------
Patient ID : 101
Name       : Ajay
Age        : 35
Disease    : Fever
Doctor     : Dr. Sharma
--------------------------------

Patient ID : 102
Name       : Ravi
Age        : 42
Disease    : Diabetes
Doctor     : Dr. Gupta
6. Count Total Patients

Display the total number of patients currently stored.

Sample Output

Total Patients : 25
7. Display Patients By Disease

Accept a disease name from the user.

Display all patients suffering from that disease.

Sample Output

Enter Disease : Fever

101  Ajay
108  Aman
115  Neha

If no patient is found:

No Patient Found
8. Display Oldest Patient

Find and display the patient having the highest age.

Sample Output

Oldest Patient Details

Patient ID : 110
Name       : Ravi
Age        : 68
Disease    : Diabetes
Doctor     : Dr. Gupta
9. Display Youngest Patient

Find and display the patient having the minimum age.

Sample Output

Youngest Patient Details

Patient ID : 121
Name       : Riya
Age        : 4
Disease    : Viral Fever
Doctor     : Dr. Mehta
10. Exit

Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System
'''


n = int(input("Enter num of patient: "))
patient = {}

for i in range(n):
    p_id = int(input("patient id: "))
   
    name = input("name: ")
    age = int(input("age: "))
    gender = input("gender: ")
    disease = input("disease: ")
    doctor = input("doctor: ")
    patient[p_id]    = {
       "name": name,
       "age": age,
       "gender": gender,
       "disease":  disease,
       "doctor": doctor
    }
print(patient)

while True:
    print(" HOSPITAL PATIENT MANAGEMENT SYSTEM")
    print("1. Add New Patient")
    print("2. Search Patient")
    print("3. Update Patient Disease")
    print("4. Delete Patient Record")
    print("5. Display All Patients")
    print("6. Count Total Patients")
    print("7. Display Patients By Disease")
    print("8. Display Oldest Patient")
    print("9. Display Youngest Patient")
    print("10. Exit")
    
    choice = int(input("Enter choice: "))
    
    match choice:
        case 1:
            p_id = int(input("patient id: "))
            if p_id in patient:
                print("Patient ID already exists.")
            else:
                name = input("name: ")
                age = int(input("age: "))
                gender = input("gender: ")
                disease = input("disease: ")
                doctor = input("doctor: ")
                patient[p_id]    = {
                     "name": name,
                     "age": age,
                     "gender": gender,
                     "disease":  disease,
                     "doctor": doctor
                }
                print("New Patient added successfully:  ",patient)  
        case 2:
            src = int(input("Enter id: "))
            if src in patient:
                print(" Patient found successfully:  ") 
                print("p_id: ", src)    
                for k, v in patient[src].items():
                    print(k, ":", v)
                
            else:    
                print("Patient Record Not Found:  ")      
                
        case 3:
            p_id = int(input("Enter id: "))
            if p_id in patient:
                new_d = input(" enter  disease:  ")    
                patient[p_id]["disease"] = new_d
                print("disease updated successfully: ",)
                print("p_id: ", p_id)    
                for k, v in patient[p_id].items():
                    print(k, ":", v)
            else:    
                print("Patient Record Not Found:  ")      

        case 4:
            p_id = int(input("Enter id: "))
            if p_id in patient:
                
                del patient[p_id]
                print("Patient Record deleted successfully: ",)
                print(patient)  
            else:    
                print("Patient Record Not Found:  ")            
        

        case 5:
            print("All Patient Records")

            for p_id, details in patient.items():
                print("--------------------------")
                print("Patient ID:", p_id)

                for k, v in details.items():
                    print(f"{k}: {v}")

            print("--------------------------")  
        case 6:
            print("All Patient Count: ")
            count = 0 
            for p_id, details in patient.items():
                count += 1
            print("count = ", count)  
                
        case 7:
            disease = input("Enter disease: ")
            f = False
            for p_id, d in patient.items():
                if    d["disease"] == disease:
                    f = True    
                    print(p_id, d["name"])    
                
            if not f:    
                print("Patient Record Not Found:  ")      
                
        case 8:
            old_a = 0
            o_id =None
   
            for p_id, o in patient.items():
                if o["age"]> old_a:
                    old_a = o["age"]
                    o_id = p_id
            print("Oldest Patient: ")
            print("Patient Id: ", o_id)
            
            for k, v in patient[o_id].items():
                print(k,":",v)
                
        case 9:
            young_a = float('inf')
            young_id =None
   
            for p_id, y in patient.items():
                if y["age"]< young_a:
                    young_a = y["age"]
                    young_id = p_id
            print("Oldest Patient: ")
            print("Patient Id: ", young_id)
            
            for k, v in patient[young_id].items():
                print(k,":",v)
              
        case 10:
            print("Thank You For Using Hospital Patient Management System")
            break       
            


