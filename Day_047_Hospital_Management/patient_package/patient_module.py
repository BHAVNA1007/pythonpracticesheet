
patients = []
def add_patient():
    print("\npatient info..")
    p_id =int(input("Enter patient id: "))
    p_name =input("Enter name: ")
    p_age = int(input("Enter Age: "))
    p_g = input("Enter gender: ")
    p_dis = input("Enter Disease: ")
    p_mob = int(input("Enter Mobile Number: "))
    patient = {
        "id":p_id,
        "name":p_name,
        "age" : p_age,
        "Gender" : p_g,
        "Disease": p_dis,
        "Mobile Number": p_mob

    }
    patients.append(patient)
      
    print("Patient added...")   

def  display_patients(): 
   for patient in patients:   
       for k, v in patient.items():
          print(k ,":", v) 
       print()  

def  search_patient():
    p_id = int(input("Enter id: "))
    for patient in patients:
        if patient["id"] == p_id:
        
           for k,v in patient.items():
               print(k,":",v)
           return  
    print("patient not found...")     

 
    