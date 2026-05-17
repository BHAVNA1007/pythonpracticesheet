'''
ABCDE
 A__D
  A_C
   AB
    A
'''

n = int(input("Enter a number:  "))

i = 1

while i<=n:
   print()

   space = 1
   while space<=i:
      print(' ',end='')
      space += 1

   j = 1
   ch = 65
   while j <= n-i:
      if i==1 or j==1 or j==n-i:
         print(chr(ch),end='')
      else:
         print("_",end='')
      j+=1
      ch += 1
   i += 1    
  
          
