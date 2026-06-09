'''
09_Library_Access_System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books'''


membership = input("Membership active (yes/no): ")
book_issued = int(input("Book issued: "))

if membership == "yes":
    print("Entry allowed ")
if book_issued < 3:
    print("Can issue more books")