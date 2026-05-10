'''
6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625
'''
n = int(input("Enter a number = "))
new = n
same_num = False
square = n**2
while new > 0:
    if new % 10 == square % 10:
        same_num = True

    square= square // 10
    new = new // 10
if same_num:
    print("Yes")
else:
    print("No")
   
     
