'''
5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed.
'''

n = int(input("stores unique ISBN numbers of books: "))
isbn = set()
for i in range(n):
   isbn.add(int(input(f"isbn num {i+1}: ")))
print(isbn)        

while True:
     
    print("Menu") 
    print("1. Add ISBN") 
    print("2. Remove  ISBN") 
    print("3. Search ISBN") 
    print("4.Display ISBN List") 
    print("5. Count Books")
    print("6. Exit") 
   
    choice = int(input("Enter a choice: "))
    
    match choice:
        case 1:
                ISBN = int(input("Enter ISBN: "))
                if ISBN in isbn:
                    print("Duplicate ISBN not allowed")
                else:
                   isbn.add(ISBN)
                   print("ISBN added successfully")
                   
        case 2:
                isbn.discard(int(input(" Remove isbn: ")))     
                print(isbn)        
                
        case 3:
                id = int(input("Enter isbn: "))
                if id in isbn :
                        print("isbn found")
                else:
                        print("isbn not found")
        case 4:
                for i in isbn:
                    print(i ,end=" ")
                print()                    

        case 5:
                unique = len(isbn)
                print("Count books",unique)       

        case 6:
                print("Exit..................")             
                break                
                           