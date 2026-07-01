'''
101 Check if a string is a valid palindrome ignoring spaces and punctuation. 
S = "A man, a plan, a canal: Panama" TRUE
'''

s = input("Enter a string: ").lower()

s1 = ''

for i in s:
  if i.isalnum():
      s1 = s1 + i

rev = s1[::-1]


if s1 == rev:
   print("TRUE")

else:
   print("FALSE") 