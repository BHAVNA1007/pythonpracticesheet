'''
2.=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.
'''
python_c = set()
java_c = set()
while True:
    print("\n*********menu***********\n")
    print("1. Enroll Student in Python")  
    print("2. Enroll Student in Java") 
    print("3. Display Python Students") 
    print("4. Display Java Students") 
    print("5. Find Students Enrolled in Both Courses")
    print("6. Find Students Enrolled Only in Python")
    print("7. Find Students Enrolled Only in Java")
    print("8. Check Enrollment in Python Course")
    print("9. Display Total Unique Students") 
    print("10. Exit") 
    
    choice = int(input("\nEnter a choice: "))
    
    match choice:
        case 1:
            n = int(input("\nEnter number of student in python: "))
            
            for i in range(n):
                python_c.add(input(f"Enter Email id of python students {i+1}: "))
            #print(python_c)        

        case 2:
            n = int(input("\nEnter number of student in java: "))
            
            for i in range(n):
                java_c.add(input(f"Enter Email id of java students {i+1}: "))
            #print(java_c)    
        case 3:
            print("\nDisplay Python Students: ")
            for i in python_c:
                print(i,end=' ')
                print() 
            
        case 4:
            print("\nDisplay Java Students: ")
            for i in java_c:
                print(i,end=' ')  
                print()   
            
        case 5:
            print("\n5. Find Students Enrolled in Both Courses: ") 
            for i in python_c.intersection(java_c):
                print(i,end=' ') 
                print()
            
        case 6:   
            print("\n6. Find Students Enrolled Only in Python:")
            for i in python_c.difference(java_c):
                print(i, end=' ')
                print()

        case 7:            
            print("\n7. Find Students Enrolled Only in Java")
            for i in java_c.difference(python_c):
                print(i,end=' ')
                print()
            
        case 8:    
            stu = input("\nEnter student email id: ")
            if stu in python_c:
                print("\nstudent alredy enrolled")
            else:
                print("\nstudent not enrolled:")    
            
        case 9:    
            print("\n9.Total Unique Students are: ") 
            print(len(java_c.union(python_c)))
            
        case 10:
            print("Thank you !!!!!!!!!!!!!!!!!!")            
            break

        case _:
            print("\ninvalid choice: ")
     

  

