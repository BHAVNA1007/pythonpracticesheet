'''
69 Count how many times 'life' appears in a string. 
S = "life is life" 2

'''

s = input('Enter the string: ')
word = input('Enter a word: ')

count = 0

for i in range(len(s)-len(word)+1):
     match = 1
     for j in range(len(word)):
         if s[i+j] != word[j]:
               match = 0
              
     if match == 1:
         count += 1
print(count)



