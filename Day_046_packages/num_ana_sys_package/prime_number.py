def prime_num(n): 
    if n<=1:
       return "Not Prime Number"
    else:
       for i in range(2,(n//2)+1):
          if n%i == 0:
             return "Not Prime Number" 
        
       return  "Prime Number"