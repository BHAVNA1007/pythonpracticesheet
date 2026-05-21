'''
07_Customer_Feedback_Analysis_System
Write a Python program to count the frequency of every word in a given sentence.

Input:
delivery was fast and delivery service was good
Output:
delivery : 2
was : 2
fast : 1
and : 1
service : 1
good : 1
'''
s = input("Enter String: ") 
words = s.split() 
i = 0

while i< len(words):       
   count = 0
   j = 0
   while j < len(words):
      if words[j].lower() ==words[i].lower() :
         count = count + 1
      j = j + 1

  
      
   i  = i + 1
   print(words[i-1],count)
                 
