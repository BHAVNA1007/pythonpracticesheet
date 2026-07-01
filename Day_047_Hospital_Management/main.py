from patient_package.patient_module import add_patient, display_patients,search_patient

from doctor_package.doctor_module import add_doctor, display_doctors

from appointment_package.appointment_module import book_appointment, show_appointments

from billing_package.billing_module import generate_bill

def main():

    while True:
        
       print("\n*****Menu*****")
       print("\n========== Hospital Management System ==========")
       print("\n1. Add Patient")
       print("\n2. Display Patients")
       print("\n3. Search Patient")
       print("\n4. Add Doctor")
       print("\n5. Display Doctors")
       print("\n6. Book Appointment")
       print("\n7. Show Appointments")
       print("\n8. Generate Bill")
       print("\n9. Exit")
    
       choice = int(input("\nEnter choice: "))
    
       match choice:
          case 1:
            print("\n1. Add Patient")
            add_patient()
          case 2: 
            print("\n2. Display Patients")  
            display_patients()
          case 3:  
            print("\n3. Search Patient") 
            search_patient()
          case 4:
             print("\n4. Add Doctor")
             add_doctor()
          case 5:
             print("\n5. Display Doctors")
             display_doctors()
          case 6:
             print("\n6. Book Appointment")
             book_appointment()
          case 7:   
             print("\n7. Show Appointments")
             show_appointments()
          case 8:   
             print("\n8. Generate Bill")
             generate_bill()
          case 9:   
             print("\nThank you for visiting...")
             break
      
main()



