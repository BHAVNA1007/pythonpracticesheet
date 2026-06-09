'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

'''

n = int(input("Enter a number: "))

i = 1

while i<=n:
  print()

  space = 1
  while space<=n-i:
     print(" ",end='') 
     space += 1

  j = 1
  while j<=i:
     print(j,end=' ')
     j += 1

  i += 1 