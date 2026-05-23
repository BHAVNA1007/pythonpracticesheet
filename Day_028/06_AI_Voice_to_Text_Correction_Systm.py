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
result =''
for i in range(len(words)):
    duplicate = False
    for j in range(i+1,len(words)):
         if words[i] == words[j] :
            duplicate = True
            break
    if duplicate == False:
        result = result + words[i]+" "
        
print(result)  
                             
