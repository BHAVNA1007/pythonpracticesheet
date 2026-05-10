'''10.Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700
'''
num = int(input("Enter The Number = "))
h1 = int(input("Enter The units used by house1 = "))
h2 = int(input("Enter The units used by house2 = "))
h3 = int(input("Enter The units used by house3 = "))



if h1 < 50:
    bill = h1 * 5
    print("House 1 Bill = ", bill - 100)
elif h1 <= 100 :
    bill = h1 * 5
    print("House 1 Bill = ", bill)
elif h1 > 100 and h1 <= 200:
    bill = (100 * 5) +( (h1 - 100)*7)
    print("House 1 Bill = ", bill)
else:
    bill = (100*5) + (100*7)+ ((h1 - 200)* 10)
    print("House 1 Bill = ", bill)


if h2 < 50:
    bill2 = h2 * 5
    print("House 2 Bill = ", bill2 - 100)

elif h2 <= 100 :
    bill2 = h2 * 5
    print("House 2 Bill = ", bill2)
elif h2 > 100 and h2 <= 200:
    bill2 = (100 * 5) +( (h2 - 100)*7)
    print("House 2 Bill = ", bill2) 
else:
    bill2 = (100*5) + (100*7)+ ((h2 - 200)* 10)
    print("House 2 Bill = ", bill2)


if h3 < 50:
    bill3 = h3 * 5
    print("House 3 Bill = ", bill3 - 100)

elif h3 <= 100 :
    bill3 = h3 * 5
    print("House 3 Bill = ", bill3)
elif h3 > 100 and h3 <= 200:
    bill3 = (100 * 5) +( (h3 - 100)*7)
    print("House 3 Bill = ", bill3) 
else:
    bill3 = (100*5) + (100*7)+ ((h3- 200)* 10)
    print("House 3 Bill = ", bill3) 

t_collection =  bill + bill2 + bill3
print("Total Collection = ", t_collection )


if bill > bill2:
    if bill > bill3:
        print("Highest Bill = ", bill)
    else:
        if bill2 > bill3:
            print("Highest Bill = ",bill2)
        else:
            print("Highest Bill = ",bill3)
else:
    if bill2 > bill3:
        print("Highest Bill = ",bill2)
    else:
        print("Highest Bill = ",bill3)






