'''
149 Check if two strings are scrambled versions of each other. S1 = "great", S2 = "rgeat" TRUE

'''

s1 = input("Enter a s1: ")
s2 = input("Enter a s2: ")

if sorted(s1)==sorted(s2) :
    print("True")

else:
    print("False")  