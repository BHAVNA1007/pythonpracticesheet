def lowest_mark(marks):
    l_m = marks[0]
    for m in marks:
        if m < l_m:
           l_m = m
    return l_m 