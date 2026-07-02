'''
Question 5: Hotel Room Booking System
Scenario

A hotel wants to generate the final bill of guests based on the duration of their stay.

Requirements

Create a class named Guest with:

guest_id
guest_name
number_of_days
room_charge_per_day

Initialize the values using a constructor.

Calculations
Room Bill = Number of Days × Room Charge Per Day
GST = 12% of Room Bill
Final Bill = Room Bill + GST
Sample Input
Enter Guest ID : G101
Enter Guest Name : Rohan Mehta
Enter Number of Days : 4
Enter Room Charge Per Day : 2500
Sample Output
------ Hotel Bill ------
Guest ID              : G101
Guest Name            : Rohan Mehta
Number of Days        : 4
Room Charge Per Day   : ₹2500.0
Room Bill             : ₹10000.0
GST (12%)             : ₹1200.0
Final Bill            : ₹11200.0

'''

class Guest:

    def __init__(self, guest_id, guest_name, number_of_days, room_charge_per_day):
 
        self.id = guest_id
        self.name = guest_name
        self.days = number_of_days
        self.charge = room_charge_per_day

        self.room_bill = self.days * self.charge
       
        self.gst = self.room_bill * 0.12

        self.final_bill = self.room_bill + self.gst

def main():

    guest_id = input("Enter Guest ID :")
    guest_name = input("Enter Guest Name :")
    number_of_days = int(input("Enter Number of Days :"))
    room_charge_per_day = float(input("Enter Room Charge Per Day :"))

    g = Guest(guest_id, guest_name, number_of_days, room_charge_per_day)
    
    print("\n------ Hotel Bill ------\n")
  
    print("Guest ID              :", g.id)
    print("Guest Name            :", g.name)
    print("Number of Days        :", g.days)
    print("Room Charge Per Day   :", g.charge)
    print("Room Bill             :", g.room_bill)
    print("GST (12%)             :", g.gst)
    print("Final Bill            :", g.final_bill)

main()

         


