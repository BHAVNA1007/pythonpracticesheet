def highest_mark(marks):
    h_m = marks[0]
    for m in marks:
        if m > h_m:
           h_m = m
    return h_m 
