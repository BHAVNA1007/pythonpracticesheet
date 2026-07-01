def count_senior_employees(emp_a):
    count = 0 
    for age in emp_a:
        if age >= 50:
           count += 1
    return count    
