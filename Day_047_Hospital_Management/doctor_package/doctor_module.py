
doctors = []

def  add_doctor():
    print("\nDoctors info....")
    d_id = int(input("Enter id: "))
    d_name = input("Enter Name: ")
    s = input("Enter Specialization: ")
    exp = int(input("Enter exp: "))
    fee = int(input("Enter Consultation Fees: "))

    doctor = {
       "Doctor ID" : d_id,
       "Doctor Name": d_name,
       "Specialization": s,
       "Experience": exp,
       "Consultation Fees": fee
    }
    doctors.append(doctor)

def display_doctors():
    for doctor in doctors:
        for k, v in doctor.items():
            print(k, ":", v)
        print()
    