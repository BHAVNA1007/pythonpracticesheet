'''
7.A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)
'''

n = int(input("Enter no of  players:  "))

players = []

for i in range(n):
   print(f"Enter  player{i+1} details:")
   p_id = input("Enter  player id: ")
   p_name = input("Enter   player name: ")
   runs = int(input("Enter runs score: "))
   player = (p_id, p_name, runs )
   players.append(player)


print("\nAll  players")
for p in  players:
    print(p)

Highest = players[0]
for p in players:
    if Highest[2] < p[2]:
         Highest = p
print("\nHighest Scorer:")
print(Highest)


Lowest  = players[0]
for p in players:
    if Lowest[2] > p[2]:
         Lowest = p
print("\nLowest Scorer:")
print(Lowest)


count = 0
sum = 0
for p in players:
   count += 1
   sum += p[2]
   avg = sum / count

print("\nAverage Runs:", avg)
print("\nTotal Runs:", sum)

print("\nPlayers Scoring More Than 50 Runs: ")
for p in players:

    if  p[2] > 50:
        print(p)   



