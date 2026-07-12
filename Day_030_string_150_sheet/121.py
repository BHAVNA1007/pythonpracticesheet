'''
121 Check if a string contains only binary digits (0/1). S1 = "1010", S2 = "102" S1: True, S2: False

'''

s = input("S: ")

is_binary = True

for ch in s:

   if ch != "1" and ch != "0":

        is_binary = False

if is_binary:

    print(True)

else:

    print(False) 