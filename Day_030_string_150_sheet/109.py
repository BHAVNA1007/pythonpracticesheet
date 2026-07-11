'''

109 Find the lexicographically smallest substring of length k. S = "banana", k = 3 "ana

'''
     

 
s = input("S: ")

k = int(input("K: "))

smallest = s[:k]

for i in range(1, len(s) - k + 1):

    sub = s[i:i+k]

    if sub < smallest:

        smallest = sub

print(smallest)  