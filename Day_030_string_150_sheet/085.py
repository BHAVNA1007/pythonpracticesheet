'''
85 Convert string into a char array without built-in functions. 
S = "test" {'t', 'e', 's', 't'}
'''

s = input("Enter a string: ")

res = ''
 
list =[]
for i in s:
   list.append(i)

print(list)