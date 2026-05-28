'''
67 Count how many times a substring appears. 
S = "abab", Sub = "ab" 2

'''
s = input('Enter the string: ')
sub = input('Enter the sub: ')
count = 0

for i in range(len(s)-len(sub)+1):
    match = 1
    for j in range(len(sub)):
        if s[i+j] != sub[j]:
           match = 0
    if match == 1:
       count += 1
print(count)  
