'''
04_Palindrome_Number_List_Checker_Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:
Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
'''
n = int(input('Enter the size of list: '))

print('Plz enter the numbers...')

numbers = []

i =0
while i < n:
   x = int(input('number: '))
   numbers.append(x)
   i += 1
print(numbers)


palindrom = []

for num in numbers:
    new_n = num
    rev = 0
    
    while new_n > 0:
       d = new_n % 10
       rev = rev*10+d
       new_n = new_n//10
    if num == rev:
       palindrom.append(rev)

print('Palindromes:', palindrom)
    
count = 0
for i in palindrom:
    count += 1  
print('Count :', count)

max = palindrom[0]
for i in palindrom:
    if i > max:
       max = i 
print('Largest :', max)

palindrom.sort()
print('Sorted: ',palindrom)


     





