def longest_name(emp_names):
    long = emp_names[0]
    for i in range(len(emp_names)):
         if  len(emp_names[0]) < len(emp_names[i]):
              
            emp_names[0] = emp_names[i]
    return emp_names[0]
