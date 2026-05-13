'''
30) Extended Slanted Star Block
    **
     **
      **
       **
        **
'''

n = int(input("Enter a number: "))
i = 1
while i <= n:
   print()
   space = 1
   while space <= i:
       print(" ",end ="")
       space += 1

   j = i
   while j <= i+1 :
       print("*",end= "")
       j+=1
   i+=1  
      