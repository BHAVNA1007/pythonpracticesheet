'''
27) Continuous Number Pyramid
            1
           2 3
          4 5 6
         7 8 9 10
'''
n = int(input("Enter a number: "))

i = 1
k =1
while i <= n:
   print()
   space = 1
   while space <= n-i:
      print(" ",end="") 
      space += 1

   s = 1
 
   while s <= i:
      print(k,end=' ')
      s += 1
      k+=1 
   i+=1
       
       

