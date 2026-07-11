'''

78 Find the longest mirror-image substring at both ends. S = "aabccbaa" "aab"

'''

s = input("S: ")

res = ''

for i in range(len(s)-1,0,-1):

    prefix = s[:i]
    
    suffix = s[-i:] 

    if prefix[::-1] == suffix:

         res = prefix
 
         break

print(res) 
