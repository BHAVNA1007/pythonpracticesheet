'''
a
bc
def
ghij
klmno

'''
n = int(input("Enter a number: "))

i = 1
ch = 97
while i <= n:

   print()

   j = 1
   while j <= i:

      print(chr(ch),end='')

      j += 1
      ch += 1

   i += 1