'''
83 Create a string from a byte array. 
Byte[] = {72, 101, 108} (ASCII for H, e, l) "Hel"

'''

arr = input('Enter byte: ').split()

print("Byte[] = ",arr)

res = ''
for i in arr:
   
   res = res + chr(int(i))

print(res)

