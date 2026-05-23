'''
05_Social_Media_Hashtag_Trend_Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.
### Input:
text
aabcbcdbca

### Output:
text
dbca

### Explanation:
dbca contains all unique characters: a,b,c,d
'''
s = input('Enter the string: ')

long = ''

for i in range(len(s)):
    temp = ''
    for j in range(i,len(s)):
        if s[j] not in temp:
            temp += s[j]
        else:
            break 
    if len(temp) > len(long):
        long = temp
   
print(long)          