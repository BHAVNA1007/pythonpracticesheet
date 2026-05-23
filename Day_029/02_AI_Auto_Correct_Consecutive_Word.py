'''02_AI_Auto_Correct_Consecutive_Word_Remover

An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

### Input:
text
hello hello hello team meeting meeting started

### Output:
text
hello team meeting started
'''
s = input('Enter the string: ')
word = ''
words = s.split()

for i in range(len(words)):
    duplicate = False
    for j in range(i+1,len(words)):
         if words[i] == words[j]:
             duplicate = True
             break
    if duplicate == True     
        word += words[i] +' '

print(word)   
          