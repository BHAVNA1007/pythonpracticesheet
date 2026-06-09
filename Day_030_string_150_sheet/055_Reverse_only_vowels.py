'''
055_Reverse_only_vowels
 S = "hello" "holle"
'''
 
s = input('Enter a string: ')
    
vowel = ''

for ch in s:
  if ch in 'aeiouAEIOU':
      vowel += ch

vowel = vowel[::-1]


res = ''
j = 0

for ch in s:
   if ch in 'aeiouAEIOU':
      res += vowel[j]
      j += 1
   else:
      res += ch

print(res)
          