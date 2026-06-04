'''
3.MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45
'''
row = int(input("Employee: "))
col = int(input("Month: "))

arr = []

for i in range(row):
    rows = []
    for j in range(col):
        rows.append(int(input()))
    arr.append(rows)

for i in range(row):
    for j in range(col):
       print(arr[i][j],end=' ')
    print() 

while  True:
  
    print("==MENU==")
    print("1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score")
    print("3. Display Employee-wise Maximum Score")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    match choice:
          case 1:
               m_sum = 0
               m_row = 0 
               for i in range(len(arr)):
                  total = 0
   
                  for j in range(len(arr[i])):
                     total += arr[i][j]
       
                  #print(f"Row {i+1} Sum = {total}") 

                  if total > m_sum:
                     m_sum = total
                     m_row = i + 1

               print()
               print(f"Employee {m_row} has Highest Total Score = {m_sum}")
  
          case 2:
               for i in range(col):
                  total = 0
                  count = 0
                  for j in range(row):
                     total += arr[j][i]
                     count += 1
                     avg = total /count

                  print(f"Month {i+1} Average = {avg }") 
               print()

          case 3: 
                
               for i in range(row):
                   max = arr[i][0] 
  
                   for j in range(col):
                     if arr[i][j] > max:
                        max = arr[i][j] 
              
                   print(f"Employee {i+1} Max Score = {max}")
    
          case 4:  
               print('Thank You for Using')

               break 



              
  