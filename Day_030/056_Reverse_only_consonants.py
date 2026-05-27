'''
056_Reverse_only_consonants
 S = "apple" "eplpa"
'''
s = input('Enter a string: ')


cons = ''

for ch in s:
  if ch not in 'aeiouAEIOU':
     cons += ch


cons = cons[::-1]

res = ''
j = 0

for ch in s:
   if ch not in "aeiouAEIOU":
      res += cons[j] 
      j += 1
   else:
      res += ch
print(res)

