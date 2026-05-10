'''8.
 ATM Note Counter

A bank ATM dispenses ₹100 notes.

Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700

Output:
Notes = 7
'''

'''
amount = int(input('Enter a number = '))

notes = 0 

while amount >= 100 :
    
    amount = amount - 100
    
    notes += 1
     
print(notes)

'''

amount = int(input("Enter amount = "))

count = 0

while amount >= 100:

    amount = amount - 100
    count += 1

s = ''

for notes in str(count):
     s += notes
print("Notes = ", s)
    

    
    