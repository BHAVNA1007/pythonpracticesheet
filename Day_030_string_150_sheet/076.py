
'''
076

76 Find the longest common suffix among strings. Strings = ["baking", "making", "taking"] "king"

'''

n = int(input("Enter N: "))

strings = []

for i in range(n):
    strings.append(input(f"str {i+1}: "))
print(strings)

suffix = strings[0]

for s in strings[1:]:

    while not s.endswith(suffix):
  
         suffix = suffix[1:]

print(suffix)

