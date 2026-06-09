'''
63 Count frequency of each character. 
S = "aabcc" a: 2, b: 1, c: 2
'''
s = input('Enter the string: ')

visited = []

for i in s:
   count = 0
   
   if i not in visited:
      for j in s:
         if i == j:
            count += 1
     
      print(i,':',count)
      visited.append(i) 
             
   
   