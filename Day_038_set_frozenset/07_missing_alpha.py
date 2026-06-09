'''
07_missing_alpha
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z.
'''
alphabets = set("abcdefghijklmnopqrstuvwxyz")
s = set()

while True:
    print("Menu")
    print("1. Enter Sentence")    
    print("2. Display Missing Alphabets")
    print("3. Count Missing Alphabets")
    print("4. Exit")
    
    choice = int(input("Enter choice: "))
    
    match choice:
        case 1:
            s = set(input("Enter sentence: ").lower())
            print(s)
            
        case 2:
            if not s:
                print("enter sentence first: ")
            else:    
                print("missing alphabets: ")
                for alpha  in alphabets:
                    if alpha not in s:
                        print(alpha, end=" ")   
                print()

        case 3:
            count = 0
            for alpha  in alphabets:
                if alpha not in s:
                        count += 1
                        
            print("Count of Missing Alphabets: ",count)
        case 4:
                print("Exit..........")            
                break
            
