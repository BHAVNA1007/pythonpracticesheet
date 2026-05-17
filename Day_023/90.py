'''
     1               
    101            
   10101         
  1010101           
 101010101   
10101010101

'''
n = int(input('Enter a number: '))
i = 1
while i<=n:
   print()
   space = 1
   while space<=n-i+1:
      print(' ',end='')
      space+=1
   
   j = 1
   while j<=i*2-1:
      if j%2==0:
         print("0",end='')
      else:
         print("1",end='') 
      j+=1
   i+=1