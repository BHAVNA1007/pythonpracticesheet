'''
046_to_055_string

46 Check if a substring appears at both the start and end. 
   S = "abcabca", Sub="abca" TRUE

'''

#46 Check if a substring appears at both the start and end. 
#S = "abcabca", Sub="abca" TRUE


s = input("Enter the string: ")
sub = input("Enter the sub: ")
print(s.startswith(sub) and s.endswith(sub))

'''
s_w = True
if len(sub)>len(s):
    s_w = False

else:
    for i in range(len(sub)):
       if s[i] != sub[i]:
           s_w = False

e_w = True
if len(sub) > len(s):
    e_w  = False

else:
    end = len(s)-len(sub)
    for i in range(len(sub)):

        if s[end+i] != sub[i]:
           e_w = False
if s_w == True and e_w  == True:
     print("True")
else:
     print("False")













