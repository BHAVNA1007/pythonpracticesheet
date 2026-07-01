from student_res_system_package import percentage_marks
#from student_res_system_package.percentage_marks import percentage



def grade(marks):

    g =percentage_marks.percentage(marks)

    if  90 <= g <= 100:
       return "A+"

    elif 80 <= g < 90:
       return "A"

    elif 70 <= g < 80:
       return "B"

    elif 60 <= g < 70:
       return "C"

    elif 50 <= g < 60:
       return "D"

    else:
       return "Fail" 