'''
147 Decompress a run-length encoded string. 
S = "a3b2c1" "aaabbc"
''' 

s = input("Enter a string: ")
prev = ''
res = ''
 
for i in s:
   if i.isalpha():
       res = res + i
       prev = i
   else:
       res = res + prev * (int(i)-1)

print(res)