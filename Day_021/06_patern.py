'''
6)
a
ab
abc
abcd
abcde
'''

n = int(input("enter a number: "))

i = 1

while i<=n:
  
   print()
   ch = 97
   j = 1
   while j<=i:
      print(chr(ch),end="")
      ch += 1
      j += 1
   i += 1 