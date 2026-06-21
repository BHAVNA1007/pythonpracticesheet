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


visitor = set()

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
                n = int(input("\nEnter number of visitors:"))
                for i in range(n):
                   visitor.add(int(input("Add Visitor: ")))    
                
        case 2:
                v_id = int(input("\nEnter visitor id to remove visitor:"))
                if v_id in visitor:     
                    visitor.remove(v_id)  
                    print(f"\nvisitore with id {v_id} removed succesfully:")
                else:
                    print(f"\nvisitor with id {v_id} not available: ")            
                
        case 3:
                v_id = int(input("\nEnter id for search: "))
                if v_id in visitor:
                        print("visitor found")
                else:
                        print("visitor not found")
        case 4:
                print("\nAll visitors: ")
                for v in visitor:
                    print(v,end=" ")
                print()                    

        case 5:
                unique = len(visitor)
                print("\nCount Unique Visitors",unique)       

        case 6:
                print("\nClear Visitor Data: ") 
                visitor.clear()        
                print(visitor)

        case 7:
                print("\nExit..................")             
                break                
                           