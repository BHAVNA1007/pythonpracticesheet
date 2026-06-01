'''
98 Check if the first 'z' is immediately followed by another 'z'. 
S1 = "zzyy", S2 = "zyzz" S1: True, S2: False

'''

s1 = input('Enter a string: ')

found=False

for i in range(len(s1)): 
    if s1[i]=="z":
        if s1[i+1]=="z":
            found=True
            break
        else:
            break
if found:
    print("True")
else:
    print("False")