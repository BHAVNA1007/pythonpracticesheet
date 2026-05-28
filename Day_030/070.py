'''
70 Compare the number of times 'the' and 'is' appear. 
S = "the cat is on the mat" the: 2, is: 1 (theis)
'''

s = input('Enter a string: ')

s1 = s.split()
th = 0
i_s = 0
for i in range(len(s1)):
   
    if s1[i] == 'the':
        th += 1
    elif s1[i] == "is":
        i_s += 1

print("the : ",th)
print("is: ", i_s)