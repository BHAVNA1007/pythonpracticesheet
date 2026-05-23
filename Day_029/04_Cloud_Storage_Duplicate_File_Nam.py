'''
04_Cloud_Storage_Duplicate_File_Name_Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:
* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:
text
file file image file image data

### Output:
text
file file(1) image file(2) image(1) data
'''
s = input('Enter the string: ')
s1 = s.split()
print(s1)

for i in range(len(s1)):
    count = 0 

    for j in range(i):
      
        if s1[i] == s1[j]:
           count += 1

    if count == 0:
        print(s1[i],end=' ')
    else:
        print(f'{s1[i]}({count})', end=' ')           
    
         