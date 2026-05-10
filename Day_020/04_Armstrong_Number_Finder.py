'''
4.Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
'''
s = int(input("Enter starting number :"))
e = int(input("Enter ending number :"))

for n in range(s,e+1):

     temp = n
     power = len(str(n))
     total = 0

     while temp > 0:
        d = temp % 10
       
        total += d**power
        temp = temp // 10
     
     if total == n:
          print(n)
      
             
