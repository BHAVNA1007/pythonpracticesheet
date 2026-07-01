def count_names_starting_with_vowel(emp_names):
    
    res = [] 
    for name in emp_names:
        if name.startswith(("A","E","I","O","U")):
            res.append(name)
            
    return len(res) 

