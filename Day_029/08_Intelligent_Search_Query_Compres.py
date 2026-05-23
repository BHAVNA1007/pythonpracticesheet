'''
08_Intelligent_Search_Query_Compressor

A search engine company wants to compress user queries.

## Rules:

* Count frequency of each character
* Display characters in sorted order
* Ignore spaces
* Case insensitive

### Input:

text
Google Search


### Output:

text
a1c1e2g2h1l1o2r1s1t1
'''
s = input('Enter a string: ')
res =''
s =s.lower().replace(" ","")
for i in range(len(s)):
    count = 1

    for j in range(i+1,len(s)):
        if s[i] == s[j]:
           count += 1
    if s[i] not in s[:i]:
        print(''.join(sorted(s[i])),str(count))         
    











