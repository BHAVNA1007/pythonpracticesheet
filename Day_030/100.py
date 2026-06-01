'''
100 Return true if string contains 'abc' not followed by '.'. S1 = "abcx", S2 = "abc." S1: True, S2: False

'''

s = input('Enter a string: ')

found = 0
for i in s:
   if i=='.':
       found = 1
 
if found==1:
   print("False")
else:
   print("True")   
