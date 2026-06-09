'''
21) Hollow Pyramid (Practice)
            *
           * *
          *   *
         *     *
        *********
'''
n = int(input("Enter a number: "))

i = 1

while i<= n:

   print()

   j = 1
   while j <= (2*n)-1:

       if (i+j==n+1) or (j-i==n-1) or i==n:

          print("*",end="")
      
       else:
          print(" ",end='')
       j += 1
   i += 1    