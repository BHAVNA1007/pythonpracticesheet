'''
4.=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================

An institute offers fixed subjects:

Python
Java
MySQL
React
Spring Boot

These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed.
'''

n =  int(input("Enter sub how many: "))
sub = []

for i in range(n):
       sub.append(input())
fs = frozenset(sub)       

while True:
    print("Menu")
    print("1. Display Subjects")
    print("2. Search Subject")
    print("3. Count Subjects")
    print("4. Attempt to Add Subject")
    print("5. Exit")      
    
    choice = int(input("Enter a choice: "))
    
    match choice:
        case 1:
            print("Subjects: ", fs)
            
        case 2:
            s = input("Enter subject: ")
            if s in fs:
                print("subject found")
            else:             
                print("subject not found")      
        case 3:
                total = len(fs)
                print("Count Subjects",total)       
        case 4:
                print("Cannot add subject because frozenset is immutable.")
                
        case 5:
                print("Exit..................")   
                break                
                            



       

