'''
6 Add Binary
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 '''
 
a = input("a = ")
b = input("b = ")

decimal1 = 0
for i in a:
    decimal1 = decimal1 * 2 + int(i)
#print(decimal1)    

decimal2 = 0
for i in b:
    decimal2 = decimal2 * 2 + int(i)
#print(decimal2)   

sum = decimal1 + decimal2
#print(sum)

binary = ''
while sum > 0:
    binary =  str(sum%2) + binary
    sum = sum // 2
print(binary)    
    
    

 

