'''
02_Employee_Salary_Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []
'''
n = int(input('Enter the size of list: '))

print('Plz enter the salaries...')

salaries = []

i =0
while i < n:
   x = int(input('salary: '))
   salaries.append(x)
   i += 1
print(salaries)

avg = 0
sum = 0
count = 0
for i in range(n):
    sum += salaries[i]
    count += 1
    avg = sum // count
print('Average =',avg)

for i in range(n):
    if salaries[i] > avg:
       print('Above Average =',salaries[i])


for i in salaries[:]:
    if i < 15000:
       salaries.remove(i)
print('Remaining List =',salaries)





