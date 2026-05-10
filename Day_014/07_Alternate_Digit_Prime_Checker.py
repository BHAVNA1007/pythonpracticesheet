'''7Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime
'''
num = int(input("Enter a number = "))

l = len(str(num))

sum = 0
for i in range(l-1):
     d1 = num // 10 ** (l - 1) % 10
     print(d1)
     sum += d1
     d2 = num // 10 ** (l - 2) % 10
     print(d2)
     continue
    
print("Alternate Sum = ",sum)