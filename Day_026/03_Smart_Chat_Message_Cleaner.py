'''
03_Smart_Chat_Message_Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy
'''

msg = input('Enter the message: ')

cln_msg=''

space = False

for ch in msg:
    if ch !=' ':
       cln_msg += ch
       space = False
    else:
       if space == False:
          cln_msg += ch
          space = True

print('Cleaned Message: ',cln_msg)  
