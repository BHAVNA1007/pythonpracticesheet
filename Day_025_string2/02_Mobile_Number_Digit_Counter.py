'''
2.Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12
'''
num = input('Enter the string: ')
l = len(num)
count = 0

for ch in num:
    if ch<='9' and ch>='0':

        count += 1

print("Total digits: ",count)



