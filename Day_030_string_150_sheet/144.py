'''
144 Check if a string is valid HTML/XML tag sequence. S = "<a><b></a></b>" FALSE
'''

import re

s = input("S = ")

tags = re.findall(r'</?[A-Za-z]+>' , s)

stack = []

for tag in tags:

    if tag.startswith('</'):

        if not stack:
            print(False)
            break

        top = stack.pop()
    
        if top != tag[2:-1]:
           print(False)
           break

    else:
    
        stack.append(tag[1:-1])

else:

    print(len(stack)==0) 