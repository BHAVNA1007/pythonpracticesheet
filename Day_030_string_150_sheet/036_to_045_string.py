'''
036_to_045_string

36. Reverse the order of words in a string.
37. Reverse each word in a string.
38. Reverse words without using split().
39. Search all occurrences of a character.
40. Search all occurrences of a word.
41. Check if a string contains a substring (without using contains()).
42. Check if two strings are equal without using equals().
43. Check if two strings are rotations of each other.
44. Check if two strings are anagrams.
45. Check whether a string starts with or ends with another string.
'''

'''
#36. Reverse the order of words in a string.
#S = "one two three" "three two one"

s = input('Enter the string: ')

s1 = s.split()

r_s =''

for  i in range(len(s1)-1,-1,-1):
   r_s += s1[i] +' '
print(r_s)
'''

'''
#37. Reverse each word in a string.
#S = "cat dog" "tac god"

s = input('Enter the string: ')
s1 = s.split()


for i in range(len(s1)):
    word = s1[i]
    for j in range(len(word)):
       rev = word[::-1]
    print(rev,end=" ")
'''
'''
#38. Reverse words without using split().
#S = "a b c" "c b a"

s = input('Enter the string: ')

rev = s[::-1]
print(rev)
'''

'''
#39. Search all occurrences of a character.
#S = "banana", Char = 'a' 1, 3, 5 (indices)

s = input('Enter a string: ')
char = input('Enter a char: ')

for i in range(len(s)):
    if s[i] == char:
       print(i, end=' ')

'''

'''
#40. Search all occurrences of a word.
#S = "a b a b", Word = "b" 2, 6 (start indices)

s = input('Enter a string: ')
w = input('Enter s word: ')

for i in range(len(s)):
   if s[i] == w:
      print(i, end=' ')
'''

'''
#41. Check if a string contains a substring (without using #contains()).
#S1 = "Hello", Sub = "ell" TRUE

s = input('Enter a string: ')
sub = input('Enter a sub: ')
s_s = False

for i in range(len(s)-len(sub)+1):
    temp = ''

    for j in range(len(sub)):
       temp += s[i+j]

       
    if temp == sub:
        s_s = True
        break
 
if s_s:
   print("True")
else:
   print("False")  
'''

'''
#42. Check if two strings are equal without using equals().
#S1 = "abc", S2 = "abc" TRUE

s1 = input('Enter a s1: ')
s2 = input('Enter a s2: ')
match = True

if len(s1) != len(s2):
    match = False

else:
   for i in range(len(s1)):
       if s1[i] != s2[i]:
          match = False
          break

if match:
    print("Ture")
   
else:
    print('False')  
'''

'''
#43. Check if two strings are rotations of each other.
#S1 = "abcde", S2 = "cdeab" TRUE 

s1 = input('Enter a s1: ')
s2 = input('Enter a s2: ')

match = False

if len(s1) == len(s2):
     match = True

     for i in range(len(s1)):
         s=s1[1:]+s1[:i]
    
         if s == s2:
             match = True
             break

if match:
    print("True")

else:
    print("False")
'''

#44. Check if two strings are anagrams.
#    S1 = "listen", S2 = "silent" TRUE
'''
s1 = input('Enter a s1: ')
s2 = input('Enter a s2: ')

if len(s1) == len(s2):
    if sorted(s1) == sorted(s2):
         print('True')
    else:
         print("Flase")   
    
else:
   print("Flase")   
'''

'''
s1 = input('Enter a s1: ')
s2 = input('Enter a s2: ')

if  len(s1) != len(s2):
    print('False')

else:
    f = True
    for ch in  s1:
         if ch.count(s1) != ch.count(s2):
              f = False
              break
    if f :
         print('True')

    else:
         print('False') 

'''
# 45. Check whether a string starts with or ends with another string.
# S = "apple pie", Prefix = "apple", Suffix = "pie" Start: True, End: #True
          

s = input('Enter the string: ')

prf =input('Enter the prf: ')
suf =input('Enter the suf: ')

print(s.startswith(prf))
       
print(s.endswith(suf))

'''
f1 = True
if len(prf) > len(s):
    f1 = False

else: 
   for i in range(len(prf)):
       if s[i] != prf[i]:
         f1 = False
         break  
if f1 == True:
    print("True") 
else:
    print('False')

    
f2 = True

if len(suf) > len(s):
   f2 = False 
else:
    start_suf = len(s)-len(suf)
   
    for i in range(len(suf)):
        if s[start_suf + i] != suf[i] :
            f2 = False
            break 

if f2 == True:
   print("True")
else:
    print('False')

    
'''























