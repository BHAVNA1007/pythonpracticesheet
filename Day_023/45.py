'''

    5
   44
  333
 2222
11111

'''

n = int(input("Enter a number: "))

i = 1
k = n
while i <= n:
   print()
 
   space = 1
   while space <= n-i:
      print(" ", end='')
      space += 1

   j = 1
  
   while j <= i:
      print(k,end='')
      
      j +=1
   k -=1
   i += 1
    