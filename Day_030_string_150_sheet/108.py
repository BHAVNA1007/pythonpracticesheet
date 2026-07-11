'''

108 Check if a string is an isogram (no repeating letters). S = "ambidextrous" TRUE

'''

s = input("S: ")

unique = True

for i in range(len(s)):

    for j in range(i+1, len(s)):

        if s[i] == s[j]:

           unique = False

if unique:

    print("TRUE")

else:
 
    print("FALSE")

  