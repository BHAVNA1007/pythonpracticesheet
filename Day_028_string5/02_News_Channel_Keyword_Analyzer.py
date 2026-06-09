'''
2.Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india
'''
s = input('Enter the string: ')
s1 = s.split()

max_c = 0
res = ''

for i in range(len(s1)):
   count = 0

   for j in range(len(s1)):
       if s1[i] == s1[j]:
          count += 1

   if count > max_c:
      max_c = count
      res = s1[i]

print(res)