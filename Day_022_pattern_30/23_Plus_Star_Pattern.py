'''
23) Plus Star Pattern
          *
          *
         ***
          *
          *
'''
n = int(input("Enter a number: "))

i = 1
k = 1

while i <= n:
    space = 1
    while space <= n:
        print(" ", end='')
        space += 1

    print('*')

    k +=1
    i +=1

j = 1
while j <= n:
    print('*', end='')
    j +=1

j = n - 1
while j >= 1:
    print('*', end='')
    j -=1

print()
i =n - 1
k =n - 1

while i >= 1:
    space = 1
    while space <= n:
        print(" ", end='')
        space += 1

    print('*')

    k -= 1
    i -= 1