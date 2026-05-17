'''

a
bc
d f
g  j
klmno

'''

n = int(input("Enter a number: "))

i = 1
ch = 97
while i<=n :
   print()
 
   j = 1
   
   while j <= i:
      if i==n or j==1 or i==j:
          print(chr(ch),end='')
      else:
          print(" ",end='')
      j += 1
      ch += 1
   i += 1 