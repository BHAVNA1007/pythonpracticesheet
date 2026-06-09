'''
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''

'''
import math

num = int(input("Enter a number = "))

is_prime = True
if num <= 1:
     
     print("not Prime Number")
     is_prime = False

else:
     for i in range(2, int(math.sqrt(num)+1 )):
           if num % i == 0:
              print("Not Prime")
              is_prime = False
              break
     else:
         print("Prime Number")

if is_prime:
   n_prime = num + 1
   while True:
       is_prime = True

        
       if n_prime <= 1:

           is_prime = False 

       else:
           for i in range(2, int(math.sqrt(n_prime)+1)):
               if n_prime % i == 0 :
                   is_prime = False
                
                   break
       if is_prime:
           print("Next Prime = ", n_prime)
           break
       n_prime += 1

else:
   p_prime = num - 1
   while True:
       is_prime = True
       if p_prime <= 1:

           is_prime = False  
       else:
           for i in range(2, int(math.sqrt(p_prime)+1)):
               if p_prime % i == 0:
                  is_prime = False
                  break
       if is_prime:
            print("previous immediate prime number",p_prime)
            break
       p_prime -= 1
                   
'''
import math
num = int(input("Enter The number = "))

prime = True

if num <= 1:
   prime = False
   print("Not Prime") 
else:
   for i in range(2, int(math.sqrt(num))):
       if num % i == 0:
           prime = False
           print("Not prime")
           break
   else:
       print(" Prime")
   

if prime:
    n_prime = num + 1
   
    while True:
        prime = True 
        if n_prime <= 1:
            prime = False
        else:
            for i in range(2, int(math.sqrt(n_prime)+1)):
                 if n_prime % i ==0 :
                      prime = False
                      break
            else:
                print("Next Prime = ", n_prime)
                break
        n_prime += 1    
else:

    p_prime = num - 1
    while True:
       prime = True 
       if p_prime <= 1:
           prime = False
       else:
           for i in range(2, int(math.sqrt(p_prime))):
               if p_prime % i == 0:
                    prime = False
                    break
           else:
               print("Privious Prime =", p_prime)
               break
       p_prime -= 1
        
    
    
    
