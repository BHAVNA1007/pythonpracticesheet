'''8.
=========================================
LIBRARY BOOK ISSUE TRACKER
==========================

A library records issued books.

books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]

Write a program to:

* Count how many times each book was issued.

Sample Output:
{
'Python':3,
'Java':2,
'C++':1
}
'''
n = int(input("Enter num of books: "))

books = []
for b in range(n):
    books.append(input())
print(books)

issued = {}
for book in books:
    issued [book] = issued .get(book, 0)+1
print(issued )
