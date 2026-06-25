'''
5.Hospital Record System (Search Digit)

A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

Task

Write a recursive function to determine whether a given digit is present.

Input
Enter Patient ID:
5837264

Enter Digit:
7
Output
Digit Found
'''

def found(n,d):
   if n == '':
       return False

   if int(n[0]) == d:
       return True

   return found(n[1:],d)  

def main():
   
    num = input("Enter Patient ID:")
    d = int(input("Enter Digit:"))

    if found(num, d):
       print("Digit Found") 

    else:
       print("Digit not Found")

main()
    

'''
def found(n, d):
    if n == 0:
        return False

    if n % 10 == d:
        return True

    return found(n // 10, d)

num = int(input("Enter Patient ID: "))
d = int(input("Enter Digit: "))

if found(num, d):
    print("Digit Found")
else:
    print("Digit Not Found")

'''
   
     

