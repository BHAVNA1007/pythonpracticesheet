'''
133 Convert a Roman numeral string to integer. 
S = "XIV" 14
'''
s = input("Enter a string: ").upper()

I = 1
V = 5
X = 10


Sum = 0
for i in s:
    if i=='X' :
       Sum += X
    elif i == 'I':
       Sum -= I
    else:
       Sum += V
print(Sum)  
   