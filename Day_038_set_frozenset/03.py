'''
3.=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations.
'''

n = int(input("Enter number of visitors: "))
v_id = set()
for i in range(n):
    v_id.add(int(input(f"visitor id {i+1}: ")))
print(v_id)        

while True:
     
    print("Menu") 
    print("1. Add Visitor") 
    print("2. Remove Visitor") 
    print("3. Check Visitor") 
    print("4. Display All Visitors") 
    print("5. Count Unique Visitors") 
    print("6. Clear Visitor Data") 
    print("7. Exit") 
   
    choice = int(input("Enter a choice: "))
    
    match choice:
        case 1:
                v_id.add(int(input("Add Visitor: ")))     
                print(v_id)
                
        case 2:
                v_id.discard(int(input(" Remove Visitor: ")))     
                print(v_id)        
                
        case 3:
                id = int(input("Enter id: "))
                if id in v_id :
                        print("visitor found")
                else:
                        print("visitor not found")
        case 4:
                for visitor in v_id:
                    print(visitor,end=" ")
                print()                    

        case 5:
                unique = len(v_id)
                print("Count Unique Visitors",unique)       

        case 6:
                print("Clear Visitor Data: ") 
                v_id.clear()        
                print(v_id)

        case 7:
                print("Exit..................")             
                break                
                           