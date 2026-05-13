'''
8) Border Number Pattern
    1 2 3 4 5
    2       5
    3       5
    4       5
    5 5 5 5 5

'''

n = int(input('Enter a number: '))

i = 1

while i<= n:
    print() 
    j = 1
    
    while j <= n:
       
        if i==n or   j==1 :
              print(i,end='')

        
        else:
            print(' ', end = '') 

        if j==n or i==1:

            print(j,end='')

   
 

        j += 1

    i += 1

   


