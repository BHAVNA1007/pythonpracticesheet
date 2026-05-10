'''Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67'''

import math
total_runs = int(input("Total runs ="))
overs, ball =map(int,input().split())
print(f"Overs = {overs}.{ball}")
total_balls = (overs*6)+ball
print(f"Total Balls = {total_balls}")
run_rate = total_runs/(overs+ball)
print(f"Run Rate = {run_rate}")
