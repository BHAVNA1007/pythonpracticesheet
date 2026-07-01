def find_second_highest_age(emp_a):
    n_age = []

    for age in emp_a:
        if age not in n_age:
            n_age.append(age)

    n_age.sort()
    return n_age[-2]
