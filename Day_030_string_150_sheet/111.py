'''
111 Check if a string can be rearranged into a palindrome. S = "aabbc" TRUE

'''

s = input("S: ")
odd = 0
visited = ""


for ch in s:
  
   if ch not in visited:
 
       count = 0

   for c in s:

       if c == ch:

           count += 1

   if count % 2 != 0:
    
       odd += 1

   visited += ch

if odd <= 1:

   print(True)

else: 
                 
   print(False)
        