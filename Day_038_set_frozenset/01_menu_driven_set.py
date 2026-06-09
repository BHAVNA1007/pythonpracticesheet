'''
1.=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.
'''

coding_c = {2,3,4,5,6}
robotics_c = {3,5,7,8,9}

while True:
    print("*********menu***********")
    print("1. Add Student to Coding Club")  
    print("2. Add Student to Robotics Club") 
    print("3. Display Students in Coding Club") 
    print("4. Display Students in Robotics Club") 
    print("5. Find Students in Both Clubs") 
    print("6. Find Students Only in Coding Club") 
    print("7. Find Students Only in Robotics Club") 
    print("8. Display All Unique Club Members") 
    print("9. Display Total Unique Club Members") 
    print("10. Exit") 
    
    choice = int(input("Enter a choice: "))
    
    match choice:
        case 1:
            coding_c.add(10)
            print(coding_c)     

        case 2:
            robotics_c.add(1)
            print(robotics_c )   
    
        case 3:
           print(coding_c)        

        case 4:
            print(robotics_c )      

        case 5:
            print("Students in Both Clubs",robotics_c &  coding_c )   

        case 6:
            print(" Students Only in Coding Club", coding_c - robotics_c  )      

        case 7:
            print(" Students Only in Robotics Club", robotics_c  - coding_c  ) 
            
        case 8:
            print("Display All Unique Club Members", robotics_c |coding_c  )  

        case 9:
            total = len(robotics_c |coding_c )
            print("total Unique Club Members",total )            

        case 10:
            print("Thank you  for visiting...")      
            break            
            

