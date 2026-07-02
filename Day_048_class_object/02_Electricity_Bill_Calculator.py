'''
Question 2: Electricity Bill Calculator
Scenario


An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0
'''


class Customer:

    def __init__(self, customer_id, customer_name, units_consumed):

        self.id = customer_id
        self.name = customer_name
        self.units = units_consumed
        self.Total_Bill =  (self.units * 8) + 150

def main():
     
     customer_id = input("Enter Customer ID :")
     customer_name = input("Enter Customer Name :") 
     units_consumed = float(input("Enter Units Consumed :"))

     c = Customer(customer_id, customer_name, units_consumed)
     
     print("\n------ Electricity Bill ------\n")
     print("\nCustomer ID       :", c.id)
     print("Customer Name     :", c.name)
     print("Units Consumed    :", c.units) 
     print("Total Bill Amount :", c.Total_Bill)

main()
