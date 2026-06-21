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

coding_c =  set()
robotics_c = set()

while True:
    print("\n*********menu***********\n")
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
    
    choice = int(input("\nEnter a choice: "))
    
    match choice:
        case 1:
            n = int(input("\nNumber of students in coding club: "))
            for i in range(n):
                coding_c.add(input(f"Enter id c_c {i+1}: "))  

        case 2:
            n = int(input("\nNumber of students in robotics club: "))
            for i in range(n):
                robotics_c.add(input(f"Enter id r_c {i+1}: "))  
 
        case 3:
           print("\nstudents in coding club are: ")
           for i in coding_c:
               print(i,end=' ')
        case 4:
            print("\nstudents in robotics club are: ")
            for i in robotics_c:
                print(i,end=' ')      

        case 5:
            print("\nStudents in Both Clubs are: " )   
            for i in coding_c.intersection(robotics_c):
                print(i,end=' ')

        case 6:
            print("\nStudents Only in Coding Club are:" )
            for i in coding_c.difference(robotics_c):
                print(i,end=' ')      

        case 7:
            print("\nStudents Only in Robotics Club are:")
            for i in robotics_c.difference(coding_c):
                print(i,end=' ') 
            
        case 8:
            print("\nDisplay All Unique Club Members are:")
            for i in robotics_c.union(coding_c):
                print(i,end=' ')  

        case 9:
            print("\nall unique club members are: ")
            print(len(robotics_c.union(coding_c)))            

        case 10:
            print("Thank you  for visiting...")      
            break
        case _:
            print("\ninvalid choice")            
            

