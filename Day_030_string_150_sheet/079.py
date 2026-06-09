'''
79 Divide a string into n equal parts. 
S = "abcdef", n = 3 "ab", "cd", "ef"

'''

s = input('Enter a string: ')
n = int(input('Enter n: '))

lenght = len(s)//n

res = ''

for i in s:
   res += i
   if len(res) == lenght:
      print(res,end=', ')
      res =''        