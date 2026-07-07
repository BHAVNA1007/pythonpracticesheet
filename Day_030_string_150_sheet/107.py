'''
107 Check if a string is a pangram (contains every letter). 
S = "The quick brown fox jumps over the lazy dog" TRUE

'''


s = input("Enter string: ").lower()
 
f = 0
for i in range(93, 123):
  
  if ch >= "a" and ch <= "z":
     f = 1

if f == 1:
   print("t")  

else:
   print("f") 