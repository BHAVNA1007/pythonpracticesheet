
from student_res_system_package import percentage_marks, stu_details, stu_grade, stu_highest_marks,stu_lowest_marks, total_marks
def main():

   name = ""
   roll_n = 0
   marks = []

   print("*** STUDENT RESULT MANAGEMENT ***\n\n")
   print("1. Add Student Details")
   print("2. Calculate Total Marks")
   print("3. Calculate Percentage")
   print("4. Find Grade")
   print("5. Display Result")
   print("6. Find Highest Mark")
   print("7. Find Lowest Mark")
   print("8. Exit")

   while True:
       choice = int(input("Enter choice: "))

       match choice:
             case 1:
                  print("\n1. Add Student Details") 
                  name, roll_n, marks = stu_details.Student_Details()
                 
             case 2:
                  print("\n2. Calculate Total Marks")
                  
                  if marks:
                     total = total_marks.cal_marks(marks)
                     print("Total marks: ",total)
                  else:
                     print("Please add stu details first") 
             case 3:
                  print("\n3. Calculate Percentage")

                  if marks:
                     res = percentage_marks.percentage(marks)
                     print("Percentage: ",res)

             case 4:
                  print("\n4. Find Grade")

                  if marks:
                      g = stu_grade.grade(marks)
                      print("Grade =", g) 
             
             case 6:
                  print("\n6. Find Highest Mark")

                  
                  if marks:
                      highest = stu_highest_marks.highest_mark(marks)
                      print("highest mark: ",highest)

             case 7:
                  print("\n7. Find Lowest Mark")
                  
                  if marks:
                     lowest = stu_lowest_marks.lowest_mark(marks)
                     print("Lowest Mark: ",lowest) 
  
             case 5:
                  print("\n5. Display Result")

                  print("----------- RESULT CARD -----------")
                  if marks:
                      total = total_marks.cal_marks(marks)
                      res = percentage_marks.percentage(marks)
                      g = stu_grade.grade(marks)
                      highest= stu_highest_marks.highest_mark(marks)
                      lowest = stu_lowest_marks.lowest_mark(marks)

                      print("\nname  :", name)
                      print("Roll No : ", roll_n)
                      print("\nMarks")


                      for i in range(len(marks)):
                          print(f"Mark {i+1} :  {marks[i]} ") 
    
                      
                      print("\nTotal marks: ",total)
                      print("Percentage: ",res)
                      print("Grade :", g)
                      print("highest mark: ",highest)
                      print("Lowest Mark: ",lowest) 


             case 8:
                  print("Thank You. Program Terminated.")
                  break  
main()
                   
