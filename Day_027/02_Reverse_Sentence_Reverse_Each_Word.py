'''
02_Reverse_Sentence_Reverse_Each_Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:
Python is powerful
Output:
lufrewop si nohtyP
'''
s = input('Enter the string: ')
words = s.split()

i = len(words)-1
final = ''
while i>=0:
   word = words[i]
   
   j = len(word)-1
   rev = ''
   while j >= 0:
      rev = rev + word[j]
      j -= 1
   final = final + rev + ' '
   i -= 1

print(final)
      
     
