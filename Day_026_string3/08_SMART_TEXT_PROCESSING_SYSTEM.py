'''
08_SMART_TEXT_PROCESSING_SYSTEM

A software company is developing a Smart Text Processing System for
handling user messages. Different users require different text
transformations. To avoid creating separate applications, the company
wants a menu-driven program where users can select operations according
to their requirements.

The system should continue executing until the user selects Exit.

====================================================== MENU
======================================================

===== Smart Text Processing System =====

1.  Reverse Complete String
2.  Reverse Every Word
3.  Reverse Word Order
4.  Exit

====================================================== Choice 1 :

Conditions: - Reverse the complete string - Ignore extra spaces - Keep
special characters (@,#,$,%) in their original positions - Do not use
built-in reverse functions

Example: Input: ja@va#py

Output: yp@av#aj

Test Case 1: ab@cd#ef Output: fe@dc#ba

Test Case 2: py@th#on Output: no@ht#yp

Test Case 3: java@proOutput : orpa@vaj

====================================================== Choice 2 :

Conditions: - Reverse every word separately - Words containing digits
should not be reversed - Ignore extra spaces between words - First
letter of each reversed word should become uppercase

Example: Input: java is easy123 programming

Output: Avaj Si easy123 Gnimmargorp

Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
Repoleved

Test Case 2: hello java99 world Output: Olleh java99 Dlrow

====================================================== Choice 3 :

Conditions: - Reverse order of words - Remove duplicate words - Ignore
case while checking duplicates - Keep only first occurrence

Example: Input: Java python Java react Python

Output: React Python Java

Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

Test Case 2: Python React Java Python React Output: Java React Python

====================================================== Choice 4
======================================================
Program Closed Successfully
'''

'''
08_SMART_TEXT_PROCESSING_SYSTEM
'''

while True:

    print("=" * 55)
    print("===== Smart Text Processing System =====")
    print("=" * 55)

    print("1. Reverse Complete String")
    print("2. Reverse Every Word")
    print("3. Reverse Word Order")
    print("4. Exit")

    print("=" * 55)

    choice = int(input("Enter Choice: "))

    print('======================================================')
    print(' CHOICE 1')
    print(' ======================================================')

    match choice:
        case 1:

             s = input("Enter String: ")
             s = s.strip()
             s_ch = {}
             for i in range(len(s)):
                  if not s[i].isalnum():
                     s_ch[i] = s[i]
             letters =""
             for ch in s:
                if ch.isalnum():
                    letters += ch
             rev = ''
             for i in range(len(letters)-1,-1,-1):
                 rev += letters[i]  

             res = ''
             index = 0
             for i in range(len(s)):
                 if i in s_ch:
                     res += s_ch[i]
                 else:
                     res += rev[index]
                     index += 1
             print(res) 

        case 2:
             s = input("Enter String: ")
             words = s.split()     
             i = 0
             while i < len(words):
                 word = words[i]
                 
                 rev =''
                 j = len(word)-1
                 
                 digit = False
                 d = 0
                 while d < len(word):
                     if word[d].isdigit():
                        digit  = True
                        break
                     d += 1   

                 if digit == False:
                      
    
                     while j >= 0 :
                         if word[j] <= 'z' and word[j] >= 'a':
                             rev = rev + word[j]
                         j = j - 1  
                     print(rev.title(), end=' ') 
                 else:
                     print(word, end=' ')     
                 i += 1

        case 3:
             s = input("Enter String: ") 
             words = s.split() 
             i = 0
             unique = []
             while i< len(words):       
                 count = 0
                 j = 0
                 while j < len( unique):
                      if words[i].lower() == words[j].lower():
                          count = count + 1
                      j = j + 1

                 if count == 0:
                     unique.append(words[i])
                 i  = i + 1

             i = len(unique) - 1
             while i >= 0:
                 print(unique[i].title(),end=' ')
                 i = i - 1     
             break     




                             