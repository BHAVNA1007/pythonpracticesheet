'''
6) Number Triangle with Dashes
    - - - - 1
    - - - 2 3
    - - 3 4 5
    - 4 5 6 7
    5 6 7 8 9
'''

n = int(input('Enter a num : '))

i = 1
 
while i <= n:
    print()
   
    j = i
    while j <= n:
       print('-', end=" ")
       j += 1
  
    num = i
    k = 1
    while k <=i :
       print(num, end=' ')
       k+=1 
       num +=1
   
 
    i += 1
   
    

