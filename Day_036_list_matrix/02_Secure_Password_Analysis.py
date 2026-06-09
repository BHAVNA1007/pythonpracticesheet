'''
2.Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")
'''

n = int(input("Enter size N: "))

pwd = []
for i in range(n):
   pwd.append(input())
print(pwd) 

count = 0
for i in range(len(pwd)):
   for j in range(i+1,len(pwd)):
       
       common = False
       
          
       for ch1 in pwd[i]:
          
           for ch2 in pwd[j]:

               if ch1 == ch2:
                  common = True
                  break

           if common:
               break   

       if not common:
           print((pwd[i],pwd[j]))
           count += 1
print(count)
         
           
        
       