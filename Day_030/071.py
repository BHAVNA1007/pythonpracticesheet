'''
71 Print all substrings. 
S = "abc" "a, b, c, ab, bc, abc
'''

s = input('Enter a string: ')

for i in range(len(s)):
    for j in range(i,len(s)):
      sub = s[i:j+1]
      print(sub, end=" ") 