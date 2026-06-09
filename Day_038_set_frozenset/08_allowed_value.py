'''
8.
=========================================
ALLOWED CHARACTER VALIDATOR
=========================================

Allowed characters are:
A-Z, a-z, 0-9

Store allowed characters in a Frozen Set.

Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit

Requirements:
- Use Frozen Set.
- Username should contain only allowed characters.
'''

allowed_characters = frozenset(
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"    
)

username = ""

while True:
    print("Menu:")
    print("1. Enter Username")
    print("2. Validate Username")
    print("3. Display Allowed Characters")
    print("4. Exit")
    
    choice = int(input("Enter choice: "))
    
    match choice:
        case 1:
            username = input("Enter username: ")
             
        case 2:
            if username == "":
                print("Enter username first")     
            else:
                valid = True
                for char  in username:  
                    if char not in allowed_characters:                         
                        valid = False
                        break

                if valid:
                    print("valid username")
                else:        
                    print("Invalid username")
        case 3:
            print("Allowed Characters:") 
            for ch in sorted(allowed_characters):
                print(ch, end=" ")
            print()    
            
        case 4:
            print("Exiting...................")
            break
            