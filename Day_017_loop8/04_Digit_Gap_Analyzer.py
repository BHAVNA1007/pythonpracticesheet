'''
4.Digit Gap Analyzer

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number
'''
num = int(input("Enter The Number = "))
l = len(str(num))
st = ""
count = 0
max = 0
print("Differences:", end=" ")
while l>1:

   d1 = num//10**(l-1)%10
   d2 = num//10**(l-2)%10
   diff = abs(d1 - d2)
   print(diff, end = " ")
   st += str(diff)
   if diff > 2:
       count += 1
   if max < diff:
       max = diff
   l -= 1
   
print("\nCount (>2) =",count)

print("Max Difference =", max)

smooth = True
for i in range(len(st)):
    if int(st[i]) <= 2:
       smooth = True
    else:
       smooth = False

if smooth:
    print("Smooth Number")
else:
    print("Irregular Pattern")


   

      
   