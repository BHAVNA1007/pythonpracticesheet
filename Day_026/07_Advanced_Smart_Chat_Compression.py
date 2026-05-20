'''07_Advanced_Smart_Chat_Compression_Expansion_System

A messaging application stores repeated characters in compressed form to
reduce storage space. Before displaying messages to users, the system
should reconstruct the original message.

The application team has introduced additional rules.

Conditions: - Alphabet followed by number - Repeat character according
to the number - If alphabet is uppercase convert expanded characters
into lowercase - Ignore special symbols - Display expanded string -
Display total character count

Test Case 1 Input: Enter compressed message: a3

Output: Expanded Message: aaa

Total Characters: 3

Test Case 2 Input: Enter compressed message: A4b5

Output: Expanded Message: aaaabbbbb

Total Characters: 9

Test Case 3 Input: Enter compressed message: x2Y3

Output: Expanded Message: xxyyy

Total Characters: 5

Test Case 4 Input: Enter compressed message: m5@n2P4

Output: Expanded Message: mmmmmnnpppp

Total Characters: 11

Test Case 5 Input: Enter compressed message: R3S2t5

Output: Expanded Message: rrrssttttt

Total Characters: 10
'''


'''
07_Advanced_Smart_Chat_Compression_Expansion_System
'''

s = input("Enter compressed message: ")

result = ''

for i in range(len(s) - 1):

    ch = s[i]
    next = s[i + 1]

  
    if ((ch >= 'a' and ch <= 'z') or
        (ch >= 'A' and ch <= 'Z')) and (next >= '0' and nxt <= '9'):

        
        if ch >= 'A' and ch <= 'Z':
            ch = chr(ord(ch) + 32)

        result = result + ch * int(next)

print("Expanded Message:", result)
print("Total Characters:", len(result))


















