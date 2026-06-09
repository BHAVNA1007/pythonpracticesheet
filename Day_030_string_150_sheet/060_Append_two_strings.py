'''
060_Append_two_strings but remove adjacent duplicates. S1="miss", S2="issippi" "misisip

'''
s1 = input('Enter s1: ')
s2 = input('Enter s2: ')

prev1 = s1[0]
res1 = prev1

i = 1

while i < len(s1):
   if s1[i] != prev1:
      res1 += s1[i]
      prev1 = s1[i]
    
   i+=1


       
prev2 = s2[0]
res2 = prev2

i = 1

while i < len(s2):
   if s2[i] != prev2:
      res2 += s2[i]
      prev2 = s2[i]
    
   i+=1

res = res1 + res2
print(res)


