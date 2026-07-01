'''
104 Check if a string contains balanced brackets of all types ((), {}, []).

S = "{[()]}" TRUE

'''

s = input("Enter brackets: ")

oc_brackets = 0
cc_brackets = 0

os_brackets = 0
cs_brackets = 0

of_brackets = 0
cf_brackets = 0

for i in s:
  if i == "{":
     oc_brackets += 1

  elif i == "}":
     cc_brackets += 1
  
  elif i == "[":
     os_brackets += 1

  elif i == "]":
     cs_brackets += 1

  elif i == "(":
     of_brackets += 1

  elif i == ")":
     cf_brackets += 1


if oc_brackets == cc_brackets and os_brackets == cs_brackets   and of_brackets == cf_brackets:
   print("TRUE")

else:
   print("FALSE")





