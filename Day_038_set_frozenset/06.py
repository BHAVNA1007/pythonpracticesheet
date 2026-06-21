'''
6.
=========================================
COMMON CHARACTER FINDER
=========================================

Enter two strings and find common characters.

Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit

Example:
String1: python
String2: typhoon

Output:
{p, t, h, o, n}
'''
str1 = ''
str2 = ''
while True:
    print("\nMenu\n")
    print("1. Enter First String") 
    print("2. Enter Second String")
    print("3. Display Common Characters")
    print("4. Count Common Characters")
    print("5. Exit")
    
    choice = int(input("\nEnter a choice: "))
    
    match choice:
        case 1:
            str1 = input("\nEnter first string: ")         

        case 2:
            str2 = input("\nEnter second string: ")         
       
        case 3:
            print("\nCommon characters are: ")
            print(set(str1).intersection(str2))

        case 4:
            print("\ncount of Common characters are: ")
            print(len(set(str1).intersection(str2)))
            
        case 5:
            print("\nExit.................")            
            
            break 
        case _:
            print("\ninvalid choice:")               
    

