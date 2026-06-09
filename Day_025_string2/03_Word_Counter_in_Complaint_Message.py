'''
3.Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5
'''
msg = input('Enter complaint: ')

msg1 = msg.split()
print(msg1)

count = 0
for words in msg1:
    count += 1

print(count)