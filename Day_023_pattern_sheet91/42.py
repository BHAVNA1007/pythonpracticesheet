'''

54321
5432
543
54
5

'''

n = int(input("Enter a number: "))

i = 1

while i <= n:

    print()

    j = i
    k = n
    while j <= n:
       print(k, end='')
       k -= 1 
       j += 1
        
    i += 1
       
    