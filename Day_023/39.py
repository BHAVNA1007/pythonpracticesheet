'''
123456
54321
1234
321
12
1

'''
n = int(input("Enter a number: "))

i = 1

while i <= n:

    print()

    j = 1
    
    k = n-i+1
    while j <= n - i + 1:

      if i % 2 != 0:
          print(j, end='')
      else:
          print(k, end='')

      j += 1
     
      k -= 1  
    i += 1

         
