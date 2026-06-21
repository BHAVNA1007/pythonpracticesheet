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

sub = frozenset({"python","java","mysql","react","spring boot"})

while True:
    print("\nMenu:\n")
    print("1. Display Subjects")
    print("2. Search Subject")
    print("3. Count Subjects")
    print("4. Attempt to Add Subject")
    print("5. Exit")      
    
    choice = int(input("Enter a choice: "))
    
    match choice:
        case 1:
            print("\nSubjects are: ")
            for i in sub:
               print(i,end=" ")  
            
        case 2:
            s = input("\nEnter subject name for search: ")
            if s in sub:
                print("\nsubject found")
            else:             
                print("\nsubject not found")      
        case 3:
                total = len(sub)
                print("Count Subjects",total)       
        case 4:
                s = input("Enter subject to add: ")
                sub.add(s) #frozenset has no attribut add error throw
                
        case 5:
                print("Exit..................")   
                break    
        case _:
               print("\ninvalid choice:")             
                            



       

