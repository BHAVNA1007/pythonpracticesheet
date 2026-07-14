'''
135 Check if two strings differ by exactly one character. S1 = "pale", S2 = "ple" False (differs by insertion/deletion)

'''

s1 = input("S1: ")

s2 = input("S2: ")



if len(s1) != len(s2):
   print(False)

else:
   count = 0

   for i in range(len(s1)):
       if s1[i] != s2[i]:
          count += 1
         

   if count == 1 :
       print(True)

   else:
       print(False) 
     
               
 



   

    
    
