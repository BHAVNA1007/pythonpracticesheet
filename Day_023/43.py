'''
    1
   21
  321
 4321 
54321

'''
n = int(input("Enter a number: "))

i = 1

while i <= n:
   print()

   space = i
   
   while space <= n:

      print(".", end='')
      space += 1

   j = i
  
   while j >= 1:
      print(j,end='')
      j -= 1
   
   i += 1
