'''

ABCDE
A  D
A C
AB
A
'''

n = int(input('Enter a number: '))

i = 1

while i<=n:
   print()
   
   j = 1
   ch = 65
   while j<=n:
      if i==1 or j==1 or i+j==n+1:
         print(chr(ch),end='')
      else:
         print(" ",end='')
      j += 1
      ch += 1
   i += 1  
           