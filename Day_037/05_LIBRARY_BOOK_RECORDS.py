'''
======================
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
'''


from collections import namedtuple

n = int(input("Enter no of books:  "))

book = namedtuple("book",['book_id','title','author','price'])

books = []

for i in range(n):
   print(f"Enter book{i+1} details:")
   b_id = input("Enter book id: ")
   b_t = input("Enter book title: ")
   auth = input("Enter  auther name: ")
   p = int(input("Enter amount: "))
   books.append(book(b_id,b_t,auth,p))



for b in books:
    print(b.book_id,end=' ')
    print(b.title,end=' ')
    print(b.author,end=' ')
    print(b.price,end=' ')
    print()

       
Expensive = books[0]
for b in books:

    if  Expensive.price > b.price:
        Expensive = b
         

print("\nMost Expensive Book: ")
print(b.book_id,end=' ')
print(b.title,end=' ')
print(b.author,end=' ')
print(b.price,end=' ')
print()


count = 0
sum = 0
for b in books:
   count += 1
   sum += b.price
   avg = sum / count

print("\nAverage Book Price:", avg)



  
ath = input("\nEnter author name: ") 
  
for b in books:
   
   if b.author == ath:
       print(b.book_id,end=' ')
       print(b.title,end=' ')
       print(b.author,end=' ')
       print(b.price,end=' ')
       print()

























