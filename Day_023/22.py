'''

A
AB
A C
A  D
ABCDE

'''

n = int(input("Enter a number: "))

i = 1

while i<=n :
   print()

   j = 1
   ch = 65
   while j <= n:
      if i==n or j==1 or i==j:
          print(chr(ch),end='')
      else:
          print(" ", end='')
      j += 1
      ch += 1  
   i += 1  