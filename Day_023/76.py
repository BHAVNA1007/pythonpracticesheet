'''
x
xx
xxx
xxxx
xxx
xx
x
'''
n = int(input('Enter a number: '))

i = 1

while i<=n:
   print()
  
   j = 1
   while j<=i:
     print("x",end='')
     j += 1
   i += 1 

i=n-1

while i>=1:
   print()
   
   j = 1
   while j<=i:
     print("x",end='')

     j+=1
   i-=1
 
  
 
      
   