'''
*
* *
*   *
*    *
* * * * 
'''

n = int(input("Enter the number: "))

i = 1

while i<=n :
   print()
   j = 1
  
   while j<=i:
       if j==1 or i==n or i==j:
          print("*",end='')
       else:
          print(" ", end='')   

       j += 1
   i += 1 
