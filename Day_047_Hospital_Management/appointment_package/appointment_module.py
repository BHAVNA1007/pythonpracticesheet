from datetime import datetime

appointments = []

def book_appointment():
    print("appointment info...")
    a_id = int(input("Enter appointment id: "))
    p_id = int(input("Enter patient id: "))
    d_id = int(input("Enter Doctor id: "))
    a_date = datetime.strptime(
        input("Enter Date(dd-mm-yyyy): "),
        "%d-%m-%Y"
    ).date()
    a_time = datetime.strptime(
        input("Enter time (H:M): "),
        "%H:%M"
    ).time()

    appointment = {
       "Appointment ID": a_id,
       "Patient ID":p_id,
       "Doctor ID":d_id,
       "Appointment Date": a_date,
       "Appointment Time": a_time
    }

    appointments.append(appointment)


def show_appointments():
    for appointment in appointments:
        for k, v in appointment.items():
            print(k, ":", v)
        print()    

