'''
5.

=========================================
WORD LENGTH GROUPING
====================

A content management system stores article tags.

tags = ["python","java","api","react","html","css"]

Write a program to:

* Group words according to their length.
* Store result in dictionary.

Sample Output:
{
3:['api','css'],
4:['java','html'],
5:['react'],
6:['python']
}
'''
n = int(input("Enter size of com: "))

pages = []
for p in range(n):
    pages.append(input())
print(pages)

group = {}
for w in pages:
    length = len(w)
    if length not in group:
        group[length] = []
        
    group[length].append(w)
print(group)    



 
