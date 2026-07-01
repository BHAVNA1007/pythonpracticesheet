def Student_Details():
    name = input("Enter Student Name :")
    roll_n = int(input("Enter Roll Number :"))
    
    n = int(input("Marks:"))
    marks = []
    for m in range(n):
        
        mark = int(input(f"Enter Mark {m+1} :")) 

        while mark<0 or mark>100:
            print("Invalid marks")
            mark = int(input(f"Enter Mark {m+1} :")) 
        marks.append(mark)
         
    print("Student details added successfully.")

    return name, roll_n, marks
