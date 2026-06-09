'''
07_Remove_Duplicate_Words_from_a_String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.

``
hello hello how are are you


Output:


hello how are you
'''
s = input("Enter String: ") 
words = s.split() 
i = 0
unique = []
while i< len(words):       
   count = 0
   j = 0
   while j < len( unique):
      if words[i].lower() == unique[j].lower():
         count = count + 1
      j = j + 1

   if count == 0:
      unique.append(words[i])
      
   i  = i + 1

i = len(unique) - 1
while i >= 0:
    print(unique[i],end=' ')
    i = i - 1     
      