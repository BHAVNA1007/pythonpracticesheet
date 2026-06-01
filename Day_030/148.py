'''
148 Find the first recurring substring of length k. 
S = "abcab", k = 2 "ab
'''

s = input("Enter string: ")
k = int(input("k: "))

for i in range(len(s) - k + 1):
    sub = s[i:i+k]

    for j in range(i + 1, len(s) - k + 1):
        if sub == s[j:j+k]:
            print("First recurring substring =", sub)
            break

  
