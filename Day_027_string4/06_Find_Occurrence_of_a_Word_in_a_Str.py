'''06_Find_Occurrence_of_a_Word_in_a_String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:

iphone is good and iphone battery is strong

Word:
iphone
'''

s = input('Enter the string: ')
word = input('Enter a word')

count = 0
i = 0

while i <= len(s) - len(word):
   j = 0
   match = 1
   while j < len(word):
      if s[i + j] != word[j]:
          match = 0
          break
      j = j+1

   if match == 1:
      count = count + 1
 
   i = i + 1

print('Num of ocu:  ', count)




