'''Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0'''

principal, rate, time = map(int,input().split())
print(f"Principal = {principal}")
print(f"Rate = {rate}%")
print(f"Time = {time} years")

amount = principal*((1+(rate/100))**time)
print(f"Amount after interest = {amount}")

