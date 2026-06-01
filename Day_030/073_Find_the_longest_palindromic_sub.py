'''
73 Find the longest palindromic substring. 
S = "babad" "bab" (or "aba")
'''
s = input('Enter a string: ')


p = ''

length = 1

for i in range(len(s)):
  
   for j in range(i,len(s)):
       sub = s[i:j+1]  
      
       rev = sub[::-1]
      
       if sub == rev:
           if len(sub) > length:
               p = sub
               length = len(sub)    

print(p)               
        
       
