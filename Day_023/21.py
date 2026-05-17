'''

1
22
3 3
4  4
55555

'''
n = int(input("Enter a number: "))

i = 1

while i <= n:
    print()

    j = 1
    while j <= i:
       if i == n or j==1 or  i == j:
            print(i, end="")
       else:
            print(" ", end='')
       j += 1
    i += 1  
     