def perfect_num(n):
    i = 1
    sum = 0
    while i <= n//2:
       if n % i == 0:
          sum += i 
       i += 1
    if sum == n:
       return True
    else:
       return False 