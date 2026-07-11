'''
077

77 Find the longest substring that appears at both ends. S = "abracadabra" "abra"

'''

s = input("S: ")

res = ""

for i in range(len(s)-1, 0, -1):

     prefix = s[:i]
     suffix = s[-i:]

     if prefix == suffix:

         res = prefix

         break
print(res)
    