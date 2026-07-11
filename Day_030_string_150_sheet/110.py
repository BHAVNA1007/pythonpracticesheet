'''
110 Find the lexicographically largest substring of length k. S = "banana", k = 3 "nan"

'''

s = input("S: ")

k = int(input("K: "))

largest = s[:k]

for i in range(1, len(s)-k+1):

     sub = s[i:i+k]

     if sub > largest:

        largest = sub

print(largest)