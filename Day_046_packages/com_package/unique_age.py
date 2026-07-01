def remove_duplicate_ages(emp_a):
    n_age = []

    for age in emp_a:
        if age not in n_age:
            n_age.append(age)

    
    return n_age 
