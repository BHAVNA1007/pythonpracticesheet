'''
145 Remove HTML tags from a string. S = "<h1>Title</h1>" "Title

'''

s = input("S: ") 

res = ""

inside_tag = False

for ch in s:

    if ch == "<":

        inside_tag = True

    elif ch == ">":

        inside_tag = False

    elif not inside_tag:

         res += ch

print(res)  
     

  
 
       

