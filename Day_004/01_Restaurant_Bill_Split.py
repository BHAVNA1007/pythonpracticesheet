'''Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75'''



total_bill, gst, service_charge, num_friends =map(int,input().split())

print(f"Total bill amount = {total_bill}")

print(f"GST = {gst}%")

print(f"Service charge = {service_charge}%")

print(f"Number of friends = {num_friends}")


include_gst = total_bill*(gst/100)

include_service_charge =  total_bill*(service_charge/100)

final_bill = (total_bill+include_gst+include_service_charge)

print(f"Final Bill = {final_bill}")

each_pay = final_bill/num_friends 

print(f"Each Person Pays = {each_pay}" )






