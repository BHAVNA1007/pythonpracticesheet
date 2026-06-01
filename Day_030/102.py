'''
102 Reverse a string using recursion. 
S = "abc" "cba
'''

s = input("Enter a string: ")

l = len(s)
rev = ''
for i in range(l-1,-1,-1):
    rev += s[i]
print(rev)
   