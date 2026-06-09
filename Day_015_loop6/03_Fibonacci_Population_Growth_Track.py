'''3.Fibonacci Population Growth Tracker

A wildlife research team is studying the growth of a rare species.  
They observe that the population follows a Fibonacci pattern:

- Month 1 → 0 animals  
- Month 2 → 1 animal  
- Every next month → sum of previous two months  

The researchers want to analyze the growth pattern.

Write a program to:

- Read number of months n
- Generate Fibonacci series up to n months using loop
- Print population for each month
- Find total population observed
- Count how many months population exceeded 5

Input:
8

Output:
Population Growth:
0 1 1 2 3 5 8 13

Total Population = 33
Months with Population > 5 = 2
'''
num = int(input("Enter The Number Of Months = "))

f_population = 0
s_population = 1
total_population = 0

count = 0

for i in range(num):
    print("Population Growth: ", f_population)
    t_population = f_population + s_population
    if  f_population > 5:
        count += 1


    f_population = s_population
    s_population = t_population
    

    total_population = total_population + f_population

print("Total Population = ", total_population)
print("Months with Population > 5 = ", count)
    

  
    
    
