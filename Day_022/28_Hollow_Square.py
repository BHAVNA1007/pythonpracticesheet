'''
28) Hollow Square
    ***
    *   *
    *   *
    *   *
    ***
'''
n = int(input('Enter a number: '))

i = 1

while i <= n:
  print()

  j = 1
  while j <= n:
     if i==1 or i==n or j==1 or j==n :
         print("*", end='')
    
     else:
         print(" ",end='')
     j +=1
  i += 1

  

