'''
19) Reverse Number Cross
    5   5
     4 4
      3
     4 4
    5   5
'''

n = int(input('Enter a number: '))

i = 1

while i<= n:
    print()
    k = n 
    j = 1
    while j<=n:
         
        if i==j  :
            print("*",end='') 
            
        else:
            print(' ',end='')
            
                       
        j+=1
        k -=1

    i +=1
            