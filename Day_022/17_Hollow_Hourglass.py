'''
17) Hollow Hourglass
    * * * * * *
      *     *
        * *
         *
        * *
      *     *
    * * * * * *

'''

n = int(input("Enter a number : "))

# Upper Part
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


# Lower Part
i = n-1

while i >= 1:

    j = 1

    while j <= (2*n)-1:

        if (i == 1) or (i == j) or (i+j == 2*n):
            print("*", end="")

        else:
            print(" ", end="")

        j += 1

    print()

    i -= 1