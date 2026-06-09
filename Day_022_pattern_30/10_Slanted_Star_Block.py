'''
10) Slanted Star Block
    **
     **
      **
       **
'''

n = int(input("Enter a number: "))
i = 1

while i<= n:
   print()
   j = i

   space = 1
   while space <= i:
      print(" ",end ="" )
      space += 1
   while j<=i+1:
      print("*",end="")
      j+=1
   i +=1 
