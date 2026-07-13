'''

132 Check if a string is a valid IP address. S = "192.168.1.1" TRUE

'''
import re
s = input("Enter IP address: ")

pattern = r'^\d+\.\d+\.\d+\.\d+$'

if re.match(pattern, s):

    print(True)

else:

    print(False)