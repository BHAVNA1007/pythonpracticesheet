'''
82 Create a string from a character array. 
Char[] = {'h', 'i'} "hi"

'''

s = input('Enter char list: ').split()
print("Char[] = ",s)


res = ''
for i in s:
   res += i

print(res)

    
  