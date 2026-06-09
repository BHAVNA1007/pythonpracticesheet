'''
ABCDE
ABCD
ABC
AB
A

'''

n = int(input("Enter a number: "))

i = 1

while i <= n:
   print()

   j = i
   ch = 65
   while j <= n:
      print(chr(ch),end="")

      j += 1
      ch += 1
   
   i += 1

     