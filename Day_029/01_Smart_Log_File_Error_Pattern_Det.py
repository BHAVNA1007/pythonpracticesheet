'''
1. Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:
text
abcabcbb

Output:
text
abc
'''
text = input('Enter the text: ')
long_sub = ''

for i in range(len(text)):
    temp = ''
    for j in range(i,len(text)):
        if text[j] not in temp:
             temp += text[j]
        if len(temp) > len(long_sub): 
             long_sub = temp
print(long_sub)
  
    



