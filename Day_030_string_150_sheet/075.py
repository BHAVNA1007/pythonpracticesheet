'''
 75 Find the longest common prefix among strings.
 Strings = ["flower", "flow", "flight"] "fl"

'''

n = int(input("N: "))

strings = []

for i in range(n):

    strings.append(input(f"str{i+1} : "))

print(strings)

prefix = strings[0]

for s in strings[1:]:

   while not s.startswith(prefix):
       prefix = prefix[:-1]

print('longest common prefix is: ', prefix)


     