
'''
    1
    2
    3
    4
123454321
    4
    3
    2
    1
'''

n = int(input("Enter a number: "))

i = 1
k = 1

while i <= n:
    space = 1
    while space <= n:
        print(" ", end='')
        space += 1

    print(k)

    k +=1
    i +=1

j = 1
while j <= n:
    print(j, end='')
    j +=1

j = n - 1
while j >= 1:
    print(j, end='')
    j -=1

print()
i =n - 1
k =n - 1

while i >= 1:
    space = 1
    while space <= n:
        print(" ", end='')
        space += 1

    print(k)

    k -= 1
    i -= 1