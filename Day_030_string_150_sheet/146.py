'''
146 Compress a string using run-length encoding. 
S = "aaabbc" "a3b2c1"
'''

s = input('Enter a string: ')
prev = s[0]
res = ''
count = 1

for i in range(1, len(s)):
   
   if s[i] == prev:
      count += 1
   else:
      res += prev + str(count)
      prev = s[i]
      count = 1 

res += prev + str(count)
print(res)