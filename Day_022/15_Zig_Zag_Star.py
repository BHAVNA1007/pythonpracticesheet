'''
15) Zig-Zag Star
    *   *   *
      *   *
    *   *   *
'''

n = int(input('Enter a number: '))
i = 1

while i <= n:
    print()
    
    j = 1

    while j<=i :

       if i % 2 != 0:
          print('*', end=' ')

       elif j% 2!=0:
           
           print("*", end=' ')
       else:
           print(" ")
      
       j+=1

    i+=1
 