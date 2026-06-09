'''
81 Generate a hash code or UUID. 
S = "test" Hash: 3556498 (Example hash code)
'''
s=input("Enter s: ")
res=0
for i in s:
    res=res*31+ord(i)
print(res) 