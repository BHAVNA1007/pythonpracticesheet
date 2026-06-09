'''
1
12
123
1234
123
12
1
'''
#first half

n = int(input('Enter a number: '))
i = 1
while i<=n:
   print()
   j = 1
   while j<=i:
      print(j,end='')
      j += 1
   i+=1

#second half
i = n-1
while i>=1:
   print()
   j = 1
   while j<=i:
      print(j,end='')
      j+=1
   i-=1