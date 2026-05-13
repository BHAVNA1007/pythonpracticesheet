'''
20) Continuous Diamond Numbers
           1
          2 3
         4 5 6
        7 8 9 10
         4 5 6
          2 3
           1
'''

n = int(input('Enter a number : '))

i = 1
k = 1
while i <= n:
    
    print()
    space = 1

    while space <= n-i:
       print(" ",end = '') 
       space  += 1

    j = 1
   
    while j <= i:
       print(k, end=' ') 
       j += 1
       k += 1   
    i += 1 
