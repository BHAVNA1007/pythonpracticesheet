'''
06_AI_Voice_to_Text_Correction_System

A company has developed an AI-based voice-to-text application for virtual meetings.

Due to microphone disturbances and speech recognition delays, some words are captured multiple times consecutively in the generated text.

Before saving the meeting transcript, the system must remove duplicate words while maintaining the original order of words.

Write a Python program to remove repeated words from a sentence.

Input:
hello hello team team meeting meeting started
Output:
hello team meeting started
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
                 
