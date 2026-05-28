'''
66 Count number of sentences in a paragraph. 
P = "This. Is. Test." 3
'''

s = input('Enter a para: ')

count = 0

for i in range(len(s)):
    if s[i] == '.':
        count += 1
print(count)
