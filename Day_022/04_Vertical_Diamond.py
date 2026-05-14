'''
4) Vertical Diamond
       *
      * *
     *   *
    *     *
     *   *
      * *
       *
'''

n = int(input("Enter a number: "))

i = 1

while i <= n:
      print()

      j = 1
      while j<= (n*2) - 1:
      
         if ( i + j == n + 1) or ( j - i == n - 1) :

             print("*",end='')

         else:
    
            print(" ",end='')

         j += 1

      i += 1
  
