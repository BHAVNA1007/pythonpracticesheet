'''
22) Inverted Hollow Pyramid
    *********
     *     *
      *   *
       * *
        *
'''
n = int(input('Enter a number:'))
i = 1

while i <= n:

    j = 1

    while j <= (2*n)-1:

        if (i == 1) or (i == j) or (i+j == 2*n):
            print("*", end="")

        else:
            print(" ", end="")

        j += 1

    print()

    i += 1

