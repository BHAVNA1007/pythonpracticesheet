'''
15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220
'''

v_t = input("Enter vehicle type: ")
h_p = int(input("Enter hours parked: "))


if v_t == 'Bike':
     fee = h_p * 10
     if h_p > 5:
         fee = fee + 100
         print(f"Total Parking Fee: {fee}")
     else:
         print(f"Total Parking Fee: {fee}")
else:
     if v_t == 'Car':
          fee = h_p * 20
          if h_p > 5:
             fee = fee + 100
             print(f"Total Parking Fee: {fee}")
          else:
             print(f"Total Parking Fee: {fee}")
     else:
         if v_t == 'Bus':
             fee = h_p * 50
             if h_p > 5:
                fee = fee + 100
                print(f"Total Parking Fee: {fee}")
             else:
                print(f"Total Parking Fee: {fee}")



        


   
     
     
    