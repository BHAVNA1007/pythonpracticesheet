'''
72 Print all substrings of length n. 
S = "abc", n = 2 "ab, bc

'''
s = input('Enter s string: ')
n = int(input('Enter a length for substrings: '))

for i in range(len(s)):
    for j in range(i,len(s)):
        sub = s[i:j+1]
        
        if n== len(sub):  
           print(sub,end=" ")           