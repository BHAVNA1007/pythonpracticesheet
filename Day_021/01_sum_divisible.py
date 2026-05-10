'''
01_sum_divisible
WAP to find out the sum of all integer between 100 and 200 which are divisible by 9
'''

s = int(input("Enter starting number :"))
e = int(input("Enter ending number :"))
total = 0
for n in range(s, e+1):
   
    if n % 9 == 0:
       total += n
print("Sum of all digit which divisible by 9 is:",total)