'''Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5'''


monthly_salary, working_days, wor_hr_p_day = map(int,input().split())
print(f"Monthly salary = {monthly_salary}")
print(f"Working hours per day = {working_days}")
print(f"Monthly salary = {wor_hr_p_day}")
salary_per_day = monthly_salary/working_days
print(f"Salary per day = {salary_per_day}")
salary_per_hour = monthly_salary/(working_days*wor_hr_p_day)
print(f"Salary per hour = {salary_per_hour}")
