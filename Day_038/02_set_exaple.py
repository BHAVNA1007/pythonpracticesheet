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

while True:
    print("*********menu***********")
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
    
    choice = int(input("Enter a choice: "))
    
    match choice:
        case 1:
            n = int(input("Enter number of student in python: "))
            p_s = set()
            for i in range(n):
                 p_s.add(input(f"Email student {i+1}: "))
            print(p_s)        

        case 2:
            n = int(input("Enter number of student in java: "))
            j_s = set()
            for i in range(n):
                j_s.add(input(f"Email student {i+1}: "))
            print(j_s)    
        case 3:
            print("Display Python Students: ", p_s) 
            
        case 4:
            print("Display Java Students: ", j_s)     
            
        case 5:
            print("5. Find Students Enrolled in Both Courses: ",p_s & j_s)  
            
        case 6:   
            print("6. Find Students Enrolled Only in Python", p_s - j_s)

        case 7:            
            print("7. Find Students Enrolled Only in Java",  j_s - p_s )
            
        case 8:    
            in_python = len(p_s )
            print("8. Check Enrollment in Python Course: ",  in_python)
            
        case 9:    
            
            total = len(p_s | j_s)
            print("9. Display Total Unique Students: ", total) 
            
        case 10:
            print("Thank you !!!!!!!!!!!!!!!!!!")            
            break
     

  

